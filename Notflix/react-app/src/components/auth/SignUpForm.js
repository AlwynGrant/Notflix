import React, { useState } from 'react';
import { useSelector, useDispatch } from 'react-redux'
import { Redirect } from 'react-router-dom';
import { signUp } from '../../store/session';

import './auth-styles/signup.css'

const SignUpForm = () => {
  const [errors, setErrors] = useState([]);
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [repeatPassword, setRepeatPassword] = useState('');
  const user = useSelector(state => state.session.user);
  const dispatch = useDispatch();

  const onSignUp = async (e) => {
    e.preventDefault();
    if (password === repeatPassword) {
      const data = await dispatch(signUp(email, password));
      if (data) {
        setErrors(data)
      }
    }
    else {
      setErrors(['Both password fields must match.'])
    }
  };
  const updateEmail = (e) => {
    setEmail(e.target.value);
  };

  const updatePassword = (e) => {
    setPassword(e.target.value);
  };

  const updateRepeatPassword = (e) => {
    setRepeatPassword(e.target.value);
  };

  if (user) {
    return <Redirect to='/profiles' />;
  }

  return (
    <div className='signup-container'>
      <form className='signup-form' onSubmit={onSignUp}>
        <div className='signup-text'>Sign up</div>
        <div className='signup-errors-container'>
          {errors.map((error, ind) => (
            <div className='signup-errors' key={ind}>{error}</div>
          ))}
        </div>

        <div className='signup-email-div'>
          <input
            className='signup-email-input'
            type='text'
            name='email'
            placeholder='Email'
            onChange={updateEmail}
            value={email}
          ></input>
        </div>
        <div className='signup-password-div'>
          <input
            className='signup-password-input'
            type='password'
            name='password'
            placeholder='Password'
            onChange={updatePassword}
            value={password}
          ></input>
        </div>
        <div className='signup-repeat-password-div'>
          <input
            className='signup-repeat-password-input'
            type='password'
            name='repeat_password'
            placeholder='Confirm password'
            onChange={updateRepeatPassword}
            value={repeatPassword}
            required={true}
          ></input>
        </div>
        <div className='signup-btn-div'>
          <button className='signup-btn' type='submit'>Sign up</button>
          <div className='signup-to-login'>Already have an account? <a href='/login'>Login</a></div>
        </div>
      </form>
    </div>
  );
};

export default SignUpForm;
