
import React from 'react';
import { NavLink } from 'react-router-dom';
import { useSelector } from 'react-redux';
import LogoutButton from '../auth/LogoutButton';
import './navbar-styles/navbar_home.css'

const NavBar = () => {
  const accountHolder = useSelector(state => state.session.user);

  return (
    <nav className='navbar-home'>
      <div className='navbar-home-container'>
          <div className='home-logo'>
            NOTFLIX_LOGO
          </div>
          <LogoutButton />
          <NavLink className='home-login-link' to='/login' exact={true} activeClassName='active'>
            Login
          </NavLink>
      </div>
    </nav>
  );
}

export default NavBar;
