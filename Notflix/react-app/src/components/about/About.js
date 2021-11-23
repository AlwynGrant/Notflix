import React, { useEffect } from 'react';

import './about.css'

function AboutPage() {

    return (
        <div className='about-container'>
            <div className='about-form'>
                <div className='about-question'>
                    About Notflix
                </div>
                <br />
                <div className='about-answer'>Notflix is a direct clone of Netflix, a media streaming platform that houses movies from various genres such as action & adventure, eastern/western animation, comedy, documentaries, horror, romance, thrillers, dramas, as well as a sub-series of genres for a younger audience.</div>
                <br />
                <br />
                <div className='about-answer'>This app was built using React & Redux on the frontend, Flask & SQLAlchemy on the backend, and maintained with Docker and Heroku. For more information on the app or my developing history as well as other projects, see my <a target="_blank" rel="noreferrer" href='https://github.com/AlwynGrant/Notflix'>Github</a>, and <a target="_blank" rel="noreferrer" href='https://www.linkedin.com/in/alwyn-grant-928b091a3/'>LinkedIn</a></div>
            </div>
        </div>
    );
}
export default AboutPage;
