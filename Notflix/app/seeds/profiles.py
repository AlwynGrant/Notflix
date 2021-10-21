from app.models import db, User, Profile


# Adds a demo user, you can add other users here if you want
def seed_profiles():
    democritus = Profile(
        user_id=1,
        username='Democritus',
        profile_img='https://kickrbucket.s3.us-west-1.amazonaws.com/1634746455038.jpg',
        kids=False
    )
    mom = Profile(
        user_id=1,
        username='Mom',
        profile_img='https://kickrbucket.s3.us-west-1.amazonaws.com/1634746445926.png',
        kids=False
    )
    leech = Profile(
        user_id=1,
        username='Leech',
        profile_img='https://kickrbucket.s3.us-west-1.amazonaws.com/1634746427415.png',
        kids=False
    )
    kids = Profile(
        user_id=1,
        username='Kids',
        profile_img='https://kickrbucket.s3.us-west-1.amazonaws.com/1634746854870.jpg',
        kids=True
    )

    db.session.add(democritus)
    db.session.add(mom)
    db.session.add(leech)
    db.session.add(kids)

    db.session.commit()


# Uses a raw SQL query to TRUNCATE the users table.
# SQLAlchemy doesn't have a built in function to do this
# TRUNCATE Removes all the data from the table, and RESET IDENTITY
# resets the auto incrementing primary key, CASCADE deletes any
# dependent entities
def undo_profiles():
    db.session.execute('TRUNCATE profiles RESTART IDENTITY CASCADE;')
    db.session.commit()
