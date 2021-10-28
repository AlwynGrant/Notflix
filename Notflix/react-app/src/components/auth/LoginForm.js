import React, { useState } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { Redirect } from 'react-router-dom';
import { login } from '../../store/session';
import './auth-styles/login.css'

const LoginForm = () => {
  const [errors, setErrors] = useState([]);
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const user = useSelector(state => state.session.user);
  const dispatch = useDispatch();

  const onLogin = async (e) => {
    e.preventDefault();
    const data = await dispatch(login(email, password));
    if (data) {
      setErrors(data);
    }
  };

  const handleSubmitDEMO = async (e) => {
    e.preventDefault();
    dispatch(login('demo@aa.com', 'password'));
  }

  const updateEmail = (e) => {
    setEmail(e.target.value);
  };

  const updatePassword = (e) => {
    setPassword(e.target.value);
  };

  if (user) {
    return <Redirect to='/profiles' />;
  }

  return (
    <div className='login-container'>
      <form className='login-form' onSubmit={onLogin}>
        <div className='login-text'>Log in</div>
        <div className='login-errors-container'>
          {errors.map((error, ind) => (
            <div className='login-errors' key={ind}>{error}</div>
          ))}
        </div>
        <div className='login-email-div'>
          <input
            className='login-email-input'
            name='Email'
            type='text'
            placeholder='Email'
            value={email}
            onChange={updateEmail}
          />
        </div>
        <div className='login-password-div'>
          <input
            className='login-password-input'
            name='Password'
            type='password'
            placeholder='Password'
            value={password}
            onChange={updatePassword}
          />
        </div>
        <div className='login-btn-div'>
          <button className='login-btn' type='submit'>Login</button>
          <button className='login-btn' onClick={(e) => handleSubmitDEMO(e)}>Demo</button>
          <div className='login-to-signup'>New to Notflix? <a href='/signup'>Sign up</a></div>
        </div>
      </form>
    </div>
  );
};

export default LoginForm;
