from flask import Blueprint, jsonify, request
from flask_login import login_required, current_user
from app.models import db, User, Profile, Movie
from app.forms import NewProfileForm

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
# get session users selected profiles
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
