import React, { useState, useEffect } from 'react';
import { useHistory, useParams } from 'react-router-dom';
import { useSelector, useDispatch } from 'react-redux';
import { changeProfile, removeProfile, listOneProfile, listAllProfiles } from '../../store/profile'
import IconModal from '../modals/ProfileIconModal';

import './profile-styles/profile_edit.css'

function ProfileEditPage() {
    const history = useHistory();
    const dispatch = useDispatch();
    const { profile_id } = useParams();

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

    const profile = useSelector(state => state.profile[0]);

    const [icon, setIcon] = useState(undefined);
    const [username, setUsername] = useState('');
    const [isForKids, setIsForKids] = useState(false);
    const [iconModal, setIconModal] = useState(false);
    const [errors, setErrors] = useState([]);


    const handleSubmitEdit = (e) => {
        e.preventDefault();

        const editThisProfile = {
            username: username,
            profile_img: icon,
            kids: isForKids
        };
        if (username.length > 2 && username.length <= 50) {
            dispatch(changeProfile(editThisProfile, profile_id)).then(() => {
                setUsername("");
                setIsForKids(false);
            });
            dispatch(listAllProfiles())
            history.push('/profiles/manage');
        } else {
            setErrors(['Username must be between 3 & 50 characters.'])
        }
    };

    const handleSubmitDelete = (e) => {
        e.preventDefault();
        dispatch(removeProfile(profile_id))
        dispatch(listAllProfiles())
        history.push('/profiles/manage')
    }

    const handleCancel = (e) => {
        e.preventDefault();

        history.push('/profiles/manage')
    }

    const handleIconModal = (e) => {
        e.preventDefault()
        setIconModal(true);
    }

    useEffect(() => {
        dispatch(listOneProfile(profile_id))
        setIsForKids(profile?.kids)
        setUsername(profile?.username)
        setIcon(profile?.profile_img)
    },[dispatch, profile?.id])

    return (
        <div className='profile-edit-container'>
            <div className='profile-edit-form'>
                <div className='profile-edit-text'>
                    Edit Profile
                </div>
                <form className='profile-edit-form-inputs' onSubmit={(e) => handleSubmitEdit(e)}>
                    <div className='profile-edit-img-div'>
                        <div onClick={(e) => handleIconModal(e)} className='profile-edit-change'>Change Icon</div>
                        <img
                            className='profile-new-img'
                            src={icon}
                            onChange={(e) => setIcon(e.target.value)}
                        />
                    </div>
                        <div className='profile-edit-input-container'>
                        {errors.map((error, ind) => (
                            <div className='profile-edit-errors' key={ind}>{error}</div>
                        ))}
                            <input
                                className='profile-edit-name-input'
                                placeholder='Name'
                                type='text'
                                value={username}
                                onChange={(e) => setUsername(e.target.value)}
                            />
                            <div className='profile-edit-maturity'>
                                <input
                                    type='checkbox'
                                    className='profile-edit-name-checkbox'
                                    defaultChecked={false}
                                    checked={isForKids}
                                    onChange={(e) => setIsForKids(e.target.checked)}
                                />
                                <p className='profile-edit-checkbox-name'>Kid?</p>
                            </div>
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
                                    className='profile-edit-delete'
                                    onClick={(e) => handleSubmitDelete(e)}
                                >Delete Profile</button>
                            </div>
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
export default ProfileEditPage;
