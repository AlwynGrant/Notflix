from flask import Blueprint, jsonify, request
from flask_login import login_required, current_user
from app.models import db, User, Profile, Movie
from app.forms import NewProfileForm, EditProfileForm

profile_routes = Blueprint('profiles', __name__)

# profiles page
# get session users profiles
@profile_routes.route('')
@login_required
def profile():
    profiles = Profile.query.filter(
        Profile.user_id == int(current_user.get_id())
    )

    return {'profiles': [profile.to_dict() for profile in profiles]}

# browse page
# get session users selected profile
@profile_routes.route('/<int:profile_id>')
@login_required
def pick_profile(profile_id):
    profile = Profile.query.get(profile_id)

    if int(current_user.get_id()) == profile.user_id:
        return profile.to_dict()


# browse page
# get session users selected profiles
@profile_routes.route('/new', methods=['POST'])
@login_required
def new_profile():
    form = NewProfileForm()
    form["csrf_token"].data = request.cookies["csrf_token"]

    if form.validate_on_submit():

        new_profile = Profile(
            user_id=current_user.get_id(),
            username=form.username.data,
            profile_img=form.profile_img.data,
            kids=form.kids.data
        )

        db.session.add(new_profile)
        db.session.commit()
        return new_profile.to_dict()


# edit profile
@profile_routes.route('/<int:profile_id>/edit', methods=['PATCH'])
@login_required
def edit_profile(profile_id):
    profile = Profile.query.get(profile_id)

    form = EditProfileForm()
    form["csrf_token"].data = request.cookies["csrf_token"]

    if form.validate_on_submit():
        profile.username = form.username.data
        profile.profile_img = form.profile_img.data
        profile.kids = form.kids.data

        db.session.commit()

        updated_profile = Profile.query.get(profile_id)

        return updated_profile.to_dict()

# delete profile
@profile_routes.route('/<int:profile_id>/delete', methods=['DELETE'])
@login_required
def delete_profile(profile_id):
    profile = Profile.query.get(profile_id)

    user_id = current_user.get_id()

    if int(user_id) == int(profile.user_id):

        db.session.delete(profile)
        db.session.commit()

    return profile.to_dict()
