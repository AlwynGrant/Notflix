from flask import Blueprint, jsonify
from flask_login import login_required, current_user
from app.models import User, Profile, Movie

profile_routes = Blueprint('profiles', __name__)

# profiles page
# get session users profiles
@profile_routes.route('')
@login_required
def profile():
    profiles = Profile.query.filter(Profile.user_id == int(current_user.get_id()))
    return {'profiles': [profile.to_dict() for profile in profiles]}


# PLACEHOLDER
@profile_routes.route('/PLACEHOLDER')
@login_required
def pick_profile():
    pass
