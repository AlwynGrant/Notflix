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
    pass

# add or remove from movie list


@movie_routes.route('/<int:profile_id>/like', methods=['POST'])
@login_required
def edit_mylist(profile_id):
    movie = request.json['movie']
    likes = movie.movie_likes
    dislikes = movie.movie_dislikes


    if profile_id in likes:
        # unlike movie path
        likes.remove(profile_id)
        dislikes.append(profile_id)
        # update the movie rating
        total = len(likes) + len(dislikes)
        movie.rating = (len(likes) / total) * 100
        db.session.commit()
    else:
        # like movie path
        dislikes.remove(profile_id)
        likes.append(profile_id)
        # update the movie rating
        total = len(likes) + len(dislikes)
        movie.rating = (len(likes) / total) * 100

        db.session.commit()

    return movie.to_dict()
