from re import M
from app.models import db, User, Movie


# Adds a demo user, you can add other users here if you want
def seed_movies():
    # HORROR ====================================================================================================================
    deep_blue_sea_2 = Movie(
        movie_url='https://notflix-clone-bucket.s3.us-west-1.amazonaws.com/horrors/DEEP+BLUE+SEA+2+Official+Trailer+(2018)+Shark+Movie+HD-(1080p).mp4',
        movie_thumbnail='https://notflix-clone-bucket.s3.us-west-1.amazonaws.com/horror_THUMBNAILS/deep-blue-sea-2-movie-poster-md.jpg',
        name = 'Deep Blue Sea 2',
        description='A brilliant billionaire creates five genetically altered bull sharks, which proceed to wreak havoc for a group of scientists on an isolated research facility.',
        year_released = 2018,
        production='Tom Siegrist',
        maturity_rating = 'R',
        director= 'Darin Scott',
        cast = 'Danielle Savre, Rob Meyes, Michael Beach, Nathan Lynn, Kim Syster, Jeremy Boado, Adrian Collins, Cameronm Robertson',
        run_time = '1h 34min',
        rating = 0,
        kids = False
    )


    grave_encounters = Movie(
        movie_url='https://notflix-clone-bucket.s3.us-west-1.amazonaws.com/horrors/Grave+Encounters+-+Official+Trailer-(1080p).mp4',
        movie_thumbnail='https://notflix-clone-bucket.s3.us-west-1.amazonaws.com/horror_THUMBNAILS/grave_encounters_thumb.jpg',
        name = 'Grave Encounters',
        description='For their ghost hunting reality show, a production crew locks themselves inside an abandoned mental hospital that\'s supposedly haunted - and it might prove to be all too true.',
        year_released = 2011,
        production= 'Shawn Angelski, Michael Karlin',
        maturity_rating = 'Not Rated',
        director= 'The Vicious Brothers',
        cast= 'Sean Rogerson, Ashleigh Gryzko, Mackenzie Gray, Juan Riedinger, Merwin Mondesir, Matthew K McBride',
        run_time='1h 32min',
        rating = 0,
        kids = False
    )

    insidious_2 = Movie(
        movie_url='https://notflix-clone-bucket.s3.us-west-1.amazonaws.com/horrors/Insidious_+Chapter+2+Official+Trailer.mp4',
        movie_thumbnail='https://notflix-clone-bucket.s3.us-west-1.amazonaws.com/horror_THUMBNAILS/HD-wallpaper-insidious-chapter-2-2013-movie-thumbnail.jpg',
        name = 'Insidious II',
        description='The Lamberts believe that they have defeated the spirits that have haunted their family, but they soon discover that evil is not beaten so easily.',
        year_released = 2013,
        production= 'Jason Blum, Oren Peli',
        maturity_rating = 'PG-13',
        director='James Wan',
        cast= 'Patrick Wilson, Rose Byrne, Lin Shaye, Ty Simpkins, Barbara Hershey',
        run_time='1h 46min',
        rating = 0,
        kids = False
    )
    it_comes_at_night = Movie(
        movie_url='https://notflix-clone-bucket.s3.us-west-1.amazonaws.com/horrors/It+Comes+At+Night+_+Official+Trailer+HD+_+A24-(1080p).mp4',
        movie_thumbnail='https://notflix-clone-bucket.s3.us-west-1.amazonaws.com/horror_THUMBNAILS/it_comes_at_night.jpg',
        name = 'It Comes at Night',
        description='Secure within a desolate home as an unnatural threat terrorizes the world, a man has established a tenuous domestic order with his wife and son. Then a desperate young family arrives seeking refuge.',
        year_released = 2017,
        production= 'David Kaplan, Andrea Roa',
        maturity_rating = 'R',
        director='Trey Edward Shults',
        cast= 'Joel Edgerton, Christopher Abbott, Carmen Ejogo, Kelvin Harrison Jr., Riley Keough',
        run_time='1h 31min',
        rating = 0,
        kids = False
    )

    hush = Movie(
        movie_url='https://notflix-clone-bucket.s3.us-west-1.amazonaws.com/horrors/Official+Trailer+1+(2016)+-+HUSH-(1080p).mp4',
        movie_thumbnail='https://notflix-clone-bucket.s3.us-west-1.amazonaws.com/horror_THUMBNAILS/hush-582501e40a770.jpg',
        name = 'Hush',
        description='A deaf and mute writer who retreated into the woods to live a solitary life must fight for her life in silence when a masked killer appears at her window.',
        year_released = 2016,
        production= 'Trevor Macy, Jason Blum',
        maturity_rating = 'R',
        director='Mike Flanagan',
        cast= 'John Gallagher Jr., Michael Trucco, Kate Siegel',
        run_time='1h 22min',
        rating = 0,
        kids = False
    )

    paranormal_activity_2 = Movie(
        movie_url='https://notflix-clone-bucket.s3.us-west-1.amazonaws.com/horrors/Paranormal+Activity+2+Trailer-(480p).mp4',
        movie_thumbnail='https://notflix-clone-bucket.s3.us-west-1.amazonaws.com/horror_THUMBNAILS/paranormal-2.jpg',
        name='Paranormal Activity 2',
        description='After experiencing what they think are a series of "break-ins", a family sets up security cameras around their home, only to realize that the events unfolding before them are more sinister than they seem.',
        year_released = 2010,
        production='Blumhouse Productions',
        maturity_rating = 'R',
        director='Tod Williams',
        cast= 'Sprague Grayden, Brian Boland, Molly Ephraim, Katie Featherston',
        run_time='1h 31min',
        rating = 0,
        kids = False
    )
    quarantine = Movie(
        movie_url='https://notflix-clone-bucket.s3.us-west-1.amazonaws.com/horrors/Quarantine+(2008)+-+Trailer+1080p-(1080p).mp4',
        movie_thumbnail='https://notflix-clone-bucket.s3.us-west-1.amazonaws.com/horror_THUMBNAILS/quarantine.jpg',
        name='Quarantine',
        description='A television reporter and her cameraman are trapped inside a building quarantined by the CDC, after the outbreak of a mysterious virus which turns humans into bloodthirsty killers.',
        year_released = 2008,
        production= 'Sergio Aguero, Doug Davison, Roy Lee',
        maturity_rating = 'R',
        director='John Erick Dowdle',
        cast= 'Jennifer Carpenter, Jay Hernandez, Columbus Short, Greg Germann, Steve Harris, Dania Ramirez, Rade Šerbedžija, Johnathon Schaech',
        run_time='1h 29min',
        rating = 0,
        kids = False
    )
    rings = Movie(
        movie_url='https://notflix-clone-bucket.s3.us-west-1.amazonaws.com/horrors/Rings+_+Trailer+%231+_+Paramount+Pictures+International-(1080p).mp4',
        movie_thumbnail='https://notflix-clone-bucket.s3.us-west-1.amazonaws.com/horror_THUMBNAILS/rings.jpg',
        name='Rings',
        description='A young woman finds herself on the receiving end of a terrifying curse that threatens to take her life in 7 days.',
        year_released = 2017,
        production='Walter F. Parkes, Laurie MacDonald',
        maturity_rating= 'PG-13',
        director='F. Javier Gutiérrez',
        cast= 'Matilda Lutz, Alex Roe, Johnny Galecki, Aimee Teegarden, Bonnie Morgan, Vincent D\'Onofrio',
        run_time='1h 42min',
        rating = 0,
        kids = False
    )
    the_conjuring_2 = Movie(
        movie_url='https://notflix-clone-bucket.s3.us-west-1.amazonaws.com/horrors/The+Conjuring+2+-+Main+Trailer+%5BHD%5D-(1080p).mp4',
        movie_thumbnail='https://notflix-clone-bucket.s3.us-west-1.amazonaws.com/horror_THUMBNAILS/the_conjuring_2.jpg',
        name='The Conjuring 2',
        description='Ed and Lorraine Warren travel to North London to help a single mother raising four children alone in a house plagued by a supernatural spirit.',
        year_released = 2016,
        production= 'Peter Safran, Rob Cowan, James Wan',
        maturity_rating= 'R',
        director='James Wan',
        cast='Vera Farmiga, Patrick Wilson, Frances O\'Connor, Madison Wolfe, Simon McBurney, Franka Potente',
        run_time='2h 14min',
        rating = 0,
        kids = False
    )
    unfriended = Movie(
        movie_url='https://notflix-clone-bucket.s3.us-west-1.amazonaws.com/horrors/Unfriended+-+Official+Trailer+(HD)-(1080p).mp4',
        movie_thumbnail='https://notflix-clone-bucket.s3.us-west-1.amazonaws.com/horror_THUMBNAILS/unfriended-movie.jpg',
        name='Unfriended',
        description='A group of online chatroom friends find themselves haunted by a mysterious, supernatural force using the account of their dead friend.',
        year_released=2014,
        production= 'Timur Bekmambetov, Nelson Greaves',
        maturity_rating = 'R',
        director='Leo Gabriadze',
        cast= 'Shelley Hennig, Moses Storm, Renee Olstead, Will Peltz, Jacob Wysocki, Courtney Halverson, Heather Sossaman',
        run_time='1h 23min',
        rating = 0,
        kids = False
    )

    db.session.add(deep_blue_sea_2)
    db.session.add(grave_encounters)
    db.session.add(insidious_2)
    db.session.add(it_comes_at_night)
    db.session.add(hush)
    db.session.add(paranormal_activity_2)
    db.session.add(quarantine)
    db.session.add(rings)
    db.session.add(the_conjuring_2)
    db.session.add(unfriended)


# HORROR ====================================================================================================================

    movie = Movie(
        movie_url = None,
        movie_thumbnail=None,
        name=None,
        description=None,
        year_released=None,
        production=None,
        maturity_rating=None,
        director=None,
        cast=None,
        run_time=None,
        rating=None,
        kids=False
    )





    db.session.commit()



# Uses a raw SQL query to TRUNCATE the users table.
# SQLAlchemy doesn't have a built in function to do this
# TRUNCATE Removes all the data from the table, and RESET IDENTITY
# resets the auto incrementing primary key, CASCADE deletes any
# dependent entities
def undo_movies():
    db.session.execute('TRUNCATE movies RESTART IDENTITY CASCADE;')
    db.session.commit()
