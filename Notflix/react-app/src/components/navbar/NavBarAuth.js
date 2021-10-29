import React from 'react';
import { NavLink } from 'react-router-dom';

import './navbar-styles/navbar_auth.css'

import notflix_text_1000 from './images/notflix_text_1000.png'

const NavBarAuth = () => {
    return (
        <nav className='navbar-auth'>
            <div className='navbar-auth-container'>
                <NavLink className='auth-logo' to='/'>
                    <img className='auth-logo' src={notflix_text_1000} alt='logo-here'/>
                </NavLink>
            </div>
        </nav>
    );
}

export default NavBarAuth;
