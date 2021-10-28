import React, { useState, useEffect } from 'react';
import { useHistory, useParams } from 'react-router-dom';
import { useSelector, useDispatch } from 'react-redux';
import { changeProfile, removeProfile, listOneProfile, listAllProfiles } from '../../store/profile'

import './profile-styles/profile_edit.css'

function ProfileEditPage() {
    const history = useHistory();
    const dispatch = useDispatch();
    const { profile_id } = useParams();

    const [icon, setIcon] = useState(undefined)
    const [username, setUsername] = useState('')
    const [isForKids, setIsForKids] = useState(false)
    const [errors, setErrors] = useState([])

    const accountHolder = useSelector(state => state.session.user);
    const profile = useSelector(state => state.profile[0]);

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

    const handleSubmitEdit = (e) => {
        e.preventDefault();

        const editThisProfile = {
            username: username,
            profile_img: icon,
            kids: isForKids
        };
        if (username.length > 2) {
            dispatch(changeProfile(editThisProfile, profile_id)).then(() => {
                setUsername("");
                setIsForKids(false);
            });
            dispatch(listAllProfiles())
            history.push('/profiles/manage');
        } else {
            setErrors(['Username must be 3 or more characters'])
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
        </div>
    );
}
export default ProfileEditPage;
