from re import M
from app.models import db, User, Movie, Genre


# Adds a demo user, you can add other users here if you want
def seed_movies():
    # HORROR ====================================================================================================================
    deep_blue_sea_2 = Movie(
        movie_url='https://notflix-clone-bucket.s3.us-west-1.amazonaws.com/horrors/DEEP+BLUE+SEA+2+Official+Trailer+(2018)+Shark+Movie+HD-(1080p).mp4',
        movie_thumbnail='https://notflix-clone-bucket.s3.us-west-1.amazonaws.com/horror_THUMBNAILS/deep_blue_sea_2.jpg',
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

    deep_blue_sea_2.genres.append(Genre.query.get(5))
    grave_encounters.genres.append(Genre.query.get(5))
    insidious_2.genres.append(Genre.query.get(5))
    it_comes_at_night.genres.append(Genre.query.get(5))
    hush.genres.append(Genre.query.get(5))
    paranormal_activity_2.genres.append(Genre.query.get(5))
    quarantine.genres.append(Genre.query.get(5))
    rings.genres.append(Genre.query.get(5))
    the_conjuring_2.genres.append(Genre.query.get(5))
    unfriended.genres.append(Genre.query.get(5))

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




# THRILLERS ====================================================================================================================

    zodiac = Movie(
        movie_url='https://notflix-clone-bucket.s3.us-west-1.amazonaws.com/thrillers/yt5s.com-Zodiac+(2007)+Trailer+%231+_+Movieclips+Classic+Trailers-(1080p).mp4',
        movie_thumbnail='https://notflix-clone-bucket.s3.us-west-1.amazonaws.com/Thrillers_THUMBNAILS/ZODIAC-ant.jpg',
        name='Zodiac',
        description='Between 1968 and 1983, a San Francisco cartoonist becomes an amateur detective obsessed with tracking down the Zodiac Killer, an unidentified individual who terrorizes Northern California with a killing spree.',
        year_released=2007,
        production='Phoenix Pictures',
        maturity_rating='R',
        director='David Fincher',
        cast='Jake Gyllenhaal, Mark Ruffalo, Robert Downey Jr., Anthony Edwards, Brian Cox, Elias Koteas, Donal Logue, John Carroll Lynch, Dermot Mulroney, Chloë Sevigny',
        run_time='2h 37min',
        rating=0,
        kids=False
    )
    the_hateful_8 = Movie(
        movie_url='https://notflix-clone-bucket.s3.us-west-1.amazonaws.com/thrillers/yt5s.com-The+Hateful+Eight+Official+Teaser+Trailer+%231+(2015)+-+Samuel+L.+Jackson+Movie+HD-(1080p).mp4',
        movie_thumbnail='https://notflix-clone-bucket.s3.us-west-1.amazonaws.com/Thrillers_THUMBNAILS/Hteful-Eight.jpg',
        name='The Hateful Eight',
        description='In the dead of a Wyoming winter, a bounty hunter and his prisoner find shelter in a cabin currently inhabited by a collection of nefarious characters.',
        year_released=2015,
        production='Shiny Penny, FilmColony',
        maturity_rating='R',
        director='Quentin Tarantino',
        cast='Samuel L. Jackson, Kurt Russell, Jennifer Jason Leigh, Walton Goggins, Demián Bichir, Tim Roth, Michael Madsen, Bruce Dern, James Parks, Channing Tatum',
        run_time='2h 48min',
        rating=0,
        kids=False
    )
    snowden = Movie(
        movie_url='https://notflix-clone-bucket.s3.us-west-1.amazonaws.com/thrillers/yt5s.com-Shutter+Island+(2010)+Trailer+%231+_+Movieclips+Classic+Trailers-(1080p).mp4',
        movie_thumbnail='https://notflix-clone-bucket.s3.us-west-1.amazonaws.com/Thrillers_THUMBNAILS/snowden_thumb.jpg',
        name='Snowden',
        description='The NSA\'s illegal surveillance techniques are leaked to the public by one of the agency\'s employees, Edward Snowden, in the form of thousands of classified documents distributed to the press.',
        year_released=2016,
        production='Endgame Entertainment, Vendian Entertainment, KrautPack Entertainment',
        maturity_rating='R',
        director='Oliver Stone',
        cast='Joseph Gordon-Levitt, Shailene Woodley, Melissa Leo, Zachary Quinto, Tom Wilkinson, Scott Eastwood, Logan Marshall-Green, Timothy Olyphant, Ben Schnetzer, LaKeith Lee Stanfield, Rhys Ifans, Nicolas Cage',
        run_time='2h 14min',
        rating=0,
        kids=False
    )
    the_da_vinci_code = Movie(
        movie_url='https://notflix-clone-bucket.s3.us-west-1.amazonaws.com/thrillers/yt5s.com-THE+DA+VINCI+CODE+-+Official+Trailer+%5B2006%5D+(HD)-(1080p).mp4',
        movie_thumbnail='https://notflix-clone-bucket.s3.us-west-1.amazonaws.com/Thrillers_THUMBNAILS/The-Da-Vinci-Code-Netflix.jpg',
        name='The Da Vinci Code',
        description='A murder inside the Louvre, and clues in Da Vinci paintings, lead to the discovery of a religious mystery protected by a secret society for two thousand years, which could shake the foundations of Christianity.',
        year_released=2006,
        production='Columbia Pictures, Imagine Entertainment',
        maturity_rating='PG-13',
        director='Ron Howard',
        cast='Tom Hanks, Audrey Tautou, Ian McKellen, Alfred Molina, Jürgen Prochnow, Paul Bettany, Jean Reno',
        run_time='2h 29min',
        rating=0,
        kids=False
    )
    shutter_island = Movie(
        movie_url='https://notflix-clone-bucket.s3.us-west-1.amazonaws.com/thrillers/yt5s.com-Shutter+Island+(2010)+Trailer+%231+_+Movieclips+Classic+Trailers-(1080p).mp4',
        movie_thumbnail='https://notflix-clone-bucket.s3.us-west-1.amazonaws.com/Thrillers_THUMBNAILS/shutter-island-poster.jpg',
        name='Shutter Island',
        description='In 1954, a U.S. Marshal investigates the disappearance of a murderer who escaped from a hospital for the criminally insane.',
        year_released=2010,
        production='Phoenix Pictures, Sikelia Productions',
        maturity_rating='R',
        director='Martin Scorsese',
        cast='Leonardo DiCaprio, Mark Ruffalo, Ben Kingsley, Michelle Williams, Emily Mortimer, Patricia Clarkson, Max von Sydow',
        run_time='2h 18min',
        rating=0,
        kids=False
    )
    triple_9 = Movie(
        movie_url='https://notflix-clone-bucket.s3.us-west-1.amazonaws.com/thrillers/yt5s.com-Triple+9+Official+Trailer+%231+(2016)+-+Kate+Winslet%2C+Woody+Harrelson+Movie+HD-(1080p).mp4',
        movie_thumbnail='https://notflix-clone-bucket.s3.us-west-1.amazonaws.com/Thrillers_THUMBNAILS/triple_9.jpg',
        name='Triple 9',
        description='A gang of criminals and corrupt cops plan the murder of a police officer in order to pull off their biggest heist yet across town.',
        year_released=2016,
        production='Worldview Entertainment, Sierra Pictures, Anonymous Content, MadRiver Pictures, SureFire Capital',
        maturity_rating='R',
        director='John Hillcoat',
        cast='Casey Affleck, Chiwetel Ejiofor, Anthony Mackie, Aaron Paul, Clifton Collins Jr., Norman Reedus, Gal Gadot, Woody Harrelson, Kate Winslet',
        run_time='1h 55min',
        rating=0,
        kids=False
    )
    the_machinist = Movie(
        movie_url='https://notflix-clone-bucket.s3.us-west-1.amazonaws.com/thrillers/yt5s.com-Machinist+Trailer+(2004)-(480p).mp4',
        movie_thumbnail='https://notflix-clone-bucket.s3.us-west-1.amazonaws.com/Thrillers_THUMBNAILS/THE_MACHINIST.jpg',
        name='The Machinist',
        description='An industrial worker who hasn\'t slept in a year begins to doubt his own sanity.',
        year_released=2004,
        production='Castelao Productions, Canal+, ICAA ICF',
        maturity_rating='R',
        director='Brad Anderson',
        cast='Christian Bale, Jennifer Jason Leigh, Aitana Sánchez-Gijón, John Sharian, Michael Ironside',
        run_time='1h 41min',
        rating=0,
        kids=False
    )
    the_whole_truth = Movie(
        movie_url='https://notflix-clone-bucket.s3.us-west-1.amazonaws.com/thrillers/yt5s.com-The+Whole+Truth+Official+Trailer+1+(2016)+-+Keanu+Reeves+Movie-(1080p).mp4',
        movie_thumbnail='https://notflix-clone-bucket.s3.us-west-1.amazonaws.com/Thrillers_THUMBNAILS/the-whole-truth.jpg',
        name='The Whole Truth',
        description='A defense attorney works to get his teenage client acquitted of murdering his wealthy father.',
        year_released=2016,
        production='FilmNation Entertainment, PalmStar Entertainment, Likely Story, Merced Media',
        maturity_rating='R',
        director='Courtney Hunt',
        cast='Keanu Reeves, Renée Zellweger, Gugu Mbatha-Raw, Gabriel Basso, Jim Belushi',
        run_time='1h 33min',
        rating=0,
        kids=False
    )
    The_bank_job = Movie(
        movie_url='https://notflix-clone-bucket.s3.us-west-1.amazonaws.com/thrillers/yt5s.com-The+Bank+Job+-+Trailer+%5BHD%5D.mp4',
        movie_thumbnail='https://notflix-clone-bucket.s3.us-west-1.amazonaws.com/Thrillers_THUMBNAILS/bank-jop.jpg',
        name='The Bank Job',
        description='Martine offers Terry a lead on a foolproof bank hit on London\'s Baker Street. She targets a roomful of safe deposit boxes worth millions in cash and jewelry along with a treasure trove of dirty secrets.',
        year_released=2008,
        production='Mosaic Media Group, Relativity Media LLC, Skyline(Baker St.) Productions',
        maturity_rating='R',
        director='Roger Donaldson',
        cast='Jason Statham',
        run_time='1h 51min',
        rating=0,
        kids=False
    )
    knives_out = Movie(
        movie_url='https://notflix-clone-bucket.s3.us-west-1.amazonaws.com/thrillers/yt5s.com-Knives+Out+Trailer+%231+(2019)+_+Movieclips+Trailers-(1080p).mp4',
        movie_thumbnail='https://notflix-clone-bucket.s3.us-west-1.amazonaws.com/Thrillers_THUMBNAILS/Knives-Out-Film-Poster-1.jpg',
        name='Knives Out',
        description='A detective investigates the death of a patriarch of an eccentric, combative family.',
        year_released=2019,
        production='T-Street',
        maturity_rating='PG-13',
        director='Rian Johnson',
        cast='Daniel Craig, Chris Evans, Ana de Armas, Jamie Lee Curtis, Michael Shannon, Don Johnson, Toni Collette, Lakeith Stanfield, Katherine Langford, Jaeden Martell, Christopher Plummer',
        run_time='2h 10min',
        rating=0,
        kids=False
    )

    zodiac.genres.append(Genre.query.get(7))
    the_hateful_8.genres.append(Genre.query.get(7))
    snowden.genres.append(Genre.query.get(7))
    the_da_vinci_code.genres.append(Genre.query.get(7))
    shutter_island.genres.append(Genre.query.get(7))
    triple_9.genres.append(Genre.query.get(7))
    the_machinist.genres.append(Genre.query.get(7))
    the_whole_truth.genres.append(Genre.query.get(7))
    The_bank_job.genres.append(Genre.query.get(7))
    knives_out.genres.append(Genre.query.get(7))

    db.session.add(zodiac)
    db.session.add(the_hateful_8)
    db.session.add(snowden)
    db.session.add(the_da_vinci_code)
    db.session.add(shutter_island)
    db.session.add(triple_9)
    db.session.add(the_machinist)
    db.session.add(the_whole_truth)
    db.session.add(The_bank_job)
    db.session.add(knives_out)


# ROMANCE ====================================================================================================================

    titanic = Movie(
        movie_url='https://notflix-clone-bucket.s3.us-west-1.amazonaws.com/romance/yt5s.com-Titanic+3D+Re-Release+Official+Trailer+%231+-+Leonardo+DiCaprio%2C+Kate+Winslet+Movie+(2012)+HD-(1080p).mp4',
        movie_thumbnail='https://notflix-clone-bucket.s3.us-west-1.amazonaws.com/Romance_THUMBNAILS/titanic.jpg',
        name='Titanic',
        description='A seventeen-year-old aristocrat falls in love with a kind but poor artist aboard the luxurious, ill-fated R.M.S. Titanic.',
        year_released=1997,
        production='Paramount Pictures, 20th Century Fox, Lightstorm Entertainment',
        maturity_rating='PG-13',
        director='James Cameron',
        cast='Leonardo DiCaprio, Kate Winslet, Billy Zane, Kathy Bates, Frances Fisher, Bernard Hill, Jonathan Hyde, Danny Nucci, David Warner, Bill Paxton',
        run_time='3h 14min',
        rating=0,
        kids=False
    )
    dear_john = Movie(
        movie_url='https://notflix-clone-bucket.s3.us-west-1.amazonaws.com/romance/yt5s.com-DEAR+JOHN+-+Official+Trailer+(HD)-(1080p).mp4',
        movie_thumbnail='https://notflix-clone-bucket.s3.us-west-1.amazonaws.com/Romance_THUMBNAILS/dear-john.jpg',
        name='Dear John',
        description='A romantic drama about a soldier who falls for a conservative college student while he\'s home on leave.',
        year_released=2010,
        production='Screen Gems, Relativity Media, Temple Hill Entertainment',
        maturity_rating='PG-13',
        director='Lasse Hallström',
        cast='Channing Tatum, Amanda Seyfried, Henry Thomas, Scott Porter, Richard Jenkins',
        run_time='1h 48min',
        rating=0,
        kids=False
    )
    five_feet_apart = Movie(
        movie_url='https://notflix-clone-bucket.s3.us-west-1.amazonaws.com/romance/yt5s.com-Five+Feet+Apart+Teaser+Trailer+%231+(2019)+_+Movieclips+Trailers-(1080p).mp4',
        movie_thumbnail='https://notflix-clone-bucket.s3.us-west-1.amazonaws.com/Romance_THUMBNAILS/Five-Feet-Apart-Riverdale-810x456.jpg',
        name='Five Feet Apart',
        description='A pair of teenagers with cystic fibrosis meet in a hospital and fall in love, though their disease means they must avoid close physical contact.',
        year_released=2019,
        production='CBS Films, Welle Entertainment, Wayfarer Entertainment',
        maturity_rating='PG-13',
        director='Justin Baldoni',
        cast='Haley Lu Richardson, Cole Sprouse, Moisés Arias',
        run_time='1h 56min',
        rating=0,
        kids=False
    )
    memoirs_of_a_geisha = Movie(
        movie_url='https://notflix-clone-bucket.s3.us-west-1.amazonaws.com/romance/yt5s.com-Memoirs+of+a+Geisha+(2005)+Official+Trailer+1+-+Ziyi+Zhang+Movie-(1080p).mp4',
        movie_thumbnail='https://notflix-clone-bucket.s3.us-west-1.amazonaws.com/Romance_THUMBNAILS/memoirs-of-a-geisha.jpg',
        name='Memoirs of a Geisha',
        description='Nitta Sayuri reveals how she transcended her fishing-village roots and became one of Japan\'s most celebrated geisha.',
        year_released=2005,
        production='Columbia Pictures, DreamWorks Pictures, Spyglass Entertainment, Amblin Entertainment, Red Wagon Entertainment',
        maturity_rating='PG-13',
        director='Rob Marshall',
        cast='Zhang Ziyi, Ken Watanabe, Michelle Yeoh, Kōji Yakusho, Youki Kudoh, Kaori Momoi, Gong Li',
        run_time='2h 25min',
        rating=0,
        kids=False
    )
    newness = Movie(
        movie_url='https://notflix-clone-bucket.s3.us-west-1.amazonaws.com/romance/yt5s.com-Newness+Trailer+%231+(2017)+_+Movieclips+Trailers-(1080p).mp4',
        movie_thumbnail='https://notflix-clone-bucket.s3.us-west-1.amazonaws.com/Romance_THUMBNAILS/Newness-2017-664x335.jpg',
        name='Newness',
        description='In contemporary Los Angeles, two millennials navigating a social media-driven hookup culture begin a relationship that pushes both emotional and physical boundaries.',
        year_released=2017,
        production='Scott Free Productions, Seville International, Lost City',
        maturity_rating='NR',
        director='Drake Doremus',
        cast='Nicholas Hoult, Laia Costa, Courtney Eaton, Danny Huston, Jessica Henwick, Esther Perel',
        run_time='1h 57min',
        rating=0,
        kids=False
    )
    the_duff = Movie(
        movie_url='https://notflix-clone-bucket.s3.us-west-1.amazonaws.com/romance/yt5s.com-The+DUFF+Official+Trailer+.mp4',
        movie_thumbnail='https://notflix-clone-bucket.s3.us-west-1.amazonaws.com/Romance_THUMBNAILS/the-duff.jpg',
        name='The DUFF',
        description='A high school senior instigates a social pecking order revolution after finding out that she has been labeled the DUFF - Designated Ugly Fat Friend - by her prettier, more popular counterparts.',
        year_released=2015,
        production='Vast Entertainment, CBS Films, Wonderland Sound and Vision',
        maturity_rating='PG-13',
        director='Ari Sandel',
        cast='Mae Whitman, Robbie Amell, Bella Thorne, Bianca Santos, Skyler Samuels, Romany Malco, Ken Jeong, Allison Janney',
        run_time='1h 41min',
        rating=0,
        kids=False
    )
    the_heartbreak_kid = Movie(
        movie_url='https://notflix-clone-bucket.s3.us-west-1.amazonaws.com/romance/yt5s.com-The+Heartbreak+Kid+-+Official%C2%AE+Trailer+%5BHD%5D-(1080p).mp4',
        movie_thumbnail='https://notflix-clone-bucket.s3.us-west-1.amazonaws.com/Romance_THUMBNAILS/the-heartbreak-kid.jpg',
        name='The Heartbreak Kid',
        description='A newly wed man who believes he\'s just gotten hitched to the perfect woman encounters another lady on his honeymoon.',
        year_released=2007,
        production='DreamWorks Pictures, Davis Entertainment Company, Conundrum Entertainment, Radar Pictures',
        maturity_rating='R',
        director='Peter Farrelly',
        cast='Ben Stiller, Michelle Monaghan, Malin Åkerman, Jerry Stiller, Rob Corddry, Carlos Mencia, Scott Wilson, Danny McBride',
        run_time='1h 56min',
        rating=0,
        kids=False
    )
    the_holiday = Movie(
        movie_url='https://notflix-clone-bucket.s3.us-west-1.amazonaws.com/romance/yt5s.com-The+Holiday+(2006)+Official+Trailer+1+-+Kate+Winslet+Movie-(1080p).mp4',
        movie_thumbnail='https://notflix-clone-bucket.s3.us-west-1.amazonaws.com/Romance_THUMBNAILS/the_holiday.jpg',
        name='The Holiday',
        description='Two women troubled with guy-problems swap homes in each other\'s countries, where they each meet a local guy and fall in love.',
        year_released=2006,
        production='Columbia Pictures, Universal Pictures, Relativity Media, Waverly Films',
        maturity_rating='PG-13',
        director='Nancy Meyers',
        cast='Cameron Diaz, Kate Winslet, Jude Law, Jack Black, Eli Wallach, Edward Burns, Rufus Sewell',
        run_time='2h 16min',
        rating=0,
        kids=False
    )
    the_shape_of_water = Movie(
        movie_url='https://notflix-clone-bucket.s3.us-west-1.amazonaws.com/romance/yt5s.com-THE+SHAPE+OF+WATER+_+Official+Trailer+_+FOX+Searchlight-(1080p).mp4',
        movie_thumbnail='https://notflix-clone-bucket.s3.us-west-1.amazonaws.com/Romance_THUMBNAILS/the-shape-of-water.jpg',
        name='The Shape of Water',
        description='At a top secret research facility in the 1960s, a lonely janitor forms a unique relationship with an amphibious creature that is being held in captivity.',
        year_released=2017,
        production='Fox Searchlight Pictures, TSG Entertainment, Double Dare You Productions',
        maturity_rating='R',
        director='Guillermo del Toro',
        cast='Sally Hawkins, Michael Shannon, Richard Jenkins, Doug Jones, Michael Stuhlbarg, Octavia Spencer',
        run_time='2h 3min',
        rating=0,
        kids=False
    )
    the_tourist = Movie(
        movie_url='https://notflix-clone-bucket.s3.us-west-1.amazonaws.com/romance/yt5s.com-The+Tourist+_+OFFICIAL+Trailer+.mp4',
        movie_thumbnail='https://notflix-clone-bucket.s3.us-west-1.amazonaws.com/Romance_THUMBNAILS/the-tourist.jpg',
        name='The Tourist',
        description='Revolves around Frank, an American tourist visiting Italy to mend a broken heart. Elise is an extraordinary woman who deliberately crosses his path.',
        year_released=2010,
        production='Columbia Pictures, GK Films, Spyglass Entertainment, StudioCanal',
        maturity_rating='PG-13',
        director='Florian Henckel von Donnersmarck',
        cast='Angelina Jolie, Johnny Depp, Paul Bettany, Timothy Dalton, Steven Berkoff, Rufus Sewell, Christian De Sica',
        run_time='1h 43min',
        rating=0,
        kids=False
    )

    titanic.genres.append(Genre.query.get(6))
    the_duff.genres.append(Genre.query.get(6))
    the_holiday.genres.append(Genre.query.get(6))
    five_feet_apart.genres.append(Genre.query.get(6))
    dear_john.genres.append(Genre.query.get(6))
    memoirs_of_a_geisha.genres.append(Genre.query.get(6))
    the_heartbreak_kid.genres.append(Genre.query.get(6))
    the_tourist.genres.append(Genre.query.get(6))
    the_shape_of_water.genres.append(Genre.query.get(6))
    newness.genres.append(Genre.query.get(6))

    db.session.add(titanic)
    db.session.add(the_duff)
    db.session.add(the_holiday)
    db.session.add(five_feet_apart)
    db.session.add(dear_john)
    db.session.add(memoirs_of_a_geisha)
    db.session.add(the_heartbreak_kid)
    db.session.add(the_tourist)
    db.session.add(the_shape_of_water)
    db.session.add(newness)


# COMEDY ====================================================================================================================

    school_of_rock = Movie(
        movie_url='https://notflix-clone-bucket.s3.us-west-1.amazonaws.com/comedy/yt5s.com-School+of+Rock+(2003)+Trailer+.mp4',
        movie_thumbnail='https://notflix-clone-bucket.s3.us-west-1.amazonaws.com/Comedy_THUMBNAILS/school_of_rock.jpg',
        name='School of Rock',
        description='After being kicked out of his rock band, Dewey Finn becomes a substitute teacher of an uptight elementary private school, only to try and turn his class into a rock band.',
        year_released=2003,
        production='Scott Rudin Productions',
        maturity_rating='PG-13',
        director='Richard Linklater',
        cast='Jack Black, Joan Cusack, Mike White, Sarah Silverman',
        run_time='1h 49min',
        rating=0,
        kids=False
    )
    good_burger = Movie(
        movie_url='https://notflix-clone-bucket.s3.us-west-1.amazonaws.com/comedy/yt5s.com-Good+Burger+(1997)+Official+Trailer+-+Kel+Mitchell%2C+Kenan+Thompson+Movie+HD.mp4',
        movie_thumbnail='https://notflix-clone-bucket.s3.us-west-1.amazonaws.com/Comedy_THUMBNAILS/good_burger.jpg',
        name='Good Burger',
        description='A dim-witted teenager and his new coworker try to save the old burger joint they work for from failing after the opening of a brand new burger restaurant across the street, which\'s planning to put them out of business.',
        year_released=1997,
        production='Nickelodeon Movies, Tollin/Robbins Productions',
        maturity_rating='PG',
        director='Brian Robbins',
        cast='Kenan Thompson, Kel Mitchell, Abe Vigoda',
        run_time='1h 35min',
        rating=0,
        kids=True
    )
    step_brothers = Movie(
        movie_url='https://notflix-clone-bucket.s3.us-west-1.amazonaws.com/comedy/yt5s.com-Step+Brothers+2008+Trailer+HD+_+Will+Ferrell+_+John+C.+Reilly.mp4',
        movie_thumbnail='https://notflix-clone-bucket.s3.us-west-1.amazonaws.com/Comedy_THUMBNAILS/step_brothers.jpg',
        name='Step Brothers',
        description='Two aimless middle-aged losers still living at home are forced against their will to become roommates when their parents marry.',
        year_released=2008,
        production='Columbia Pictures, Relativity Media, The Apatow Company, Mosaic Media Group, Gary Sanchez Productions',
        maturity_rating='R',
        director='Adam McKay',
        cast='Will Ferrell, John C. Reilly, Richard Jenkins, Mary Steenburgen, Adam Scott, Kathryn Hahn',
        run_time='1h 38min',
        rating=0,
        kids=False
    )
    bee_movie = Movie(
        movie_url='https://notflix-clone-bucket.s3.us-west-1.amazonaws.com/comedy/yt5s.com-Bee+Movie+-+Official+Trailer+2007+%5BHD%5D.mp4',
        movie_thumbnail='https://notflix-clone-bucket.s3.us-west-1.amazonaws.com/Comedy_THUMBNAILS/bee_movie.PNG',
        name='Bee Movie',
        description='Barry B. Benson, a bee just graduated from college, is disillusioned at his lone career choice: making honey. On a special trip outside the hive, Barry\'s life is saved by Vanessa, a florist in New York City. As their relationship blossoms, he discovers humans actually eat honey, and subsequently decides to sue them.',
        year_released=2007,
        production='DreamWorks Animation, Columbus 81 Productions',
        maturity_rating='PG',
        director='Simon J. Smith, Steve Hickner',
        cast='Jerry Seinfeld, Renée Zellweger, Matthew Broderick, John Goodman, Patrick Warburton, Chris Rock',
        run_time='1h 31min',
        rating=0,
        kids=True
    )
    war_dogs = Movie(
        movie_url='https://notflix-clone-bucket.s3.us-west-1.amazonaws.com/comedy/yt5s.com-War+Dogs+-+Official+Trailer+%5BHD%5D-(1080p).mp4',
        movie_thumbnail='https://notflix-clone-bucket.s3.us-west-1.amazonaws.com/Comedy_THUMBNAILS/war_dogs.jpg',
        name='War Dogs',
        description='Loosely based on the true story of two young men, David Packouz and Efraim Diveroli, who won a three hundred million dollar contract from the Pentagon to arm America\'s allies in Afghanistan.',
        year_released=2016,
        production='Joint Effort, RatPac-Dune Entertainment, The Mark Gordon Company',
        maturity_rating='R',
        director='Todd Phillips',
        cast='Jonah Hill, Miles Teller, Ana de Armas, Bradley Cooper',
        run_time='1h 54min',
        rating=0,
        kids=False
    )
    pinapple_express = Movie(
        movie_url='https://notflix-clone-bucket.s3.us-west-1.amazonaws.com/comedy/yt5s.com-Pineapple+Express+(2008)+Trailer+%231+_+Movieclips+Classic+Trailers-(1080p).mp4',
        movie_thumbnail='https://notflix-clone-bucket.s3.us-west-1.amazonaws.com/Comedy_THUMBNAILS/Pineapple-Express-Netflix-810x456.jpg',
        name='Pineapple Express',
        description='A process server and his marijuana dealer wind up on the run from hitmen and a corrupt police officer after he witnesses his dealer\'s boss murder a competitor while trying to serve papers on him.',
        year_released=2008,
        production='Columbia Pictures, Relativity Media, Apatow Productions',
        maturity_rating='R',
        director='David Gordon Green',
        cast='Seth Rogen, James Franco, Gary Cole, Rosie Perez, Danny McBride',
        run_time='1h 51min',
        rating=0,
        kids=False
    )
    scary_movie_4 = Movie(
        movie_url='https://notflix-clone-bucket.s3.us-west-1.amazonaws.com/comedy/yt5s.com-Scary+Movie+4+(1_10)+Movie+CLIP+-+Let+the+Game+Begin+(2006)+HD-(1080p).mp4',
        movie_thumbnail='https://notflix-clone-bucket.s3.us-west-1.amazonaws.com/Comedy_THUMBNAILS/scary_movie_4.jpg',
        name='Scary Movie 4',
        description='Cindy finds out the house she lives in is haunted by a little boy and goes on a quest to find out who killed him and why. Also, Alien "Tr-iPods" are invading the world and she has to uncover the secret in order to stop them.',
        year_released=2006,
        production='Brad Grey Pictures',
        maturity_rating='PG-13',
        director='David Zucker',
        cast='Anna Faris, Regina Hall, Craig Bierko, Bill Pullman, Anthony Anderson, Carmen Electra, Chris Elliott, Kevin Hart, Cloris Leachman, Michael Madsen, Phil McGraw, Leslie Nielsen, Shaquille O\'Neal, Molly Shannon',
        run_time='1h 23min',
        rating=0,
        kids=False
    )
    house_party = Movie(
        movie_url='https://notflix-clone-bucket.s3.us-west-1.amazonaws.com/comedy/yt5s.com-House+Party+(1990)+Trailer+.mp4',
        movie_thumbnail='https://notflix-clone-bucket.s3.us-west-1.amazonaws.com/Comedy_THUMBNAILS/house-party-featured1.jpg',
        name='House Party',
        description='Kid decides to go to his friend Play\'s house party, but neither of them can predict what\'s in store for them on what could be the wildest night of their lives.',
        year_released=1990,
        production='Warrington Hudlin',
        maturity_rating='R',
        director='Reginald Hudlin',
        cast='Reginald Hudlin',
        run_time='1h 40min',
        rating=0,
        kids=False
    )
    the_trip = Movie(
        movie_url='https://notflix-clone-bucket.s3.us-west-1.amazonaws.com/comedy/yt5s.com-The+Trip+_+Official+Trailer+_+Netflix-(1080p).mp4',
        movie_thumbnail='https://notflix-clone-bucket.s3.us-west-1.amazonaws.com/Comedy_THUMBNAILS/the_trip.jpg',
        name='The Trip',
        description='A dysfunctional couple head to a remote cabin to reconnect, but each has intentions to kill the other. Before they can carry out their plans, unexpected visitors arrive and they faced with a greater danger.',
        year_released=2021,
        production='Stine Hope',
        maturity_rating='TV-MA',
        director='Tommy Wirkola',
        cast='Noomi Rapace, Aksel Hennie, Atle Antonsen',
        run_time='1h 53min',
        rating=0,
        kids=False
    )
    stuart_little_2 = Movie(
        movie_url='https://notflix-clone-bucket.s3.us-west-1.amazonaws.com/comedy/yt5s.com-Stuart+Little+2+-+Trailer.mp4',
        movie_thumbnail='https://notflix-clone-bucket.s3.us-west-1.amazonaws.com/Comedy_THUMBNAILS/STUARt_little_2.jpg',
        name='Stuart Little 2',
        description='Stuart and Snowbell set out across town to rescue a friend.',
        year_released=2002,
        production='Columbia Pictures, Red Wagon Entertainment',
        maturity_rating='PG',
        director='Rob Minkoff',
        cast='Michael J. Fox, Melanie Griffith, Nathan Lane, Geena Davis, Hugh Laurie, Jonathan Lipnicki, James Woods, Steve Zahn',
        run_time='1h 17min',
        rating=0,
        kids=True
    )

    school_of_rock.genres.append(Genre.query.get(3))
    good_burger.genres.append(Genre.query.get(3))
    bee_movie.genres.append(Genre.query.get(3))
    step_brothers.genres.append(Genre.query.get(3))
    war_dogs.genres.append(Genre.query.get(3))
    pinapple_express.genres.append(Genre.query.get(3))
    scary_movie_4.genres.append(Genre.query.get(3))
    house_party.genres.append(Genre.query.get(3))
    the_trip.genres.append(Genre.query.get(3))
    stuart_little_2.genres.append(Genre.query.get(3))

    db.session.add(school_of_rock)
    db.session.add(good_burger)
    db.session.add(bee_movie)
    db.session.add(step_brothers)
    db.session.add(war_dogs)
    db.session.add(pinapple_express)
    db.session.add(scary_movie_4)
    db.session.add(house_party)
    db.session.add(the_trip)
    db.session.add(stuart_little_2)


# ACTION/ADVENTURE ====================================================================================================================

    jaws = Movie(
        movie_url='https://notflix-clone-bucket.s3.us-west-1.amazonaws.com/action_adventure/yt5s.com-Jaws+-+Theatrical+Trailer+(HD)+(1975).mp4',
        movie_thumbnail='https://notflix-clone-bucket.s3.us-west-1.amazonaws.com/Action_THUMBNAILS/JAWS.jpg',
        name='Jaws',
        description='When a killer shark unleashes chaos on beach community off Long Island, it\'s up to a local sheriff, a marine biologist, and an old seafarer to hunt the beast down.',
        year_released=1975,
        production='Zanuck/Brown Company, Universal Pictures',
        maturity_rating='PG',
        director='Steven Spielberg',
        cast='Roy Scheider, Robert Shaw, Richard Dreyfuss, Lorraine Gary, Murray Hamilton',
        run_time='2h 4min',
        rating=0,
        kids=False
    )
    john_wick = Movie(
        movie_url='https://notflix-clone-bucket.s3.us-west-1.amazonaws.com/action_adventure/yt5s.com-John+Wick+(2014)+-+Official+Trailer+-+Keanu+Reeves-(1080p).mp4',
        movie_thumbnail='https://notflix-clone-bucket.s3.us-west-1.amazonaws.com/Action_THUMBNAILS/john-wick-1.jpg',
        name='John Wick',
        description='An ex-hit-man comes out of retirement to track down the gangsters that killed his dog and took everything from him.',
        year_released=2014,
        production='Summit Entertainment, Thunder Road Pictures, 87Eleven Productions, MJW Films, DefyNite Films, Company Films',
        maturity_rating='R',
        director='Chad Stahelski',
        cast='Keanu Reeves, Michael Nyqvist, Alfie Allen, Adrianne Palicki, Bridget Moynahan, Dean Winters, Ian McShane, John Leguizamo, Willem Dafoe',
        run_time='1h 41min',
        rating=0,
        kids=False
    )
    green_latern = Movie(
        movie_url='https://notflix-clone-bucket.s3.us-west-1.amazonaws.com/action_adventure/yt5s.com-Green+Lantern+-+Trailer-(1080p).mp4',
        movie_thumbnail='https://notflix-clone-bucket.s3.us-west-1.amazonaws.com/Action_THUMBNAILS/green-lantern.jpg',
        name='Green Lantern',
        description='Reckless test pilot Hal Jordan is granted an alien ring that bestows him with otherworldly powers that inducts him into an intergalactic police force, the Green Lantern Corps.',
        year_released=2011,
        production='DC Entertainment, De Line Pictures',
        maturity_rating='PG-13',
        director='Martin Campbell',
        cast='Ryan Reynolds, Blake Lively, Peter Sarsgaard, Mark Strong, Angela Bassett, Tim Robbins',
        run_time='1h 54min',
        rating=0,
        kids=False
    )
    black_panther = Movie(
        movie_url='https://notflix-clone-bucket.s3.us-west-1.amazonaws.com/action_adventure/yt5s.com-Marvel+Studios\'+Black+Panther+-+Official+Trailer.mp4',
        movie_thumbnail='https://notflix-clone-bucket.s3.us-west-1.amazonaws.com/Action_THUMBNAILS/black-panther-movie-wallpaper.png',
        name='Black Panther',
        description='T\'Challa, heir to the hidden but advanced kingdom of Wakanda, must step forward to lead his people into a new future and must confront a challenger from his country\'s past.',
        year_released=2018,
        production='Marvel Studios',
        maturity_rating='PG-13',
        director='Ryan Coogler',
        cast='Chadwick Boseman, Michael B. Jordan, Lupita Nyong\'o, Danai Gurira, Martin Freeman, Daniel Kaluuya, Letitia Wright, Winston Duke, Angela Bassett, Forest Whitaker, Andy Serkis',
        run_time='2h 14min',
        rating=0,
        kids=False
    )
    avengers = Movie(
        movie_url='https://notflix-clone-bucket.s3.us-west-1.amazonaws.com/action_adventure/yt5s.com-Marvel+Studios\'+Avengers_+Endgame+-+Official+Trailer.mp4',
        movie_thumbnail='https://notflix-clone-bucket.s3.us-west-1.amazonaws.com/Action_THUMBNAILS/AvEngers-Endgame.png',
        name='Avengers: Endgame',
        description='After the devastating events of Avengers: Infinity War (2018), the universe is in ruins. With the help of remaining allies, the Avengers assemble once more in order to reverse Thanos\' actions and restore balance to the universe.',
        year_released=2019,
        production='Marvel Studios',
        maturity_rating='PG-13',
        director='Anthony Russo, Joe Russo',
        cast='Robert Downey Jr., Chris Evans, Mark Ruffalo, Chris Hemsworth, Scarlett Johansson, Jeremy Renner, Don Cheadle, Paul Rudd, Brie Larson, Karen Gillan, Danai Gurira, Benedict Wong, Jon Favreau, Bradley Cooper, Gwyneth Paltrow, Josh Brolin',
        run_time='3h 1min',
        rating=0,
        kids=False
    )
    mission_impossible = Movie(
        movie_url='https://notflix-clone-bucket.s3.us-west-1.amazonaws.com/action_adventure/yt5s.com-Mission_+Impossible+-+Fallout+(2018)+-+Official+Trailer+-+Paramount+Pictures.mp4',
        movie_thumbnail='https://notflix-clone-bucket.s3.us-west-1.amazonaws.com/Action_THUMBNAILS/mission-impossible-fallout-movie-review-1.jpg',
        name='Mission: Impossible - Fallout',
        description='Ethan Hunt and his IMF team, along with some familiar allies, race against time after a mission gone wrong.',
        year_released=2018,
        production='Skydance Media, Bad Robot Productions, TC Productions, Alibaba Pictures',
        maturity_rating='PG-13',
        director='Christopher McQuarrie',
        cast='Tom Cruise, Henry Cavill, Ving Rhames, Simon Pegg, Rebecca Ferguson, Sean Harris, Angela Bassett, Michelle Monaghan, Alec Baldwin',
        run_time='2h 27min',
        rating=0,
        kids=False
    )
    jason_bourne = Movie(
        movie_url='https://notflix-clone-bucket.s3.us-west-1.amazonaws.com/action_adventure/yt5s.com-Jason+Bourne+Official+Trailer+.mp4',
        movie_thumbnail='https://notflix-clone-bucket.s3.us-west-1.amazonaws.com/Action_THUMBNAILS/JASON-BOURNE.jpg',
        name='Jason Bourne',
        description='The CIA\'s most dangerous former operative is drawn out of hiding to uncover more explosive truths about his past.',
        year_released=2016,
        production='Perfect World Pictures, Kennedy/Marshall, Captivate Entertainment, Pearl Street',
        maturity_rating='PG-13',
        director='Paul Greengrass',
        cast='Matt Damon, Tommy Lee Jones, Alicia Vikander, Vincent Cassel, Julia Stiles, Riz Ahmed',
        run_time='2h 3min',
        rating=0,
        kids=False
    )
    waterworld = Movie(
        movie_url='https://notflix-clone-bucket.s3.us-west-1.amazonaws.com/action_adventure/yt5s.com-Waterworld+(1_10)+Movie+CLIP+-+Revenge+at+Sea+(1995)+HD-(480p).mp4',
        movie_thumbnail='https://notflix-clone-bucket.s3.us-west-1.amazonaws.com/Action_THUMBNAILS/WATER-WORLD.jpg',
        name='Waterworld',
        description='In a future where the polar ice-caps have melted and Earth is almost entirely submerged, a mutated mariner fights starvation and outlaw "smokers," and reluctantly helps a woman and a young girl try to find dry land.',
        year_released=1995,
        production='Gordon Company, Davis Entertainment, Licht/Mueller Film Corporation',
        maturity_rating='PG-13',
        director='Kevin Reynolds',
        cast='Kevin Costner, Dennis Hopper, Jeanne Tripplehorn, Tina Majorino, Michael Jeter',
        run_time='2h 15min',
        rating=0,
        kids=False
    )
    hancock = Movie(
        movie_url='https://notflix-clone-bucket.s3.us-west-1.amazonaws.com/action_adventure/yt5s.com-Hancock+(2008)+Trailer+.mp4',
        movie_thumbnail='https://notflix-clone-bucket.s3.us-west-1.amazonaws.com/Action_THUMBNAILS/HANCOCK.jpg',
        name='Hancock',
        description='Hancock is a superhero whose ill-considered behavior regularly causes damage in the millions. He changes when the person he saves helps him improve his public image.',
        year_released=2008,
        production='Columbia Pictures, Relativity Media, Overbrook Entertainment, Weed Road Pictures, Forward Pass, Blue Light',
        maturity_rating='PG-13',
        director='Peter Berg',
        cast='Will Smith, Charlize Theron, Jason Bateman',
        run_time='1h 32min',
        rating=0,
        kids=False
    )
    three_days_to_kill = Movie(
        movie_url='https://notflix-clone-bucket.s3.us-west-1.amazonaws.com/action_adventure/yt5s.com-3+Days+to+Kill+Official+Trailer+.mp4',
        movie_thumbnail='https://notflix-clone-bucket.s3.us-west-1.amazonaws.com/Action_THUMBNAILS/3-DAYS-to-kill.jpg',
        name='3 Days to Kill',
        description='A dying CIA agent trying to reconnect with his estranged daughter is offered an experimental drug that could save his life in exchange for one last assignment.',
        year_released=2014,
        production='EuropaCorp, Wonderland Sound and Vision',
        maturity_rating='PG-13',
        director='McG',
        cast='Kevin Costner, Amber Heard, Hailee Steinfeld, Connie Nielsen',
        run_time='1h 57min',
        rating=0,
        kids=False
    )


    jaws.genres.append(Genre.query.get(1))
    john_wick.genres.append(Genre.query.get(1))
    green_latern.genres.append(Genre.query.get(1))
    black_panther.genres.append(Genre.query.get(1))
    avengers.genres.append(Genre.query.get(1))
    mission_impossible.genres.append(Genre.query.get(1))
    jason_bourne.genres.append(Genre.query.get(1))
    waterworld.genres.append(Genre.query.get(1))
    hancock.genres.append(Genre.query.get(1))
    three_days_to_kill.genres.append(Genre.query.get(1))

    db.session.add(jaws)
    db.session.add(john_wick)
    db.session.add(green_latern)
    db.session.add(black_panther)
    db.session.add(avengers)
    db.session.add(mission_impossible)
    db.session.add(jason_bourne)
    db.session.add(waterworld)
    db.session.add(hancock)
    db.session.add(three_days_to_kill)

# ANIME ====================================================================================================================

    naruto = Movie(
        movie_url='https://notflix-clone-bucket.s3.us-west-1.amazonaws.com/anime/yt5s.com-The+Last+-+Naruto+the+Movie+-+Official+Trailer-(1080p).mp4',
        movie_thumbnail='https://notflix-clone-bucket.s3.us-west-1.amazonaws.com/Anime_THUMBNAILS/the_last_naruto_the_movie.jpg',
        name='The Last: Naruto the Movie',
        description='Hinata Hyuga\'s younger sister has been kidnapped, so Naruto must do what he can to save her.',
        year_released=2014,
        production='Studio Pierrot',
        maturity_rating='TV-14',
        director='Tsuneo Kobayashi',
        cast='Junko Takeuchi, Nana Mizuki, Chie Nakamura, Showtaro Morikubo, Satoshi Hino, Kazuhiko Inoue, Noriaki Sugiyama',
        run_time='1h 52min',
        rating=0,
        kids=False
    )
    no_game_no_life = Movie(
        movie_url='https://notflix-clone-bucket.s3.us-west-1.amazonaws.com/anime/yt5s.com-No+Game+No+Life_+Zero+-+Official+Trailer-(1080p).mp4',
        movie_thumbnail='https://notflix-clone-bucket.s3.us-west-1.amazonaws.com/Anime_THUMBNAILS/nogamenolifezero.jpg',
        name='No Game No Life: Zero',
        description='Adaption of the sixth Light Novel of series, it follows the story of two new characters - Riku and Shuvi - during the events of the Ancient War, prior to the 10 pledges.',
        year_released=2017,
        production='Madhouse',
        maturity_rating='TV-14',
        director='Atsuko Ishizuka',
        cast='Alexandra Bedford(English version), Jessica Boone(English version), Ricardo Contreras(English version)',
        run_time='1h 50min',
        rating=0,
        kids=False
    )
    princess_mononoke = Movie(
        movie_url='https://notflix-clone-bucket.s3.us-west-1.amazonaws.com/anime/yt5s.com-Princess+Mononoke+-+Official+Trailer.mp4',
        movie_thumbnail='https://notflix-clone-bucket.s3.us-west-1.amazonaws.com/Anime_THUMBNAILS/princess-mononoke-featured.jpg',
        name='Princess Mononoke',
        description='On a journey to find the cure for a Tatarigami\'s curse, Ashitaka finds himself in the middle of a war between the forest gods and Tatara, a mining colony. In this quest he also meets San, the Mononoke Hime.',
        year_released=1997,
        production='Studio Ghibli',
        maturity_rating='PG-13',
        director='Hayao Miyazaki',
        cast='Yōji Matsuda, Yuriko Ishida, Yūko Tanaka, Kaoru Kobayashi, Masahiko Nishimura, Tsunehiko Kamijo, Akira Nagoya, Akihiro Miwa, Mitsuko Mori, Hisaya Morishige',
        run_time='2h 14min',
        rating=0,
        kids=False
    )
    bleach = Movie(
        movie_url='https://notflix-clone-bucket.s3.us-west-1.amazonaws.com/anime/yt5s.com-Bleach+Movie+Trailer+_Memories+of+Nobody_-(480p).mp4',
        movie_thumbnail='https://notflix-clone-bucket.s3.us-west-1.amazonaws.com/Anime_THUMBNAILS/bleach-memories-of-nobody.png',
        name='Bleach: Memories of Nobody',
        description='In Karakura Town, unidentifiable spirits begin appearing en mases. While attempting to deal with these strange souls, Ichigo Kurosaki and Rukia Kuchiki meet Senna, a mysterious shinigami who wipes out most of them. Senna refuses to answer any questions, so Ichigo is forced to follow her while Rukia tries to find out what\'s going on.',
        year_released=2006,
        production='Pierrot',
        maturity_rating='TV-14',
        director='Noriyuki Abe',
        cast='Masakazu Morita, Fumiko Orikasa, Chiwa Saitō, Kentarō Itō, Romi Park, Ryōtarō Okiayu, Masashi Ebara',
        run_time='1h 27min',
        rating=0,
        kids=False
    )
    hxh = Movie(
        movie_url='https://notflix-clone-bucket.s3.us-west-1.amazonaws.com/anime/yt5s.com-Hunter+x+Hunter_+The+Last+Mission+-+Official+Theatrical+Trailer-(1080p).mp4',
        movie_thumbnail='https://notflix-clone-bucket.s3.us-west-1.amazonaws.com/Anime_THUMBNAILS/hxh-last-mission.jpg',
        name='Hunter x Hunter: The Last Mission',
        description='After a brutal attack from the "dark" side Hunters, Killua is injured and Kurapika is almost dead. What is the real goal behind the attack on all the Hunters?',
        year_released=2013,
        production='Madhouse',
        maturity_rating='TV-14',
        director='Keiichirô Kawaguchi',
        cast='Ichirō Nagai, Megumi Han, Mariya Ise, Shidou Nakamura',
        run_time='1h 37min',
        rating=0,
        kids=False
    )
    kizumonogatari = Movie(
        movie_url='https://notflix-clone-bucket.s3.us-west-1.amazonaws.com/anime/yt5s.com-KIZUMONOGATARI+PART+3_+REIKETSU+Trailer-(1080p).mp4',
        movie_thumbnail='https://notflix-clone-bucket.s3.us-west-1.amazonaws.com/Anime_THUMBNAILS/kizumonogatari-p3.jpg',
        name='Kizumonogatari Part 3: Reiketsu',
        description='Part 3 of Kizumonogatari (Wound Tale) trilogy, based on a light novel by Nisio Isin.',
        year_released=2017,
        production='Kodansha',
        maturity_rating='NR',
        director='Tatsuya Oishi, Akiyuki Shinbo',
        cast='Hiroshi Kamiya(voice), Takahiro Sakurai(voice), Maaya Sakamoto(voice)',
        run_time='1h 23min',
        rating=0,
        kids=False
    )
    only_yesterday = Movie(
        movie_url='https://notflix-clone-bucket.s3.us-west-1.amazonaws.com/anime/yt5s.com-Only+Yesterday+Official+US+Release+Trailer+.mp4',
        movie_thumbnail='https://notflix-clone-bucket.s3.us-west-1.amazonaws.com/Anime_THUMBNAILS/only-yesterday.jpg',
        name='Only Yesterday',
        description='A twenty-seven-year-old office worker travels to the countryside while reminiscing about her childhood in Tokyo.',
        year_released=1991,
        production='Studio Ghibli',
        maturity_rating='PG',
        director='Isao Takahata',
        cast='Miki Imai, Toshirō Yanagiba, Yōko Honna',
        run_time='1h 58min',
        rating=0,
        kids=False
    )
    gintama = Movie(
        movie_url='https://notflix-clone-bucket.s3.us-west-1.amazonaws.com/anime/yt5s.com-Gintama_+THE+FINAL+(2021)+-+Official+Trailer+2+_+English+Sub-(1080p).mp4',
        movie_thumbnail='https://notflix-clone-bucket.s3.us-west-1.amazonaws.com/Anime_THUMBNAILS/The-beyond-news-Gintama-+The+Final+Movie+2021-+release+date%2C+cast%2C+story%2C+teaser%2C+trailer%2C+first+look%2C+rating%2C+reviews%2C+box+office+collection+and+preview.jpg',
        name='Gintama: The Very Final',
        description='The concluding movie to the Gintama anime series.',
        year_released=2021,
        production='Bandai Namco Pictures',
        maturity_rating='NR',
        director='Chizuru Miyawaki',
        cast='Tomokazu Sugita, Daisuke Sakaguchi, Rie Kugimiya, Akira Ishida, Takehito Koyasu, Susumu Chiba, Kazuya Nakai, Kenichi Suzumura, Kōichi Yamadera',
        run_time='1h 44min',
        rating=0,
        kids=False
    )
    spirited_away = Movie(
        movie_url='https://notflix-clone-bucket.s3.us-west-1.amazonaws.com/anime/yt5s.com-Spirited+Away+-+Official+Trailer.mp4',
        movie_thumbnail='https://notflix-clone-bucket.s3.us-west-1.amazonaws.com/Anime_THUMBNAILS/spirited+away.png',
        name='Spirited Away',
        description='During her family\'s move to the suburbs, a sullen 10-year-old girl wanders into a world ruled by gods, witches, and spirits, and where humans are changed into beasts.',
        year_released=2001,
        production='Studio Ghibli',
        maturity_rating='PG',
        director='Hayao Miyazaki',
        cast='Rumi Hiiragi, Miyu Irino, Mari Natsuki, Takeshi Naito, Yasuko Sawaguchi, Tsunehiko Kamijō, Takehiko Ono, Bunta Sugawara',
        run_time='2h 5min',
        rating=0,
        kids=False
    )
    grave_of_the_fireflies = Movie(
        movie_url='https://notflix-clone-bucket.s3.us-west-1.amazonaws.com/anime/yt5s.com-Grave+of+the+Fireflies+-+Official+Trailer.mp4',
        movie_thumbnail='https://notflix-clone-bucket.s3.us-west-1.amazonaws.com/Anime_THUMBNAILS/grave-of-the-fireflies.jpg',
        name='Grave of the Fireflies',
        description='A young boy and his little sister struggle to survive in Japan during World War II.',
        year_released=1988,
        production='Studio Ghibli',
        maturity_rating='NR',
        director='Isao Takahata',
        cast='Tsutomu Tatsumi, Ayano Shiraishi, Yoshiko Shinohara, Akemi Yamaguchi',
        run_time='1h 29min',
        rating=0,
        kids=False
    )

    naruto.genres.append(Genre.query.get(2))
    no_game_no_life.genres.append(Genre.query.get(2))
    princess_mononoke.genres.append(Genre.query.get(2))
    bleach.genres.append(Genre.query.get(2))
    hxh.genres.append(Genre.query.get(2))
    kizumonogatari.genres.append(Genre.query.get(2))
    only_yesterday.genres.append(Genre.query.get(2))
    gintama.genres.append(Genre.query.get(2))
    spirited_away.genres.append(Genre.query.get(2))
    grave_of_the_fireflies.genres.append(Genre.query.get(2))

    db.session.add(naruto)
    db.session.add(no_game_no_life)
    db.session.add(princess_mononoke)
    db.session.add(bleach)
    db.session.add(hxh)
    db.session.add(kizumonogatari)
    db.session.add(only_yesterday)
    db.session.add(gintama)
    db.session.add(spirited_away)
    db.session.add(grave_of_the_fireflies)


# DOCUMENTARIES ====================================================================================================================

    what_the_health = Movie(
        movie_url='https://notflix-clone-bucket.s3.us-west-1.amazonaws.com/documentary/yt5s.com-WHAT+THE+HEALTH+Trailer-(1080p).mp4',
        movie_thumbnail='https://notflix-clone-bucket.s3.us-west-1.amazonaws.com/Documentary_THUMBNAILS/what-the-health.jpg',
        name='What the Health',
        description='An intrepid filmmaker on a journey of discovery as he uncovers possibly the largest health secret of our time and the collusion between industry, government, pharmaceutical and health organizations keeping this information from us.',
        year_released=2017,
        production='Kip Andersen, Keegan Kuhn',
        maturity_rating='NR',
        director='Kip Andersen, Keegan Kuhn',
        cast='Kip Andersen, Larry Baldwin, Neal Barnard',
        run_time='1h 37min',
        rating=0,
        kids=False
    )
    wont_you_be_my_neighbor = Movie(
        movie_url='https://notflix-clone-bucket.s3.us-west-1.amazonaws.com/documentary/yt5s.com-WON\'T+YOU+BE+MY+NEIGHBOR.mp4',
        movie_thumbnail='https://notflix-clone-bucket.s3.us-west-1.amazonaws.com/Documentary_THUMBNAILS/Fred-Rogers-in-Wont-You-Be-My-Neighbor-Courtesy-of-Focus-Films.jpg',
        name='Won\'t You Be My Neighbor?',
        description='An exploration of the life, lessons, and legacy of iconic children\'s television host Fred Rogers.',
        year_released=2018,
        production='Tremolo Productions, Impact Partners, Independent Lens',
        maturity_rating='PG-13',
        director='Morgan Neville',
        cast='Fred Rogers, François Clemmons, Yo-Yo Ma, Joe Negri, David Newell, Tom Junod, Joanne Rogers',
        run_time='1h 35min',
        rating=0,
        kids=False
    )
    andre_and_his_olive_tree = Movie(
        movie_url='https://notflix-clone-bucket.s3.us-west-1.amazonaws.com/documentary/yt5s.com-Andr%C3%A9+.mp4',
        movie_thumbnail='https://notflix-clone-bucket.s3.us-west-1.amazonaws.com/Documentary_THUMBNAILS/andre-and-his-olive-tree.jpg',
        name='André & His Olive Tree',
        description='André and His Olive Tree follows Chef André as he prepares to close his beloved Restaurant André on Valentine\'s Day of 2018, and return those coveted Michelin stars. This of course creates a shock to the industry, his staff, and his loved ones.',
        year_released=2020,
        production='Josiah Ng',
        maturity_rating='NR',
        director='Josiah Ng',
        cast='Andre Chiang',
        run_time='1h 44min',
        rating=0,
        kids=False
    )
    abducted_in_plain_sight = Movie(
        movie_url='https://notflix-clone-bucket.s3.us-west-1.amazonaws.com/documentary/yt5s.com-ABDUCTED+IN+PLAIN+SIGHT+TRAILER-(1080p).mp4',
        movie_thumbnail='https://notflix-clone-bucket.s3.us-west-1.amazonaws.com/Documentary_THUMBNAILS/abducted-in-plain-sight-netflix.jpg',
        name='Abducted in Plain Sight',
        description='The twisting, turning, stranger-than-fiction true story of the Brobergs, a naive, church-going Idaho family that fell under the spell of a sociopathic neighbor with designs on their twelve-year-old daughter.',
        year_released=2017,
        production='Top Knot Films',
        maturity_rating='TV-14',
        director='Skye Borgman',
        cast='Jan BrobergBob, BrobergMary, Ann Broberg',
        run_time='1h 31min',
        rating=0,
        kids=False
    )
    last_breath = Movie(
        movie_url='https://notflix-clone-bucket.s3.us-west-1.amazonaws.com/documentary/yt5s.com-Last+Breath+-+Official+UK+Trailer-(1080p).mp4',
        movie_thumbnail='https://notflix-clone-bucket.s3.us-west-1.amazonaws.com/Documentary_THUMBNAILS/last-breath-1.jpg',
        name='Last Breath',
        description='A deep sea diver is stranded on the seabed with 5 minutes of oxygen and no hope of rescue. With access to amazing archive this is the story of one man\'s impossible fight for survival.',
        year_released=2019,
        production='Richard da Costa, Dylan Williams, Alex Parkinson, Al Morrow, Stewart Le Marechal, Angus Lamont',
        maturity_rating='TV-MA',
        director='Richard da Costa, Alex Parkinson',
        cast='Duncan Allcock, Duncan Allcock, Kjetil Ove Alvestad',
        run_time='1h 30min',
        rating=0,
        kids=False
    )
    american_murder = Movie(
        movie_url='https://notflix-clone-bucket.s3.us-west-1.amazonaws.com/documentary/yt5s.com-American+Murder_+The+Family+Next+Door+Official+Trailer+(2020)+%2C+Documentary+Movies+Series.mp4',
        movie_thumbnail='https://notflix-clone-bucket.s3.us-west-1.amazonaws.com/Documentary_THUMBNAILS/american-murder.jpg',
        name='American Murder: The Family Next Door',
        description='In 2018, 34-year-old Shanann Watts and her two young daughters disappear in Colorado. With the heartbreaking details emerging, the family\'s story made headlines around the world.',
        year_released=2020,
        production='Knickerbockerglory',
        maturity_rating='TV-MA',
        director='Jenny Popplewell',
        cast='Nickole Atkinson(archive footage), Jim Benemann(archive footage), Luke Epple(archive sound)',
        run_time='1h 23min',
        rating=0,
        kids=False
    )
    rhyme_and_reason = Movie(
        movie_url='https://notflix-clone-bucket.s3.us-west-1.amazonaws.com/documentary/yt5s.com-Rhyme+.mp4',
        movie_thumbnail='https://notflix-clone-bucket.s3.us-west-1.amazonaws.com/Documentary_THUMBNAILS/rhyme-and-reason.jpg',
        name='Rhyme & Reason',
        description='A study in the world of hip-hop, done mostly with interviews, in order to see why it is as popular as it is today and what the future holds.',
        year_released=1997,
        production='Daniel Sollinger',
        maturity_rating='R',
        director='Peter Spirer',
        cast='B-Real, Kurtis Blow, Da Brat',
        run_time='1h 30min',
        rating=0,
        kids=False
    )
    a_kid_from_coney_island = Movie(
        movie_url='https://notflix-clone-bucket.s3.us-west-1.amazonaws.com/documentary/yt5s.com-A+Kid+From+Coney+Island+(2020)+_+Official+Trailer+HD.mp4',
        movie_thumbnail='https://notflix-clone-bucket.s3.us-west-1.amazonaws.com/Documentary_THUMBNAILS/a-kid-from-coney-island.jpg',
        name='A Kid from Coney Island',
        description='Feature documentary about the rise and fall, and rebirth of ex-NBA star, Stephon Marbury.',
        year_released=2019,
        production='Nina Yang Bongiovi',
        maturity_rating='TV-MA',
        director='Coodie, Chike Ozah',
        cast='Stephon Marbury, Ronald Stewart',
        run_time='1h 35min',
        rating=0,
        kids=False
    )
    demon_house = Movie(
        movie_url='https://notflix-clone-bucket.s3.us-west-1.amazonaws.com/documentary/yt5s.com-Demon+House+Official+Trailer+.mp4',
        movie_thumbnail='https://notflix-clone-bucket.s3.us-west-1.amazonaws.com/Documentary_THUMBNAILS/demon-house.jpg',
        name='Demon House',
        description='Paranormal investigator Zak Bagans documents the most authenticated case of possession in American history.',
        year_released=2019,
        production='Zak Bagans',
        maturity_rating='TV-14',
        director='Zak Bagans',
        cast='Zak Bagans, Adam Ahlbrandt, Matthew Mourgides',
        run_time='1h 35min',
        rating=0,
        kids=False
    )
    life_itself = Movie(
        movie_url='https://notflix-clone-bucket.s3.us-west-1.amazonaws.com/documentary/yt5s.com-Life+Itself+-+Official+Trailer.mp4',
        movie_thumbnail='https://notflix-clone-bucket.s3.us-west-1.amazonaws.com/Documentary_THUMBNAILS/Roger-Ebert-Documentary-Life-Itself-Goes-To-Magnolia.jpg',
        name='Life Itself',
        description='The life and career of the renowned film critic and social commentator, Roger Ebert.',
        year_released=2014,
        production='Garrett Basch, Zak Piper, Steve James',
        maturity_rating='R',
        director='Steve James',
        cast='Roger Ebert, Chaz Ebert, Gene Siskel(archive footage)',
        run_time='2h 1min',
        rating=0,
        kids=False
    )

    what_the_health.genres.append(Genre.query.get(4))
    wont_you_be_my_neighbor.genres.append(Genre.query.get(4))
    andre_and_his_olive_tree.genres.append(Genre.query.get(4))
    abducted_in_plain_sight.genres.append(Genre.query.get(4))
    last_breath.genres.append(Genre.query.get(4))
    american_murder.genres.append(Genre.query.get(4))
    rhyme_and_reason.genres.append(Genre.query.get(4))
    a_kid_from_coney_island.genres.append(Genre.query.get(4))
    demon_house.genres.append(Genre.query.get(4))
    life_itself.genres.append(Genre.query.get(4))

    db.session.add(what_the_health)
    db.session.add(wont_you_be_my_neighbor)
    db.session.add(andre_and_his_olive_tree)
    db.session.add(abducted_in_plain_sight)
    db.session.add(last_breath)
    db.session.add(american_murder)
    db.session.add(rhyme_and_reason)
    db.session.add(a_kid_from_coney_island)
    db.session.add(demon_house)
    db.session.add(life_itself)


    the_trip.genres.append(Genre.query.get(8))
    quarantine.genres.append(Genre.query.get(8))
    the_heartbreak_kid.genres.append(Genre.query.get(8))
    The_bank_job.genres.append(Genre.query.get(8))
    shutter_island.genres.append(Genre.query.get(8))
    three_days_to_kill.genres.append(Genre.query.get(8))
    life_itself.genres.append(Genre.query.get(8))
    war_dogs.genres.append(Genre.query.get(8))
    avengers.genres.append(Genre.query.get(8))
    rings.genres.append(Genre.query.get(8))


    db.session.commit()



# Uses a raw SQL query to TRUNCATE the users table.
# SQLAlchemy doesn't have a built in function to do this
# TRUNCATE Removes all the data from the table, and RESET IDENTITY
# resets the auto incrementing primary key, CASCADE deletes any
# dependent entities
def undo_movies():
    db.session.execute('TRUNCATE movies RESTART IDENTITY CASCADE;')
    db.session.commit()
