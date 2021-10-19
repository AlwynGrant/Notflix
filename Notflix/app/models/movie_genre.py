from .db import db

movie_genres = db.Table(
    "movie_genres",
    db.Column(
        "movie_id",
        db.Integer,
        db.ForeignKey("movies.id"),
        primary_key=True
    ),
    db.Column(
        "genre_id",
        db.Integer,
        db.ForeignKey("genres.id"),
        primary_key=True
    )
)
