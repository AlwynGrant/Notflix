import React from 'react';
import { NavLink } from 'react-router-dom';
import './navbar-styles/navbar_auth.css'

const NavBarAuth = () => {
    return (
        <nav className='navbar-auth'>
            <div className='navbar-auth-container'>
                <NavLink className='auth-logo' to='/'>
                    NOTFLIX
                </NavLink>
            </div>
        </nav>
    );
}

export default NavBarAuth;
