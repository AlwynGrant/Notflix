from .db import db

watchlist = db.Table(
    "watchlist",
    db.Column(
        "movie_id",
        db.Integer,
        db.ForeignKey("movies.id"),
        primary_key=True
    ),
    db.Column(
        "profile_id",
        db.Integer,
        db.ForeignKey("profiles.id"),
        primary_key=True
    )
)
