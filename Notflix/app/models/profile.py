from .db import db
from .like import likes
from .watchlist import watchlist

class Profile(db.Model):
    __tablename__ = 'profiles'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    username = db.Column(db.String(50), nullable=False)
    profile_img = db.Column(db.String(1000))
    kids = db.Column(db.Boolean, default=False)

    user_likes = db.relationship(
        "Movie",
        back_populates="movie_likes",
        secondary=likes
    )

    user_dislikes = db.relationship(
        "Movie",
        back_populates="movie_dislikes",
        secondary=likes
    )

    my_list = db.relationship(
        "Movie",
        back_populates="profiles_that_added_this_movie",
        secondary=watchlist
    )

    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'username': self.username,
            'profile_img': self.profile_img,
            'kids': self.kids,
            'my_list': [movie.to_dict() for movie in self.my_list],
            'profile_likes': [movie.to_dict() for movie in self.user_likes]
        }
