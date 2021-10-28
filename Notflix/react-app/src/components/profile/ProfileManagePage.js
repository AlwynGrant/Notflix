import React, { useState, useEffect } from 'react';
import { useHistory } from 'react-router-dom';
import { useSelector, useDispatch } from 'react-redux';
import { listAllProfiles } from '../../store/profile'

import './profile-styles/profile_manage.css'
import white_cross from './profile-assets/white_cross.png'
// import edit_icon from './profile-assets/edit_icon.jpg'

function ProfileManagePage() {
    const history = useHistory();
    const dispatch = useDispatch();
    const accountHolder = useSelector(state => state.session.user);
    const profiles = useSelector(state => state.profile);

    useEffect(() => {
        dispatch(listAllProfiles())
    }, [dispatch])

    return (
        <div className='profile-mng-container'>
            {/* <LogoutButton /> */}
            <div className='profile-mng-form'>
                <div className='profile-mng-question'>
                    Manage Profiles:
                </div>
                <div className='profile-picker-mng-div'>
                    {
                        profiles?.map((profile) => {
                            return (
                                <a className='mng-overlay' href={`/profiles/${profile.id}/edit`}>
                                    <div className='mng-over-text'>Manage</div>
                                    <img
                                        className='profile-main-mng-img'
                                        src={profile.profile_img}
                                        alt='profile-img'
                                        />
                                    <div className='profile-mng-name'>
                                        {profile.username}
                                    </div>
                                </a>
                            )
                        })
                    }
                    {
                        profiles.length < 5
                        && (
                            <a className='profile-link-mng-new' href='/profiles/new'>
                                <div className='profile-img-mng-container' >
                                    <img
                                        className='profile-main-img-add'
                                        src={white_cross}
                                        alt='profile-new-img'
                                    />
                                </div>
                                <div className='profile-mng-name'>
                                    Add Profile
                                </div>
                            </a>
                        )
                    }
                </div>
            </div>
            <div className='profile-done-btn-div'>
                <a className='profile-done-btn' href='/profiles'>
                    Done
                </a>
            </div>
        </div>
    );
}
export default ProfileManagePage;
