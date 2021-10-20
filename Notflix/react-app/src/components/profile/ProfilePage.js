import React, { useState, useEffect } from 'react';
import { useHistory } from 'react-router-dom';
import LogoutButton from '../auth/LogoutButton';
import { useSelector, useDispatch } from 'react-redux';
import { listAllProfiles  } from '../../store/profile'

import './profile-styles/profile.css'
import white_cross from './profile-assets/white_cross.png'

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
                            <a href='/profiles/new'>
                                <div className='profile-img-container' >
                                    <img
                                        className='profile-main-img-add'
                                        src={white_cross}
                                        alt='profile-new-img'
                                    />
                                </div>
                                <div className='profile-name'>
                                    Add Profile
                                </div>
                            </a>
                        )
                    }
                </div>
            </div>
                <div className='profile-manage-btn-div'>
                    <a className='profile-manage-btn' href='/profiles/manage'>
                        Manage Profiles
                    </a>
                </div>
        </div>
    );
}
export default ProfilePage;
