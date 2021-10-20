from flask import Blueprint, jsonify
from flask_login import login_required
from app.models import User, Profile, Movie

profile_routes = Blueprint('profiles', __name__)

# profiles page
@profile_routes.route('')
@login_required
def profile():
    pass
    # users = User.query.all()
    # return {'users': [user.to_dict() for user in users]}


# PLACEHOLDER
@profile_routes.route('/PLACEHOLDER')
@login_required
def profile():
    pass
