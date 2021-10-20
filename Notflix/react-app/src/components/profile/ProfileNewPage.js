import React, { useState, useEffect } from 'react';
import { useHistory } from 'react-router-dom';
import { useSelector, useDispatch } from 'react-redux';
import { createProfile } from '../../store/profile'

import './profile-styles/profile_new.css'
import profile_icons from '../../notflix_profile_imgs/notflix-profile-imgs';

function ProfileNewPage() {
    const history = useHistory();
    const dispatch = useDispatch();

    const [icon, setIcon] = useState(undefined)
    const [username, setUsername] = useState('')
    const [isForKids, setIsForKids] = useState(false)
    console.log(icon)

    const accountHolder = useSelector(state => state.session.user);

    const handleSubmit = (e) => {
        e.preventDefault();

        const newProfile = {
            username: username,
            kids: isForKids
        };

        dispatch(createProfile(newProfile)).then(() => {
            setUsername("");
            setIsForKids(false);
        });
        history.push('/profiles');
    };

    return (
        <div className='profile-new-container'>
            <div className='profile-new-form'>
                <div className='profile-new-text'>
                    Add Profile
                </div>
                <div className='profile-new-sub-text'>
                    Add a profile for another person watching Notflix.
                </div>
                <form className='profile-new-form-inputs'>
                    <div className='profile-new-img-div'>
                        <select
                            className='profile-new-select'
                            style={{ backgroundImage: `url(${icon})` }}
                            value={icon}
                            onChange={(e) => setIcon(e.target.value)}
                        >
                            {
                                profile_icons.map((p_icon, index) => {
                                    return <option
                                                className='profile-new-option'
                                                key={index}
                                                value={p_icon}
                                                style={{ backgroundImage: `url(${p_icon})` }}
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
                                value={isForKids}
                                onChange={(e) => setIsForKids(e.target.value)}
                            />
                            <p className='profile-new-checkbox-name'>Kid?</p>
                        </div>
                    </div>
                    <div className='profile-new-btn-div'>
                        <button className='profile-new-continue'>Continue</button>
                        <button className='profile-new-cancel'>Cancel</button>
                    </div>
                </form>
            </div>
        </div>
    );
}
export default ProfileNewPage;
