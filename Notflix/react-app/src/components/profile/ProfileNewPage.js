import React, { useState, useEffect } from 'react';
import { useHistory } from 'react-router-dom';
import { useSelector, useDispatch } from 'react-redux';
import { createProfile } from '../../store/profile'

import './profile-styles/profile_new.css'

function ProfileNewPage() {
    const history = useHistory();
    const dispatch = useDispatch();
    const accountHolder = useSelector(state => state.session.user);

    useEffect(() => {

    }, [])

    return (
        <div className='profile-new-container'>
            <div className='profile-new-form'>
                <div className='profile-new-text'>
                    Add Profile
                </div>
                <div className='profile-new-sub-text'>
                    Add a profile for another person watching Notflix.
                </div>
                <div className='profile-new-form-inputs'>
                    <div className='profile-new-img-div'>IMG_HERE</div>
                    <div className='profile-new-input-container'>
                        <input
                            className='profile-new-name-input'
                            placeholder='Name'
                            type='text'
                        />
                        <input
                            type='checkbox'
                            className='profile-new-name-checkbox'
                            defaultChecked={false}
                        />
                        <p className='profile-new-checkbox-name'>Kid?</p>
                    </div>
                </div>
                <div className='profile-new-btn-div'>
                    <button className='profile-new-continue'>Continue</button>
                    <button className='profile-new-cancel'>Cancel</button>
                </div>
            </div>
        </div>
    );
}
export default ProfileNewPage;
