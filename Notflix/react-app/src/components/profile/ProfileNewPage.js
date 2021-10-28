import React, { useState } from 'react';
import { useHistory } from 'react-router-dom';
import { useDispatch } from 'react-redux';
import { createProfile } from '../../store/profile'
import IconModal from '../modals/ProfileIconModal';

import './profile-styles/profile_new.css'

function ProfileNewPage() {
    const history = useHistory();
    const dispatch = useDispatch();

    const iconArr = [
        'https://kickrbucket.s3.us-west-1.amazonaws.com/1634746455038.jpg',
        'https://kickrbucket.s3.us-west-1.amazonaws.com/1634746460342.png',
        'https://kickrbucket.s3.us-west-1.amazonaws.com/1634746449917.png',
        'https://kickrbucket.s3.us-west-1.amazonaws.com/1634746445926.png',
        'https://kickrbucket.s3.us-west-1.amazonaws.com/1634746441814.png',
        'https://kickrbucket.s3.us-west-1.amazonaws.com/1634746437849.png',
        'https://kickrbucket.s3.us-west-1.amazonaws.com/1634746431496.png',
        'https://kickrbucket.s3.us-west-1.amazonaws.com/1634746427415.png',
        'https://kickrbucket.s3.us-west-1.amazonaws.com/1634746421357.png',
        'https://kickrbucket.s3.us-west-1.amazonaws.com/1634746854870.jpg'
    ]

    const [icon, setIcon] = useState(iconArr[0]);
    const [username, setUsername] = useState('');
    const [isForKids, setIsForKids] = useState(false);
    const [iconModal, setIconModal] = useState(false);
    const [errors, setErrors] = useState([]);


    const handleSubmit = (e) => {
        e.preventDefault();

        const newProfile = {
            username: username,
            profile_img: icon,
            kids: isForKids
        };

        if (username.length > 2 && username.length <= 50) {
            dispatch(createProfile(newProfile)).then(() => {
                setUsername("");
                setIsForKids(false);
            });
            history.push('/profiles');
        } else {
            setErrors(['Username must be between 3 & 50 characters.'])
        }
    };

    const handleCancel = (e) => {
        e.preventDefault();

        history.push('/profiles')
    }

    const handleIconModal = (e) => {
        e.preventDefault()
        setIconModal(true);
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
                        <div onClick={(e) => handleIconModal(e)} className='profile-edit-change'>Choose Icon</div>
                        <img
                            className='profile-new-img'
                            src={icon}
                            onChange={(e) => setIcon(e.target.value)}
                        />
                        <div className='profile-new-input-container'>
                            {errors.map((error, ind) => (
                                <div className='profile-new-errors' key={ind}>{error}</div>
                            ))}
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
            {
                iconModal && (
                    <IconModal
                        show={iconModal}
                        set={setIcon}
                        onClose={() => setIconModal(false)}
                    />
                )
            }
        </div>
    );
}
export default ProfileNewPage;
