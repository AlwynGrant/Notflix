import React, { useState, useEffect } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { useHistory } from 'react-router-dom';
import { listAllMovies } from '../../store/movie'
import './browse-styles/browse.css'

function BrowsePage() {
    const history = useHistory();
    const dispatch = useDispatch();

    const movies = useSelector(state => state.movies)
    console.log(movies)
    useEffect(() => {
        dispatch(listAllMovies())
    }, [dispatch])

    return (
        <>
        <div className='browse-preview-container'>
            <div className='browse-preview-feature-info'>
                <div className='browse-preview-feature-title'>FEATURED_TITLE_DIV</div>
                <div className='browse-preview-feature-summary'>FEATURED_SUMMARY_DIV</div>
                <div className='browse-preview-feature-btn-container'>
                    <button className='browse-preview-play-btn'>PLAY_BUTTON</button>
                    <button className='browse-preview-more-info-btn'>MORE_INFO_BUTTON</button>
                </div>
            </div>
            <h1>FIRST_FEATURED_PREVIEW_CONTAINER</h1>
        </div>
            <div className="browse-car-featured">
                {
                    movies?.map((movie) => {
                        return (
                            <img className='browse-img' src={movie.movie_thumbnail} alt='movie'/>
                        )
                    })
                }
            </div>
            <div className="browse-car-action">
                {
                    movies?.map((movie) => {
                        return (
                            <img className='browse-img' src={movie.movie_thumbnail} alt='movie'/>
                        )
                    })
                }
            </div>
        </>
    );
}
export default BrowsePage;
