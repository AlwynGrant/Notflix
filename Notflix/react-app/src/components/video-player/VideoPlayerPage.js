import React, { useEffect } from 'react';
import { listOneMovie } from '../../store/movie';
import { useSelector, useDispatch } from 'react-redux';
import { useHistory, useParams } from 'react-router-dom';
import ReactPlayer from 'react-player'

import './video.css'

function VideoPlayerPage() {
    const history = useHistory();
    const dispatch = useDispatch();
    const { profile_id, movieId } = useParams();
    const movie = useSelector(state => state.movies[0])

    useEffect(() => {
        dispatch(listOneMovie(movieId))
    }, [dispatch, movie?.url])

    const handleBackBtn = (e) => {
        e.preventDefault();
        history.push(`/profiles/${profile_id}/movies`)
    }
    return (
        <div className='movie-player-container'>
            <button onClick={(e) => handleBackBtn(e)} className='movie-player-back-btn'>
                <span className="material-icons">
                arrow_back
                </span>
            </button>
            <ReactPlayer
                className='movie-video'
                playing={true}
                muted={false}
                controls={true}
                url={movie?.movie_url}
                volume={0.3}
                width='100%'
                height='100%'
            />
        </div>
    );
}
export default VideoPlayerPage;
