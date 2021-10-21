import React, { useState, useEffect } from 'react';
import { useHistory } from 'react-router-dom';
import { useSelector, useDispatch } from 'react-redux';
import { createProfile } from '../../store/profile'

import './profile-styles/profile_new.css'

function ProfileNewPage() {
    const history = useHistory();
    const dispatch = useDispatch();

    const [icon, setIcon] = useState(undefined)
    const [username, setUsername] = useState('')
    const [isForKids, setIsForKids] = useState(false)
    console.log(icon, username, isForKids)
    const accountHolder = useSelector(state => state.session.user);

    const iconArr = [
        'https://kickrbucket.s3.us-west-1.amazonaws.com/1634746460342.png',
        'https://kickrbucket.s3.us-west-1.amazonaws.com/1634746455038.jpg',
        'https://kickrbucket.s3.us-west-1.amazonaws.com/1634746449917.png',
        'https://kickrbucket.s3.us-west-1.amazonaws.com/1634746445926.png',
        'https://kickrbucket.s3.us-west-1.amazonaws.com/1634746441814.png',
        'https://kickrbucket.s3.us-west-1.amazonaws.com/1634746437849.png',
        'https://kickrbucket.s3.us-west-1.amazonaws.com/1634746431496.png',
        'https://kickrbucket.s3.us-west-1.amazonaws.com/1634746427415.png',
        'https://kickrbucket.s3.us-west-1.amazonaws.com/1634746421357.png',
        'https://kickrbucket.s3.us-west-1.amazonaws.com/1634746854870.jpg'
    ]

    const handleSubmit = (e) => {
        e.preventDefault();

        const newProfile = {
            username: username,
            profile_img: icon,
            kids: isForKids
        };

        dispatch(createProfile(newProfile)).then(() => {
            setUsername("");
            setIsForKids(false);
        });

        history.push('/profiles');
    };

    const handleCancel = (e) => {
        e.preventDefault();

        history.push('/profiles')
    }

    return (
        <div className='profile-new-container'>
            <div className='profile-new-form'>
                <div className='profile-new-text'>
                    Add Profile
                </div>
                <div className='profile-new-sub-text'>
                    Add a profile for another person watching Notflix.
                </div>
                <form className='profile-new-form-inputs' onSubmit={(e) => handleSubmit(e)}>
                    <div className='profile-new-img-div'>
                        <select
                            className='profile-new-select'
                            style={{ backgroundImage: `url(${icon})` }}
                            value={icon}
                            onChange={(e) => setIcon(e.target.value)}
                        >
                            {
                                iconArr.map((p_icon, index) => {
                                    return <option
                                                className='profile-new-option'
                                                key={index}
                                                style={{ backgroundImage: `url(${icon})` }}
                                            >{p_icon}</option>
                                })
                            }
                        </select>
                        <div className='profile-new-input-container'>
                            <input
                                className='profile-new-name-input'
                                placeholder='Name'
                                type='text'
                                value={username}
                                onChange={(e) => setUsername(e.target.value)}
                            />
                            <input
                                type='checkbox'
                                className='profile-new-name-checkbox'
                                defaultChecked={false}
                                checked={isForKids}
                                onChange={(e) => setIsForKids(e.target.checked)}
                            />
                            <p className='profile-new-checkbox-name'>Kid?</p>
                        </div>
                    </div>
                    <div className='profile-new-btn-div'>
                        <button
                            className='profile-new-continue'
                            type='Submit'
                        >Continue</button>
                        <button
                            className='profile-new-cancel'
                            onClick={(e) => handleCancel(e)}
                        >Cancel</button>
                    </div>
                </form>
            </div>
        </div>
    );
}
export default ProfileNewPage;
