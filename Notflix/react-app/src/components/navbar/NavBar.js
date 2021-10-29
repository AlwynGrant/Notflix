import React from 'react';
import { NavLink } from 'react-router-dom';

import './navbar-styles/navbar_home.css'

import notflix_text_1000 from './images/notflix_text_1000.png'

const NavBar = () => {

  return (
    <nav className='navbar-home'>
      <div className='navbar-home-container'>
          <img className='home-logo' src={notflix_text_1000} alt='logo-here'/>
          <NavLink className='home-login-link' to='/login' exact={true} activeClassName='active'>
            Log In
          </NavLink>
      </div>
    </nav>
  );
}

export default NavBar;
