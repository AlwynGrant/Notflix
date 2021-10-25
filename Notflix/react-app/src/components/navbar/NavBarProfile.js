import React from 'react';
import { NavLink } from 'react-router-dom';
import './navbar-styles/navbar_profile.css';

import notflix_text_1000 from './images/notflix_text_1000.png'

const NavBarProfile = () => {
    return (
        <nav className='navbar-prof'>
            <div className='navbar-prof-container'>
                <NavLink className='navbar-prof-logo' to='/'>
                    <img className='navbar-prof-logo' src={notflix_text_1000}/>
                </NavLink>
            </div>
        </nav>
    );
}

export default NavBarProfile;
