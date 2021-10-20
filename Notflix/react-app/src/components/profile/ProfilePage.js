import React, { useState, useEffect } from 'react';
import { useHistory } from 'react-router-dom';
import LogoutButton from '../auth/LogoutButton';
import { useSelector, useDispatch } from 'react-redux';
import { listAllProfiles  } from '../../store/profile'

function ProfilePage() {
    const history = useHistory();
    const dispatch = useDispatch();
    const accountHolder = useSelector(state => state.session.user);
    const profiles = useSelector(state => state.profiles);

useEffect(() => {
    dispatch(listAllProfiles())
}, [dispatch])

    return (
        <>
            <div>
                PROFILE PAGE
            </div>
            <LogoutButton />
        </>
    );
}
export default ProfilePage;
