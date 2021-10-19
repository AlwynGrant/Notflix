from .db import db

likes = db.Table(
    "likes",
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
