import React from 'react';
import { NavLink, useParams } from 'react-router-dom';
import { useSelector } from 'react-redux';
import LogoutButton from '../auth/LogoutButton';
import './navbar-styles/navbar_movies.css'

const NavBarMovies = () => {
    const { profile_id } = useParams();
    const accountHolder = useSelector(state => state.session.user);

    return (
        <nav className='navbar-movies'>
            <div className='navbar-movies-container'>
                <div className='movies-logo'>
                    NOTFLIX_LOGO
                </div>
                <a href={`/profiles/${profile_id}/my-list`}>My list</a>
                <LogoutButton />
            </div>
        </nav>
    );
}

export default NavBarMovies;
