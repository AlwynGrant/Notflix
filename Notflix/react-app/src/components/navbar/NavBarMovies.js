import React from 'react';
import { NavLink } from 'react-router-dom';
import { useSelector } from 'react-redux';
import LogoutButton from '../auth/LogoutButton';
import './navbar-styles/navbar_movies.css'

const NavBarMovies = () => {
    const accountHolder = useSelector(state => state.session.user);

    return (
        <nav className='navbar-movies'>
            <div className='navbar-movies-container'>
                <div className='movies-logo'>
                    NOTFLIX_LOGO
                </div>
                <LogoutButton />
            </div>
        </nav>
    );
}

export default NavBarMovies;
