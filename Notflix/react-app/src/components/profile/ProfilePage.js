import React, { useState, useEffect } from 'react';
import { useHistory } from 'react-router-dom';
import LogoutButton from '../auth/LogoutButton';
import { useSelector, useDispatch } from 'react-redux';
import { listAllProfiles  } from '../../store/profile'

import './profile-styles/profile.css'

function ProfilePage() {
    const history = useHistory();
    const dispatch = useDispatch();
    const accountHolder = useSelector(state => state.session.user);
    const profiles = useSelector(state => state.profile);

useEffect(() => {
    dispatch(listAllProfiles())
}, [dispatch])

    return (
        <div className='profile-page-container'>
            {/* <LogoutButton /> */}
            <div className='profile-form'>
                <div className='profile-question'>
                    Who's watching?
                </div>
                <div className='profile-picker-div'>
                    {
                        profiles?.map((profile) => {
                            return (
                                <div>
                                    <img
                                        className='profile-main-img'
                                        src={profile.profile_img}
                                        alt='profile-img'
                                    />
                                    <div className='profile-name'>
                                        {profile.username}
                                    </div>
                                </div>
                            )
                        })
                    }
                    {
                        profiles.length < 5
                        && (
                            <div>
                                <div className='profile-main-new'>
                                    ADD_PLUS_SIGN
                                </div>
                                <div className='profile-name'>
                                    Add Profile
                                </div>
                            </div>
                        )
                    }
                </div>
            </div>
                <div className='profile-manage-btn-div'>
                    <a className='profile-manage-btn' href='/profile/manage'>
                        Manage Profiles
                    </a>
                </div>
        </div>
    );
}
export default ProfilePage;
