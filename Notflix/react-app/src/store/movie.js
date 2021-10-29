// --------------------------- Defined Action Types as Constants ---------------------

const GET_MOVIE = 'users/GET_MOVIE';
const GET_MOVIES = 'users/GET_MOVIES';

// --------------------------- Defined Action Creator(s) --------------------------

const getMovie = (movie) => ({ type: GET_MOVIE, movie });
const getMovies = (movies) => ({ type: GET_MOVIES, movies });

// ---------------------------  Defined Thunk(s) --------------------------------

// get one movie
export const listOneMovie = (movieId) => async (dispatch) => {
    const response = await fetch(`/api/movies/${movieId}`, {
        method: 'GET'
    });

    if (response.ok) {
        const data = await response.json();
        dispatch(getMovie(data));
        return response;
    }
}

// get all movies
export const listAllMovies = () => async (dispatch) => {
    const response = await fetch(`/api/movies`, {
        method: 'GET'
    });

    if (response.ok) {
        const data = await response.json();
        dispatch(getMovies(data.movies));
        return response;
    }
}

// ---------------------------  State & Reducer --------------------------------


// movie state
const initialState = [];


// movie reducer
const movieReducer = (state = initialState, action) => {
    // let newState = [ ...state ]

    switch (action.type) {
        case GET_MOVIE:
            return [ action.movie ]
        case GET_MOVIES:
            return [ ...action.movies ]
        default:
            return state;
    }
}

// Export the reducer
export default movieReducer;
