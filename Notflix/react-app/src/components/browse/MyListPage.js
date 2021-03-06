import React, { useEffect } from 'react';
import { useParams, useHistory } from 'react-router-dom';
import { useDispatch } from 'react-redux';
import { useSelector } from 'react-redux';

import { likeUnlikeMovie, listMyLikes } from '../../store/mylike'
import { listMyList, addToMyList } from '../../store/mylist'

import './browse-styles/mylist.css'

function MyListPage() {
    const { profile_id } = useParams();
    const dispatch = useDispatch();
    const history = useHistory();
    const myList = useSelector(state => state.mylist)
    const myLike = useSelector(state => state.mylike)

    useEffect(() => {
        dispatch(listMyList(profile_id))
        dispatch(listMyLikes(profile_id))
    }, [dispatch])

    const handleMyListBtn = (e, movieId) => {
        e.preventDefault()
        dispatch(addToMyList(profile_id, movieId))
    }

    const handleLikeBtn = (e, movieId) => {
        e.preventDefault()
        dispatch(likeUnlikeMovie(profile_id, movieId))
    }

    const handleMovieBtn = (e, movieId) => {
        e.preventDefault()
        history.push(`/profiles/${profile_id}/movies/${movieId}`)
    }

    return (
        <div className='list-top-container'>
            <div className="list-content">
                <div className='list-title'>My List</div>
                <div className="my-list">
                    {
                        myList?.map((movie) => {
                            return (
                                <div key={`mls-${movie.id}`} className='list-inner-container'>
                                    {/* <ReactPlayer
                                        url={movie.movie_url}
                                        className="react-player"
                                        playing={false}
                                        muted={true}
                                        loop={false}

                                        width="400px"
                                    /> */}
                                    <img className='list-img' src={movie.movie_thumbnail} alt='movie' />
                                    <div className='list-description'>
                                        <div className='list-row-1'>
                                            <div className='list-row-1-btn-container'>
                                                <button onClick={(e) => handleMovieBtn(e, movie.id)} className='list-row-1-btn-play'>
                                                    <span className="material-icons">
                                                        play_circle_outline
                                                    </span>
                                                </button>
                                                {
                                                    myList?.some((savedMovie) => savedMovie.id === movie.id)
                                                        ? <button className='list-row-1-btns' onClick={(e) => handleMyListBtn(e, movie.id)}>
                                                            <span className="material-icons">
                                                                check_circle_outline
                                                            </span>
                                                        </button>
                                                        : <button className='list-row-1-btns' onClick={(e) => handleMyListBtn(e, movie.id)}>
                                                            <span className="material-icons">
                                                                add_circle_outline
                                                            </span>
                                                        </button>
                                                }
                                                {
                                                    myLike?.some((likedMovie) => likedMovie.id === movie.id)
                                                        ? <button className='list-row-1-btns' onClick={(e) => handleLikeBtn(e, movie.id)}>
                                                            <span className="material-icons">
                                                                thumb_down_off_alt
                                                            </span>
                                                        </button>
                                                        : <button className='list-row-1-btns' onClick={(e) => handleLikeBtn(e, movie.id)}>
                                                            <span className="material-icons">
                                                                thumb_up_off_alt
                                                            </span>
                                                        </button>
                                                }
                                            </div>
                                            <button className='list-row-1-btns more-info'>
                                                <span className="material-icons">
                                                    arrow_circle_down
                                                </span>
                                            </button>
                                        </div>
                                        <div className='list-row-2'>
                                            <div className='list-row-2-rating'>{movie.rating}%</div>
                                            <div className='list-row-2-maturity-rating'>{movie.maturity_rating}</div>
                                        </div>
                                        <div className='list-row-3'>
                                            {
                                                movie.genres.map((genre, i) => {
                                                    return (
                                                        <div key={`ml-${i}`} className='list-row-3-genre-div'>{genre}</div>
                                                    )
                                                })
                                            }
                                        </div>
                                    </div>
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
