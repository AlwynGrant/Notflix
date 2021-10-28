import React, { useState, useEffect } from 'react';
import { useParams, useHistory } from 'react-router-dom';
import { likeUnlikeMovie, listMyLikes } from '../../store/mylike'
import { listMyList, addToMyList } from '../../store/mylist'
import { useDispatch, useSelector } from 'react-redux';
import './movieinfo.css'


function MoreInfoModal(props) {
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

    if (!props.show) {
        return null;
    }

    return (
            <div className='movie-modal' onClick={props.onClose}>
                <div className='movie-modal-content' onClick={e => e.stopPropagation()}>
                    <div className='movie-modal-img-container'>
                        <img className='movie-modal-img' src={props.movie.movie_thumbnail}/>
                    </div>

                    <div className='movie-modal-header'>
                        <h4 className='movie-modal-title'>{props.movie.name}</h4>

                        <div className='movie-modal-options'>
                            <button onClick={(e) => handleMovieBtn(e, props.movie.id)} className='list-row-1-btns'>
                                <span class="material-icons">
                                    play_circle_outline
                                </span>
                            </button>
                            {
                                myList?.some((savedMovie) => savedMovie.id === props.movie.id)
                                    ? <button className='list-row-1-btns' onClick={(e) => handleMyListBtn(e, props.movie.id)}>
                                        <span className="material-icons">
                                            check_circle_outline
                                        </span>
                                    </button>
                                    : <button className='list-row-1-btns' onClick={(e) => handleMyListBtn(e, props.movie.id)}>
                                        <span className="material-icons">
                                            add_circle_outline
                                        </span>
                                    </button>
                            }
                            {
                                myLike?.some((likedMovie) => likedMovie.id === props.movie.id)
                                    ? <button className='list-row-1-btns' onClick={(e) => handleLikeBtn(e, props.movie.id)}>
                                        <span className="material-icons">
                                            thumb_down_off_alt
                                        </span>
                                    </button>
                                    : <button className='list-row-1-btns' onClick={(e) => handleLikeBtn(e, props.movie.id)}>
                                        <span className="material-icons">
                                            thumb_up_off_alt
                                        </span>
                                    </button>
                            }

                        </div>
                    </div>
                    <div className='movie-modal-body'>
                        {props.movie.description}
                    </div>
                    <div className='movie-modal-details'>
                        <div className='bigger-deets'>
                            <div className='movie-modal-rating'>{props.movie.rating}%</div>
                            <div className='movie-modal-maturity-rating'>{props.movie.maturity_rating}</div>
                        </div>
                        <div className='movie-modal-genres'>
                            {
                                props.movie.genres.map((genre) => {
                                    return (
                                        <div className='list-row-3-genre-div'>{genre}</div>
                                    )
                                })
                            }
                        </div>
                        <div className='smaller-deets'> <div>Run time: </div> {props.movie.run_time}</div>
                        <div className='smaller-deets'> <div>Released: </div> {props.movie.year_released}</div>
                        <div className='smaller-deets'> <div>Starring: </div> {props.movie.cast}</div>
                        <div className='smaller-deets'> <div>Director: </div> {props.movie.director}</div>
                        <div className='smaller-deets'> <div>Production: </div> {props.movie.production}</div>
                    </div>
                </div>
            </div>
    );
}
export default MoreInfoModal;
