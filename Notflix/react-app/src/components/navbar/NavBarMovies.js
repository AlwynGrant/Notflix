import React from 'react';
import { useParams, Link } from 'react-router-dom';
import { useSelector } from 'react-redux';
import LogoutButton from '../auth/LogoutButton';
import './navbar-styles/navbar_movies.css'

import notflix_text_1000 from './images/notflix_text_1000.png'

const NavBarMovies = () => {
    const { profile_id } = useParams();

    return (
        <nav className='navbar-movies'>
            <div className='navbar-movies-container'>
                <div className='navbar-movies-link-container'>
                    <a className='movies-logo' href={`/profiles/${profile_id}/movies`}>
                        <img className='movies-logo' src={notflix_text_1000} />
                    </a>

                    <a target="_blank" rel="noreferrer" href={'https://github.com/AlwynGrant/Notflix'}>Github</a>
                    <a target="_blank" rel="noreferrer" href={'https://www.linkedin.com/in/alwyn-grant-928b091a3/'}>LinkdIn</a>
                    <a href={`/profiles/${profile_id}/my-list`}>My list</a>
                </div>
                <div>
                    <LogoutButton />
                </div>
            </div>
        </nav>
    );
}

export default NavBarMovies;
