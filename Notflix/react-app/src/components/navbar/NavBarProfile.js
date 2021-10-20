import React from 'react';
import { NavLink } from 'react-router-dom';
import './navbar-styles/navbar_profile.css'

const NavBarProfile = () => {
    return (
        <nav className='navbar-prof'>
            <div className='navbar-prof-container'>
                <NavLink className='navbar-prof-logo' to='/'>
                    NOTFLIX_LOGO
                </NavLink>
            </div>
        </nav>
    );
}

export default NavBarProfile;
