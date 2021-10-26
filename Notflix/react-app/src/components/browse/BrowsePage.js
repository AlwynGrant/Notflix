import React, { useState, useEffect } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { useHistory, useParams } from 'react-router-dom';
import { listAllMovies } from '../../store/movie'
import { getOneProfile, listOneProfile } from '../../store/profile'
import { addToMyList, listMyList } from '../../store/mylist'
import { listMyLikes, likeUnlikeMovie } from '../../store/mylike'

import './browse-styles/browse.css'


function BrowsePage() {
    const { profile_id } = useParams();
    const history = useHistory();
    const dispatch = useDispatch();

    const movies = useSelector(state => state.movies)
    const profile = useSelector(state => state.profile[0])
    const myList = useSelector(state => state.mylist)
    const myLike = useSelector(state => state.mylike)

    const actionMovies = movies?.filter(movie => movie.genres[0] === 'Action/Adventure')
    const animeMovies = movies?.filter(movie => movie.genres[0] === 'Anime')
    const comedyMovies = movies?.filter(movie => movie.genres[0] === 'Comedy')
    const docuMovies = movies?.filter(movie => movie.genres[0] === 'Documentary')
    const horrorMovies = movies?.filter(movie => movie.genres[0] === 'Horror')
    const romanceMovies = movies?.filter(movie => movie.genres[0] === 'Romance')
    const thrillerMovies = movies?.filter(movie => movie.genres[0] === 'Thrillers')
    const featuredMovies = movies?.filter(movie => movie.genres[1] === 'Featured')



    useEffect(() => {
        dispatch(listAllMovies())
    }, [dispatch])

    useEffect(() => {
        dispatch(listOneProfile(profile_id))
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

    return (
        <div className='browse-top-container'>
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
                <div className='slide-title'>Featured</div>
                <div className="browse-car-list">
                    {
                        featuredMovies?.map((movie) => {
                            return (
                                <div className='list-inner-container'>
                                    <img className='list-img' src={movie.movie_thumbnail} alt='movie' />
                                    <div className='list-description'>
                                        <div className='list-row-1'>
                                            <div className='list-row-1-btn-container'>
                                                <button className='list-row-1-btn-play'>
                                                    <span class="material-icons">
                                                        play_circle_outline
                                                    </span>
                                                </button>
                                                {
                                                    myList?.some((savedMovie) => savedMovie.id === movie.id)
                                                        ? <button className='list-row-1-btns' onClick={(e) => handleMyListBtn(e, movie.id)}>
                                                            <span class="material-icons">
                                                                check_circle_outline
                                                            </span>
                                                        </button>
                                                        : <button className='list-row-1-btns' onClick={(e) => handleMyListBtn(e, movie.id)}>
                                                            <span class="material-icons">
                                                                add_circle_outline
                                                            </span>
                                                        </button>
                                                }
                                                {
                                                    myLike?.some((likedMovie) => likedMovie.id === movie.id)
                                                        ? <button className='list-row-1-btns' onClick={(e) => handleLikeBtn(e, movie.id)}>
                                                            <span class="material-icons">
                                                                thumb_down_off_alt
                                                            </span>
                                                        </button>
                                                        : <button className='list-row-1-btns' onClick={(e) => handleLikeBtn(e, movie.id)}>
                                                            <span class="material-icons">
                                                                thumb_up_off_alt
                                                            </span>
                                                        </button>
                                                }
                                            </div>
                                            <button className='list-row-1-btns'>
                                                <span class="material-icons">
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
                                                movie.genres.map((genre) => {
                                                    return (
                                                        <div className='list-row-3-genre-div'>{genre}</div>
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
            <div className="browse-car-action">
                <div className='slide-title'>Action & Adventure</div>
                <div className="browse-car-list">
                    {
                        actionMovies?.map((movie) => {
                            return (
                                <div className='list-inner-container'>
                                    <img className='list-img' src={movie.movie_thumbnail} alt='movie' />
                                    <div className='list-description'>
                                        <div className='list-row-1'>
                                            <div className='list-row-1-btn-container'>
                                                <button className='list-row-1-btns'>
                                                    <span class="material-icons">
                                                        play_circle_outline
                                                    </span>
                                                </button>
                                                {
                                                    myList?.some((savedMovie) => savedMovie.id === movie.id)
                                                        ? <button className='list-row-1-btns' onClick={(e) => handleMyListBtn(e, movie.id)}>
                                                            <span class="material-icons">
                                                                check_circle_outline
                                                            </span>
                                                        </button>
                                                        : <button className='list-row-1-btns' onClick={(e) => handleMyListBtn(e, movie.id)}>
                                                            <span class="material-icons">
                                                                add_circle_outline
                                                            </span>
                                                        </button>
                                                }
                                                {
                                                    myLike?.some((likedMovie) => likedMovie.id === movie.id)
                                                        ? <button className='list-row-1-btns' onClick={(e) => handleLikeBtn(e, movie.id)}>
                                                            <span class="material-icons">
                                                                thumb_down_off_alt
                                                            </span>
                                                        </button>
                                                        : <button className='list-row-1-btns' onClick={(e) => handleLikeBtn(e, movie.id)}>
                                                            <span class="material-icons">
                                                                thumb_up_off_alt
                                                            </span>
                                                        </button>
                                                }
                                            </div>
                                            <button className='list-row-1-btns'>
                                                <span class="material-icons">
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
                                                movie.genres.map((genre) => {
                                                    return (
                                                        <div className='list-row-3-genre-div'>{genre}</div>
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
            <div className="browse-car-action">
                <div className='slide-title'>Anime</div>
                <div className="browse-car-list">
                    {
                        animeMovies?.map((movie) => {
                            return (
                                <div className='list-inner-container'>
                                    <img className='list-img' src={movie.movie_thumbnail} alt='movie' />
                                    <div className='list-description'>
                                        <div className='list-row-1'>
                                            <div className='list-row-1-btn-container'>
                                                <button className='list-row-1-btns'>
                                                    <span class="material-icons">
                                                        play_circle_outline
                                                    </span>
                                                </button>
                                                {
                                                    myList?.some((savedMovie) => savedMovie.id === movie.id)
                                                        ? <button className='list-row-1-btns' onClick={(e) => handleMyListBtn(e, movie.id)}>
                                                            <span class="material-icons">
                                                                check_circle_outline
                                                            </span>
                                                        </button>
                                                        : <button className='list-row-1-btns' onClick={(e) => handleMyListBtn(e, movie.id)}>
                                                            <span class="material-icons">
                                                                add_circle_outline
                                                            </span>
                                                        </button>
                                                }
                                                {
                                                    myLike?.some((likedMovie) => likedMovie.id === movie.id)
                                                        ? <button className='list-row-1-btns' onClick={(e) => handleLikeBtn(e, movie.id)}>
                                                            <span class="material-icons">
                                                                thumb_down_off_alt
                                                            </span>
                                                        </button>
                                                        : <button className='list-row-1-btns' onClick={(e) => handleLikeBtn(e, movie.id)}>
                                                            <span class="material-icons">
                                                                thumb_up_off_alt
                                                            </span>
                                                        </button>
                                                }
                                            </div>
                                            <button className='list-row-1-btns'>
                                                <span class="material-icons">
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
                                                movie.genres.map((genre) => {
                                                    return (
                                                        <div className='list-row-3-genre-div'>{genre}</div>
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
            <div className="browse-car-action">
                <div className='slide-title'>Comedy</div>
                <div className="browse-car-list">
                    {
                        comedyMovies?.map((movie) => {
                            return (
                                <div className='list-inner-container'>
                                    <img className='list-img' src={movie.movie_thumbnail} alt='movie' />
                                    <div className='list-description'>
                                        <div className='list-row-1'>
                                            <div className='list-row-1-btn-container'>
                                                <button className='list-row-1-btns'>
                                                    <span class="material-icons">
                                                        play_circle_outline
                                                    </span>
                                                </button>
                                                {
                                                    myList?.some((savedMovie) => savedMovie.id === movie.id)
                                                        ? <button className='list-row-1-btns' onClick={(e) => handleMyListBtn(e, movie.id)}>
                                                            <span class="material-icons">
                                                                check_circle_outline
                                                            </span>
                                                        </button>
                                                        : <button className='list-row-1-btns' onClick={(e) => handleMyListBtn(e, movie.id)}>
                                                            <span class="material-icons">
                                                                add_circle_outline
                                                            </span>
                                                        </button>
                                                }
                                                {
                                                    myLike?.some((likedMovie) => likedMovie.id === movie.id)
                                                        ? <button className='list-row-1-btns' onClick={(e) => handleLikeBtn(e, movie.id)}>
                                                            <span class="material-icons">
                                                                thumb_down_off_alt
                                                            </span>
                                                        </button>
                                                        : <button className='list-row-1-btns' onClick={(e) => handleLikeBtn(e, movie.id)}>
                                                            <span class="material-icons">
                                                                thumb_up_off_alt
                                                            </span>
                                                        </button>
                                                }
                                            </div>
                                            <button className='list-row-1-btns'>
                                                <span class="material-icons">
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
                                                movie.genres.map((genre) => {
                                                    return (
                                                        <div className='list-row-3-genre-div'>{genre}</div>
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
            <div className="browse-car-action">
                <div className='slide-title'>Documentary</div>
                <div className="browse-car-list">
                    {
                        docuMovies?.map((movie) => {
                            return (
                                <div className='list-inner-container'>
                                    <img className='list-img' src={movie.movie_thumbnail} alt='movie' />
                                    <div className='list-description'>
                                        <div className='list-row-1'>
                                            <div className='list-row-1-btn-container'>
                                                <button className='list-row-1-btns'>
                                                    <span class="material-icons">
                                                        play_circle_outline
                                                    </span>
                                                </button>
                                                {
                                                    myList?.some((savedMovie) => savedMovie.id === movie.id)
                                                        ? <button className='list-row-1-btns' onClick={(e) => handleMyListBtn(e, movie.id)}>
                                                            <span class="material-icons">
                                                                check_circle_outline
                                                            </span>
                                                        </button>
                                                        : <button className='list-row-1-btns' onClick={(e) => handleMyListBtn(e, movie.id)}>
                                                            <span class="material-icons">
                                                                add_circle_outline
                                                            </span>
                                                        </button>
                                                }
                                                {
                                                    myLike?.some((likedMovie) => likedMovie.id === movie.id)
                                                        ? <button className='list-row-1-btns' onClick={(e) => handleLikeBtn(e, movie.id)}>
                                                            <span class="material-icons">
                                                                thumb_down_off_alt
                                                            </span>
                                                        </button>
                                                        : <button className='list-row-1-btns' onClick={(e) => handleLikeBtn(e, movie.id)}>
                                                            <span class="material-icons">
                                                                thumb_up_off_alt
                                                            </span>
                                                        </button>
                                                }
                                            </div>
                                            <button className='list-row-1-btns'>
                                                <span class="material-icons">
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
                                                movie.genres.map((genre) => {
                                                    return (
                                                        <div className='list-row-3-genre-div'>{genre}</div>
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
            <div className="browse-car-action">
                <div className='slide-title'>Horror</div>
                <div className="browse-car-list">
                    {
                        horrorMovies?.map((movie) => {
                            return (
                                <div className='list-inner-container'>
                                    <img className='list-img' src={movie.movie_thumbnail} alt='movie' />
                                    <div className='list-description'>
                                        <div className='list-row-1'>
                                            <div className='list-row-1-btn-container'>
                                                <button className='list-row-1-btns'>
                                                    <span class="material-icons">
                                                        play_circle_outline
                                                    </span>
                                                </button>
                                                {
                                                    myList?.some((savedMovie) => savedMovie.id === movie.id)
                                                        ? <button className='list-row-1-btns' onClick={(e) => handleMyListBtn(e, movie.id)}>
                                                            <span class="material-icons">
                                                                check_circle_outline
                                                            </span>
                                                        </button>
                                                        : <button className='list-row-1-btns' onClick={(e) => handleMyListBtn(e, movie.id)}>
                                                            <span class="material-icons">
                                                                add_circle_outline
                                                            </span>
                                                        </button>
                                                }
                                                {
                                                    myLike?.some((likedMovie) => likedMovie.id === movie.id)
                                                        ? <button className='list-row-1-btns' onClick={(e) => handleLikeBtn(e, movie.id)}>
                                                            <span class="material-icons">
                                                                thumb_down_off_alt
                                                            </span>
                                                        </button>
                                                        : <button className='list-row-1-btns' onClick={(e) => handleLikeBtn(e, movie.id)}>
                                                            <span class="material-icons">
                                                                thumb_up_off_alt
                                                            </span>
                                                        </button>
                                                }
                                            </div>
                                            <button className='list-row-1-btns'>
                                                <span class="material-icons">
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
                                                movie.genres.map((genre) => {
                                                    return (
                                                        <div className='list-row-3-genre-div'>{genre}</div>
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
            <div className="browse-car-action">
                <div className='slide-title'>Romance</div>
                <div className="browse-car-list">
                    {
                        romanceMovies?.map((movie) => {
                            return (
                                <div className='list-inner-container'>
                                    <img className='list-img' src={movie.movie_thumbnail} alt='movie' />
                                    <div className='list-description'>
                                        <div className='list-row-1'>
                                            <div className='list-row-1-btn-container'>
                                                <button className='list-row-1-btns'>
                                                    <span class="material-icons">
                                                        play_circle_outline
                                                    </span>
                                                </button>
                                                {
                                                    myList?.some((savedMovie) => savedMovie.id === movie.id)
                                                        ? <button className='list-row-1-btns' onClick={(e) => handleMyListBtn(e, movie.id)}>
                                                            <span class="material-icons">
                                                                check_circle_outline
                                                            </span>
                                                        </button>
                                                        : <button className='list-row-1-btns' onClick={(e) => handleMyListBtn(e, movie.id)}>
                                                            <span class="material-icons">
                                                                add_circle_outline
                                                            </span>
                                                        </button>
                                                }
                                                {
                                                    myLike?.some((likedMovie) => likedMovie.id === movie.id)
                                                        ? <button className='list-row-1-btns' onClick={(e) => handleLikeBtn(e, movie.id)}>
                                                            <span class="material-icons">
                                                                thumb_down_off_alt
                                                            </span>
                                                        </button>
                                                        : <button className='list-row-1-btns' onClick={(e) => handleLikeBtn(e, movie.id)}>
                                                            <span class="material-icons">
                                                                thumb_up_off_alt
                                                            </span>
                                                        </button>
                                                }
                                            </div>
                                            <button className='list-row-1-btns'>
                                                <span class="material-icons">
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
                                                movie.genres.map((genre) => {
                                                    return (
                                                        <div className='list-row-3-genre-div'>{genre}</div>
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
            <div className="browse-car-action">
                <div className='slide-title'>Thrillers</div>
                <div className="browse-car-list">
                    {
                        thrillerMovies?.map((movie) => {
                            return (
                                <div className='list-inner-container'>
                                    <img className='list-img' src={movie.movie_thumbnail} alt='movie' />
                                    <div className='list-description'>
                                        <div className='list-row-1'>
                                            <div className='list-row-1-btn-container'>
                                                <button className='list-row-1-btns'>
                                                    <span class="material-icons">
                                                        play_circle_outline
                                                    </span>
                                                </button>
                                                {
                                                    myList?.some((savedMovie) => savedMovie.id === movie.id)
                                                        ? <button className='list-row-1-btns' onClick={(e) => handleMyListBtn(e, movie.id)}>
                                                            <span class="material-icons">
                                                                check_circle_outline
                                                            </span>
                                                        </button>
                                                        : <button className='list-row-1-btns' onClick={(e) => handleMyListBtn(e, movie.id)}>
                                                            <span class="material-icons">
                                                                add_circle_outline
                                                            </span>
                                                        </button>
                                                }
                                                {
                                                    myLike?.some((likedMovie) => likedMovie.id === movie.id)
                                                        ? <button className='list-row-1-btns' onClick={(e) => handleLikeBtn(e, movie.id)}>
                                                            <span class="material-icons">
                                                                thumb_down_off_alt
                                                            </span>
                                                        </button>
                                                        : <button className='list-row-1-btns' onClick={(e) => handleLikeBtn(e, movie.id)}>
                                                            <span class="material-icons">
                                                                thumb_up_off_alt
                                                            </span>
                                                        </button>
                                                }
                                            </div>
                                            <button className='list-row-1-btns'>
                                                <span class="material-icons">
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
                                                movie.genres.map((genre) => {
                                                    return (
                                                        <div className='list-row-3-genre-div'>{genre}</div>
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
export default BrowsePage;
