import React, { useState, useEffect } from 'react';
import { useParams, useHistory } from 'react-router-dom';
import { useDispatch, useSelector } from 'react-redux';
import { listAllProfiles } from '../../store/profile';
import LogoutButton from '../auth/LogoutButton';
import './navbar-styles/navbar_movies.css'

import notflix_text_1000 from './images/notflix_text_1000.png'

const NavBarMovies = () => {
    const { profile_id } = useParams();
    const dispatch = useDispatch();
    const history = useHistory();

    const profiles = useSelector(state => state.profile);
    const currentProfile = profiles?.filter(profile => String(profile.id) === profile_id)[0];
    const otherProfiles = profiles?.filter(profile => String(profile.id) !== profile_id);

    const [dropdown, setDropdown] = useState(false)

    const handleDropdown = (e) => {
        e.preventDefault();
        setDropdown(!dropdown)
    }

    const handleSwitchProfiles = (e, profileId) => {
        e.preventDefault();
        history.push(`/profiles/${profileId}/movies`)
    }

    useEffect(() => {
        dispatch(listAllProfiles(profile_id))
    }, dispatch)
    
    return (
        <nav className='navbar-movies'>
            <div className='navbar-movies-container'>
                <div className='navbar-movies-link-container'>
                    <a className='movies-logo' href={`/profiles/${profile_id}/movies`}>
                        <img className='movies-logo' src={notflix_text_1000} alt='logo-here'/>
                    </a>

                    <a target="_blank" rel="noreferrer" href={'https://github.com/AlwynGrant/Notflix'}>Github</a>
                    <a target="_blank" rel="noreferrer" href={'https://www.linkedin.com/in/alwyn-grant-928b091a3/'}>LinkdIn</a>
                    <a href={`/profiles/${profile_id}/my-list`}>My list</a>
                </div>
                <div>
                    <div onClick={(e) => handleDropdown(e)} className='profile-nav-img-container'>
                        <img className='profile-nav-img' src={currentProfile?.profile_img} alt='profile-pic'/>
                    </div>
                </div>
            </div>
                    {
                        dropdown && (
                            <div className='profile-dropdown-container'>
                                <div className='profile-pick-div'>
                                    {
                                        otherProfiles?.map((profile) => {
                                            return (
                                                <div key={profile.id} onClick={(e) => handleSwitchProfiles(e, profile.id)} className='profile-dropdown-sect'>
                                                    <img className='profile-nav-img' src={profile.profile_img} alt='profile-alt-pic'/>
                                                    <div className='profile-nav-name'>{profile.username}</div>
                                                </div>
                                            )
                                        })
                                    }
                                </div>
                                <a className='profile-manage-link' href='/profiles/manage'>Manage profiles</a>
                                <div className='profile-logout'>
                                    <LogoutButton />
                                </div>
                            </div>
                        )
                    }
        </nav>
    );
}

export default NavBarMovies;
