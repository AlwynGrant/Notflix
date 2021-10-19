from .db import db
from .movie_genre import movie_genres
from .like import likes
from .watchlist import watchlist

class Movie(db.Model):
    __tablename__ = 'movies'

    id = db.Column(db.Integer, primary_key=True)
    movie_url  = db.Column(db.String(2000), nullable=False)
    movie_thumbnail  = db.Column(db.String(2000), nullable=False)
    name  = db.Column(db.String(50), nullable=False)
    description  = db.Column(db.String(500), nullable=False)
    year_released  = db.Column(db.Int, nullable=False)
    production  = db.Column(db.String(100), nullable=False)
    maturity_rating  = db.Column(db.String(20), nullable=False)
    director  = db.Column(db.String(100), nullable=False)
    cast  = db.Column(db.String(500), nullable=False)
    run_time  = db.Column(db.String(20), nullable=False)
    rating = db.Column(db.Int, nullable=False)
    kids = db.Column(db.Boolean, default=False)

    genres = db.relationship(
        "Genre",
        back_populates="movies",
        secondary=movie_genres
    )

    movie_likes = db.relationship(
        "Profile",
        back_populates="user_likes",
        secondary=likes
    )

    profiles_that_added_this_movie = db.relationship(
        "Profile",
        back_populates="my_list",
        secondary=watchlist
    )

    def to_dict(self):
        return {
            'id': self.id,
            'movie_url': self.movie_url,
            'movie_thumbnail': self.movie_thumbnail,
            'name': self.name,
            'description': self.description,
            'year_released': self.year_released,
            'production': self.production,
            'maturity_rating': self.maturity_rating,
            'director': self.director,
            'cast': self.cast,
            'run_time': self.run_time,
            'rating': self.rating,
            'kids': self.kids,
            'movie_likes': [(profile.id) for profile in self.movie_likes],
            'genres': [(genre.genre) for genre in self.genres]
        }
