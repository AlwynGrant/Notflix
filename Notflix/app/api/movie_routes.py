from flask import Blueprint
from flask_login import login_required, current_user
from app.models import db, Profile, Movie

movie_routes = Blueprint('movies', __name__)

# list all movies
@movie_routes.route('')
@login_required
def movies():
    movies = Movie.query.all()
    return {'movies': [movie.to_dict() for movie in movies]}

# specific movie modal/video player
@movie_routes.route('/<int:movie_id>')
@login_required
def watch_movie(movie_id):
    pass