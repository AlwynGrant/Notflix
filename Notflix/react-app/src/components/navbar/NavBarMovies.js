import React from 'react';
import { useParams } from 'react-router-dom';
import { useSelector } from 'react-redux';
import LogoutButton from '../auth/LogoutButton';
import './navbar-styles/navbar_movies.css'

import notflix_text_1000 from './images/notflix_text_1000.png'

const NavBarMovies = () => {
    const { profile_id } = useParams();

    return (
        <nav className='navbar-movies'>
            <div className='navbar-movies-container'>
                <a className='movies-logo' href={`/profiles/${profile_id}/movies`}>
                    <img className='movies-logo' src={notflix_text_1000} />
                </a>
                GENRE_GENRE_GENRE_GENRE_GENRE
                <a href={`/profiles/${profile_id}/my-list`}>My list</a>
                <LogoutButton />
            </div>
        </nav>
    );
}

export default NavBarMovies;
