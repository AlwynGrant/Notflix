import React, { useEffect } from 'react';
import { useHistory } from 'react-router-dom';
import { useSelector, useDispatch } from 'react-redux';
import { listAllProfiles } from '../../store/profile'

// import './profile-styles/about.css'

function AboutPage() {
    const history = useHistory();
    const dispatch = useDispatch();
    const profiles = useSelector(state => state.profile);

    return (
        <div className='profile-page-container'>
            <div className='profile-form'>
                test
            </div>
        </div>
    );
}
export default AboutPage;
