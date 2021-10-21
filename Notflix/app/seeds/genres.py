from operator import ge
from app.models import db, Genre


# Adds a demo user, you can add other users here if you want
def seed_genres():
    action_adventure = Genre(genre='Action/Adventure')
    anime = Genre(genre='Anime')
    comedy = Genre(genre='Comedy')
    documentary = Genre(genre='Documentary')
    horror = Genre(genre='Horror')
    romance = Genre(genre='Romance')
    thrillers = Genre(genre='Thrillers')

    db.session.add(action_adventure)
    db.session.add(anime)
    db.session.add(comedy)
    db.session.add(documentary)
    db.session.add(horror)
    db.session.add(romance)
    db.session.add(thrillers)

    db.session.commit()


# Uses a raw SQL query to TRUNCATE the users table.
# SQLAlchemy doesn't have a built in function to do this
# TRUNCATE Removes all the data from the table, and RESET IDENTITY
# resets the auto incrementing primary key, CASCADE deletes any
# dependent entities
def undo_genres():
    db.session.execute('TRUNCATE genres RESTART IDENTITY CASCADE;')
    db.session.commit()
