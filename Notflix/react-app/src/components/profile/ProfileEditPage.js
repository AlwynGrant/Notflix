import React, { useState, useEffect } from 'react';
import { useHistory } from 'react-router-dom';
import { useSelector, useDispatch } from 'react-redux';
// import { createProfile } from '../../store/profile'

import './profile-styles/profile_edit.css'

function ProfileEditPage() {
    const history = useHistory();
    const dispatch = useDispatch();

    const [icon, setIcon] = useState(undefined)
    const [username, setUsername] = useState('')
    const [isForKids, setIsForKids] = useState(false)

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

        // dispatch(createProfile(newProfile)).then(() => {
        //     setUsername("");
        //     setIsForKids(false);
        // });

        history.push('/profiles/manage');
    };

    const handleCancel = (e) => {
        e.preventDefault();

        history.push('/profiles/manage')
    }

    return (
        <div className='profile-edit-container'>
            <div className='profile-edit-form'>
                <div className='profile-edit-text'>
                    Edit Profile
                </div>
                <form className='profile-edit-form-inputs' onSubmit={(e) => handleSubmit(e)}>
                    <div className='profile-edit-img-div'>
                            <select
                                className='profile-edit-select'
                                style={{ backgroundImage: `url(${icon})` }}
                                value={icon}
                                onChange={(e) => setIcon(e.target.value)}
                            >
                                {
                                    iconArr.map((p_icon, index) => {
                                        return <option
                                            className='profile-edit-option'
                                            key={index}
                                            style={{ backgroundImage: `url(${icon})` }}
                                        >{p_icon}</option>
                                    })
                                }
                            </select>
                    </div>
                        <div className='profile-edit-input-container'>
                            <input
                                className='profile-edit-name-input'
                                placeholder='Name'
                                type='text'
                                value={username}
                                onChange={(e) => setUsername(e.target.value)}
                            />
                            <input
                                type='checkbox'
                                className='profile-edit-name-checkbox'
                                defaultChecked={false}
                                checked={isForKids}
                                onChange={(e) => setIsForKids(e.target.checked)}
                            />
                            <p className='profile-edit-checkbox-name'>Kid?</p>
                        </div>
                        <div className='sub-form-edit-container'>
                            <div className='profile-edit-btn-div'>
                                <button
                                    className='profile-edit-continue'
                                    type='Submit'
                                >Continue</button>
                                <button
                                    className='profile-edit-cancel'
                                    onClick={(e) => handleCancel(e)}
                                >Cancel</button>
                                <button
                                    className='profile-edit-cancel'
                                    onClick={(e) => handleCancel(e)}
                                >Delete</button>
                            </div>
                        </div>
                </form>
            </div>
        </div>
    );
}
export default ProfileEditPage;
