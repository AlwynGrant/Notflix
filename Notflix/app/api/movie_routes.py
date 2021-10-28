from flask import Blueprint, request
from flask_login import login_required
from app.models import db, Movie, Profile

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
    movie = Movie.query.get(movie_id)
    return movie.to_dict()
