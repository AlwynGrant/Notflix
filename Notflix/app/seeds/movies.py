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
        movie_thumbnail='https://notflix-clone-bucket.s3.us-west-1.amazonaws.com/Thrillers_THUMBNAILS/Knives-Out-Film-Poster-1.jpg',
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

    movie = Movie(
        movie_url=None,
        movie_thumbnail=None,
        name=None,
        description=None,
        year_released=None,
        production=None,
        maturity_rating=None,
        director=None,
        cast=None,
        run_time=None,
        rating=0,
        kids=False
    )
    movie = Movie(
        movie_url=None,
        movie_thumbnail=None,
        name=None,
        description=None,
        year_released=None,
        production=None,
        maturity_rating=None,
        director=None,
        cast=None,
        run_time=None,
        rating=0,
        kids=False
    )
    movie = Movie(
        movie_url=None,
        movie_thumbnail=None,
        name=None,
        description=None,
        year_released=None,
        production=None,
        maturity_rating=None,
        director=None,
        cast=None,
        run_time=None,
        rating=0,
        kids=False
    )
    movie = Movie(
        movie_url=None,
        movie_thumbnail=None,
        name=None,
        description=None,
        year_released=None,
        production=None,
        maturity_rating=None,
        director=None,
        cast=None,
        run_time=None,
        rating=0,
        kids=False
    )
    movie = Movie(
        movie_url=None,
        movie_thumbnail=None,
        name=None,
        description=None,
        year_released=None,
        production=None,
        maturity_rating=None,
        director=None,
        cast=None,
        run_time=None,
        rating=0,
        kids=False
    )
    movie = Movie(
        movie_url=None,
        movie_thumbnail=None,
        name=None,
        description=None,
        year_released=None,
        production=None,
        maturity_rating=None,
        director=None,
        cast=None,
        run_time=None,
        rating=0,
        kids=False
    )
    movie = Movie(
        movie_url=None,
        movie_thumbnail=None,
        name=None,
        description=None,
        year_released=None,
        production=None,
        maturity_rating=None,
        director=None,
        cast=None,
        run_time=None,
        rating=0,
        kids=False
    )
    movie = Movie(
        movie_url=None,
        movie_thumbnail=None,
        name=None,
        description=None,
        year_released=None,
        production=None,
        maturity_rating=None,
        director=None,
        cast=None,
        run_time=None,
        rating=0,
        kids=False
    )
    movie = Movie(
        movie_url=None,
        movie_thumbnail=None,
        name=None,
        description=None,
        year_released=None,
        production=None,
        maturity_rating=None,
        director=None,
        cast=None,
        run_time=None,
        rating=0,
        kids=False
    )
    movie = Movie(
        movie_url=None,
        movie_thumbnail=None,
        name=None,
        description=None,
        year_released=None,
        production=None,
        maturity_rating=None,
        director=None,
        cast=None,
        run_time=None,
        rating=0,
        kids=False
    )


# ACTION/ADVENTURE ====================================================================================================================

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
        rating=0,
        kids=False
    )

# ANIME ====================================================================================================================

    movie = Movie(
        movie_url=None,
        movie_thumbnail=None,
        name=None,
        description=None,
        year_released=None,
        production=None,
        maturity_rating=None,
        director=None,
        cast=None,
        run_time=None,
        rating=0,
        kids=False
    )


# DOCUMENTARIES ====================================================================================================================

    movie = Movie(
        movie_url=None,
        movie_thumbnail=None,
        name=None,
        description=None,
        year_released=None,
        production=None,
        maturity_rating=None,
        director=None,
        cast=None,
        run_time=None,
        rating=0,
        kids=False
    )
    movie = Movie(
        movie_url=None,
        movie_thumbnail=None,
        name=None,
        description=None,
        year_released=None,
        production=None,
        maturity_rating=None,
        director=None,
        cast=None,
        run_time=None,
        rating=0,
        kids=False
    )
    movie = Movie(
        movie_url=None,
        movie_thumbnail=None,
        name=None,
        description=None,
        year_released=None,
        production=None,
        maturity_rating=None,
        director=None,
        cast=None,
        run_time=None,
        rating=0,
        kids=False
    )
    movie = Movie(
        movie_url=None,
        movie_thumbnail=None,
        name=None,
        description=None,
        year_released=None,
        production=None,
        maturity_rating=None,
        director=None,
        cast=None,
        run_time=None,
        rating=0,
        kids=False
    )
    movie = Movie(
        movie_url=None,
        movie_thumbnail=None,
        name=None,
        description=None,
        year_released=None,
        production=None,
        maturity_rating=None,
        director=None,
        cast=None,
        run_time=None,
        rating=0,
        kids=False
    )
    movie = Movie(
        movie_url=None,
        movie_thumbnail=None,
        name=None,
        description=None,
        year_released=None,
        production=None,
        maturity_rating=None,
        director=None,
        cast=None,
        run_time=None,
        rating=0,
        kids=False
    )
    movie = Movie(
        movie_url=None,
        movie_thumbnail=None,
        name=None,
        description=None,
        year_released=None,
        production=None,
        maturity_rating=None,
        director=None,
        cast=None,
        run_time=None,
        rating=0,
        kids=False
    )
    movie = Movie(
        movie_url=None,
        movie_thumbnail=None,
        name=None,
        description=None,
        year_released=None,
        production=None,
        maturity_rating=None,
        director=None,
        cast=None,
        run_time=None,
        rating=0,
        kids=False
    )
    movie = Movie(
        movie_url=None,
        movie_thumbnail=None,
        name=None,
        description=None,
        year_released=None,
        production=None,
        maturity_rating=None,
        director=None,
        cast=None,
        run_time=None,
        rating=0,
        kids=False
    )
    movie = Movie(
        movie_url=None,
        movie_thumbnail=None,
        name=None,
        description=None,
        year_released=None,
        production=None,
        maturity_rating=None,
        director=None,
        cast=None,
        run_time=None,
        rating=0,
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
