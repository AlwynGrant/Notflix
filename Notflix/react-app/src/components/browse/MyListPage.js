import React, { useState, useEffect } from 'react';
import { NavLink, useParams } from 'react-router-dom';
import { useDispatch } from 'react-redux';
import { useSelector } from 'react-redux';

import { listMyList } from '../../store/mylist'
import './browse-styles/mylist.css'

function MyListPage() {
    const { profile_id } = useParams();
    const dispatch = useDispatch();
    const myList = useSelector(state => state.mylist)

    useEffect(() => {
        dispatch(listMyList(profile_id))
    }, [dispatch])

    return (
        <div className='list-top-container'>
            <div className="list-content">
                <div className='list-title'>My List</div>
                <div className="my-list">
                    {
                        myList?.map((movie) => {
                            return (
                                <div className='list-inner-container'>
                                    <img className='list-img' src={movie.movie_thumbnail} alt='movie' />
                                    <div className='list-description'>Buttons go here</div>
                                </div>
                            )
                        })
                    }
                </div>
            </div>
        </div>
    );
}
export default MyListPage;
