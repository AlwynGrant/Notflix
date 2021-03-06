import React, { useState, useEffect } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { useHistory, useParams } from 'react-router-dom';
import { listAllMovies } from '../../store/movie'
import { listAllProfiles } from '../../store/profile'
import { addToMyList, listMyList } from '../../store/mylist'
import { listMyLikes, likeUnlikeMovie } from '../../store/mylike'
import MoreInfoModal from '../modals/MovieInfoModal'
import ReactPlayer from 'react-player'


import './browse-styles/mylist.css';
import './browse-styles/browse.css';

function BrowsePage() {
    const { profile_id } = useParams();
    const history = useHistory();
    const dispatch = useDispatch();


    const movies = useSelector(state => state.movies)
    const myList = useSelector(state => state.mylist)
    const myLike = useSelector(state => state.mylike)
    const profiles = useSelector(state => state.profile);
    const currentProfile = profiles?.filter(profile => String(profile.id) === profile_id)[0];

    const actionMovies = movies?.filter(movie => movie.genres[0] === 'Action/Adventure')
    const animeMovies = movies?.filter(movie => movie.genres[0] === 'Anime')
    const comedyMovies = movies?.filter(movie => movie.genres[0] === 'Comedy')
    const docuMovies = movies?.filter(movie => movie.genres[0] === 'Documentary')
    const horrorMovies = movies?.filter(movie => movie.genres[0] === 'Horror')
    const romanceMovies = movies?.filter(movie => movie.genres[0] === 'Romance')
    const thrillerMovies = movies?.filter(movie => movie.genres[0] === 'Thrillers')
    const featuredMovies = movies?.filter(movie => movie.genres[1] === 'Featured')

    const [showMovieModal, setShowMovieModal] = useState(false);

    useEffect(() => {
        dispatch(listAllMovies())
    }, [dispatch])

    useEffect(() => {
        dispatch(listAllProfiles())
        dispatch(listMyList(profile_id))
        dispatch(listMyLikes(profile_id))
    }, [dispatch, currentProfile?.id])

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

    const handleMovieModalClose = (e) => {
        e.preventDefault()
        setShowMovieModal(true)
    }

    return (
        <div className='browse-top-container'>
            <div className='browse-preview-container'>
                <ReactPlayer
                    className='featured-video'
                    playing={true}
                    muted={true}
                    loop={true}
                    url={horrorMovies[2]?.movie_url}
                />
                <div className='browse-preview-feature-info'>
                    <div className='browse-preview-feature-title'>{horrorMovies[2]?.name}</div>
                    <div className='browse-preview-feature-summary'>{horrorMovies[2]?.description}</div>
                    <div className='browse-preview-feature-btn-container'>
                        <button onClick={(e) => handleMovieBtn(e, horrorMovies[2]?.id)} className='browse-preview-play-btn'>Play</button>
                        <button onClick={(e) => handleMovieModalClose(e)} className='browse-preview-more-info-btn'>More Info</button>
                    </div>
                </div>
                <div></div>
                <div></div>
                <div></div>
                <div></div>
                <div></div>
            </div>
            <div className="browse-car-featured">
                <div className='slide-title'>Featured</div>
                    <div className="browse-car-list">
                    {
                        featuredMovies?.map((movie) => {
                            return (
                                <div key={`f-${movie.id}`} className='list-inner-container'>
                                    {/* <ReactPlayer
                                        url={movie.movie_url}
                                        className="react-player"
                                        playing={false}
                                        muted={true}
                                        loop={true}
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
                                            {/* <button onClick={(e) => handleMovieModalClose(e)} className='list-row-1-btns more-info'>
                                                <span className="material-icons">
                                                    arrow_circle_down
                                                </span>
                                            </button> */}
                                        </div>
                                        <div className='list-row-2'>
                                            <div className='list-row-2-rating'>{movie.rating}%</div>
                                            <div className='list-row-2-maturity-rating'>{movie.maturity_rating}</div>
                                        </div>
                                        <div className='list-row-3'>
                                            {
                                                movie.genres.map((genre, i) => {
                                                    return (
                                                        <div key={`gf-${i}`} className='list-row-3-genre-div'>{genre}</div>
                                                    )
                                                })
                                            }
                                        </div>
                                    </div>
                                    {/* {
                                        showMovieModal && (
                                            <MoreInfoModal
                                                show={showMovieModal}
                                                onClose={() => setShowMovieModal(false)}
                                            />
                                        )
                                    } */}
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
                                <div key={`a-${movie.id}`} className='list-inner-container'>
                                    {/* <ReactPlayer
                                        url={movie.movie_url}
                                        className="react-player"
                                        playing={false}
                                        muted={true}
                                        loop={true}
                                        width="400px"
                                    /> */}
                                    <img className='list-img' src={movie.movie_thumbnail} alt='movie' />
                                    <div className='list-description'>
                                        <div className='list-row-1'>
                                            <div className='list-row-1-btn-container'>
                                                <button onClick={(e) => handleMovieBtn(e, movie.id)} className='list-row-1-btns'>
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
                                            {/* <button className='list-row-1-btns more-info'>
                                                <span className="material-icons">
                                                    arrow_circle_down
                                                </span>
                                            </button> */}
                                        </div>
                                        <div className='list-row-2'>
                                            <div className='list-row-2-rating'>{movie.rating}%</div>
                                            <div className='list-row-2-maturity-rating'>{movie.maturity_rating}</div>
                                        </div>
                                        <div className='list-row-3'>
                                            {
                                                movie.genres.map((genre, i) => {
                                                    return (
                                                        <div key={`af-${i}`} className='list-row-3-genre-div'>{genre}</div>
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
                                <div key={`aa-${movie.id}`} className='list-inner-container'>
                                    {/* <ReactPlayer
                                        url={movie.movie_url}
                                        className="react-player"
                                        playing={false}
                                        muted={true}
                                        loop={true}
                                        width="400px"
                                    /> */}
                                    <img className='list-img' src={movie.movie_thumbnail} alt='movie' />
                                    <div className='list-description'>
                                        <div className='list-row-1'>
                                            <div className='list-row-1-btn-container'>
                                                <button onClick={(e) => handleMovieBtn(e, movie.id)} className='list-row-1-btns'>
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
                                            {/* <button className='list-row-1-btns more-info'>
                                                <span className="material-icons">
                                                    arrow_circle_down
                                                </span>
                                            </button> */}
                                        </div>
                                        <div className='list-row-2'>
                                            <div className='list-row-2-rating'>{movie.rating}%</div>
                                            <div className='list-row-2-maturity-rating'>{movie.maturity_rating}</div>
                                        </div>
                                        <div className='list-row-3'>
                                            {
                                                movie.genres.map((genre, i) => {
                                                    return (
                                                        <div key={`aaf-${i}`} className='list-row-3-genre-div'>{genre}</div>
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
                                <div key={`c-${movie.id}`} className='list-inner-container'>
                                    {/* <ReactPlayer
                                        url={movie.movie_url}
                                        className="react-player"
                                        playing={false}
                                        muted={true}
                                        loop={true}
                                        width="400px"
                                    /> */}
                                    <img className='list-img' src={movie.movie_thumbnail} alt='movie' />
                                    <div className='list-description'>
                                        <div className='list-row-1'>
                                            <div className='list-row-1-btn-container'>
                                                <button onClick={(e) => handleMovieBtn(e, movie.id)} className='list-row-1-btns'>
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
                                            {/* <button className='list-row-1-btns more-info'>
                                                <span className="material-icons">
                                                    arrow_circle_down
                                                </span>
                                            </button> */}
                                        </div>
                                        <div className='list-row-2'>
                                            <div className='list-row-2-rating'>{movie.rating}%</div>
                                            <div className='list-row-2-maturity-rating'>{movie.maturity_rating}</div>
                                        </div>
                                        <div className='list-row-3'>
                                            {
                                                movie.genres.map((genre, i) => {
                                                    return (
                                                        <div key={`cf-${i}`} className='list-row-3-genre-div'>{genre}</div>
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
                                <div key={`d-${movie.id}`} className='list-inner-container'>
                                    {/* <ReactPlayer
                                        url={movie.movie_url}
                                        className="react-player"
                                        playing={false}
                                        muted={true}
                                        loop={true}
                                        width="400px"
                                    /> */}
                                    <img className='list-img' src={movie.movie_thumbnail} alt='movie' />
                                    <div className='list-description'>
                                        <div className='list-row-1'>
                                            <div className='list-row-1-btn-container'>
                                                <button onClick={(e) => handleMovieBtn(e, movie.id)} className='list-row-1-btns'>
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
                                            {/* <button className='list-row-1-btns more-info'>
                                                <span className="material-icons">
                                                    arrow_circle_down
                                                </span>
                                            </button> */}
                                        </div>
                                        <div className='list-row-2'>
                                            <div className='list-row-2-rating'>{movie.rating}%</div>
                                            <div className='list-row-2-maturity-rating'>{movie.maturity_rating}</div>
                                        </div>
                                        <div className='list-row-3'>
                                            {
                                                movie.genres.map((genre, i) => {
                                                    return (
                                                        <div key={`df-${i}`} className='list-row-3-genre-div'>{genre}</div>
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
                                <div key={`h-${movie.id}`} className='list-inner-container'>
                                    {/* <ReactPlayer
                                        url={movie.movie_url}
                                        className="react-player"
                                        playing={false}
                                        muted={true}
                                        loop={true}
                                        width="400px"
                                    /> */}
                                    <img className='list-img' src={movie.movie_thumbnail} alt='movie' />
                                    <div className='list-description'>
                                        <div className='list-row-1'>
                                            <div className='list-row-1-btn-container'>
                                                <button onClick={(e) => handleMovieBtn(e, movie.id)} className='list-row-1-btns'>
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
                                            {/* <button className='list-row-1-btns more-info'>
                                                <span className="material-icons">
                                                    arrow_circle_down
                                                </span>
                                            </button> */}
                                        </div>
                                        <div className='list-row-2'>
                                            <div className='list-row-2-rating'>{movie.rating}%</div>
                                            <div className='list-row-2-maturity-rating'>{movie.maturity_rating}</div>
                                        </div>
                                        <div className='list-row-3'>
                                            {
                                                movie.genres.map((genre, i) => {
                                                    return (
                                                        <div key={`hf-${i}`} className='list-row-3-genre-div'>{genre}</div>
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
                                <div key={`r-${movie.id}`} className='list-inner-container'>
                                    {/* <ReactPlayer
                                        url={movie.movie_url}
                                        className="react-player"
                                        playing={false}
                                        muted={true}
                                        loop={true}
                                        width="400px"
                                    /> */}
                                    <img className='list-img' src={movie.movie_thumbnail} alt='movie' />
                                    <div className='list-description'>
                                        <div className='list-row-1'>
                                            <div className='list-row-1-btn-container'>
                                                <button onClick={(e) => handleMovieBtn(e, movie.id)} className='list-row-1-btns'>
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
                                            {/* <button className='list-row-1-btns more-info'>
                                                <span className="material-icons">
                                                    arrow_circle_down
                                                </span>
                                            </button> */}
                                        </div>
                                        <div className='list-row-2'>
                                            <div className='list-row-2-rating'>{movie.rating}%</div>
                                            <div className='list-row-2-maturity-rating'>{movie.maturity_rating}</div>
                                        </div>
                                        <div className='list-row-3'>
                                            {
                                                movie.genres.map((genre, i) => {
                                                    return (
                                                        <div key={`rf-${i}`} className='list-row-3-genre-div'>{genre}</div>
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
                                <div key={`t-${movie.id}`} className='list-inner-container'>
                                    {/* <ReactPlayer
                                        url={movie.movie_url}
                                        className="react-player"
                                        playing={false}
                                        muted={true}
                                        loop={true}
                                        width="400px"
                                    /> */}
                                    <img className='list-img' src={movie.movie_thumbnail} alt='movie' />
                                    <div className='list-description'>
                                        <div className='list-row-1'>
                                            <div className='list-row-1-btn-container'>
                                                <button onClick={(e) => handleMovieBtn(e, movie.id)} className='list-row-1-btns'>
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
                                            {/* <button className='list-row-1-btns more-info'>
                                                <span className="material-icons">
                                                    arrow_circle_down
                                                </span>
                                            </button> */}
                                        </div>
                                        <div className='list-row-2'>
                                            <div className='list-row-2-rating'>{movie.rating}%</div>
                                            <div className='list-row-2-maturity-rating'>{movie.maturity_rating}</div>
                                        </div>
                                        <div className='list-row-3'>
                                            {
                                                movie.genres.map((genre, i) => {
                                                    return (
                                                        <div key={`tf-${i}`} className='list-row-3-genre-div'>{genre}</div>
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
            {
                showMovieModal && (
                    <MoreInfoModal
                        movie={horrorMovies[2]}
                        show={showMovieModal}
                        onClose={() => setShowMovieModal(false)}
                    />
                )
            }
        </div>
    );
}
export default BrowsePage;
