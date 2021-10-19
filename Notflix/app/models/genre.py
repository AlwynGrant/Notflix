from .db import db
from .movie_genre import movie_genres

class Genre(db.Model):
    __tablename__ = 'genres'

    id = db.Column(db.Integer, primary_key=True)
    genre = db.Column(db.String(100), nullable=False)


    movies = db.relationship(
        "Movie",
        back_populates="genres",
        secondary=movie_genres
    )

    def to_dict(self):
        return {
            'id': self.id,
            'genre': self.genre
        }
