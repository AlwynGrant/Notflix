// --------------------------- Defined Action Types as Constants ---------------------

const LIKE_MOVIE = 'users/LIKE_MOVIE';

// --------------------------- Defined Action Creator(s) --------------------------

const likeMovie = (mylikes) => ({ type: LIKE_MOVIE, mylikes });

// ---------------------------  Defined Thunk(s) --------------------------------

// get current profiles list of saved movies
export const listMyLikes = (profileId) => async (dispatch) => {
    const response = await fetch(`/api/profiles/${profileId}/my-likes`, {
        method: 'GET'
    });

    if (response.ok) {
        const data = await response.json();
        dispatch(likeMovie(data.my_likes));
        return response;
    }
}


// like or unlike movie
export const likeUnlikeMovie = (profileId, movieId) => async (dispatch) => {
    const response = await fetch(`/api/profiles/${profileId}/like`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
            movieId
        })
    });

    if (response.ok) {
        const data = await response.json();
        dispatch(likeMovie(data.my_likes));
        return response;
    }
}

// ---------------------------  State & Reducer --------------------------------


// movie state
const initialState = [];


// movie reducer
const myLikeReducer = (state = initialState, action) => {
    let newState = [...state]

    switch (action.type) {
        case LIKE_MOVIE:
            return [ ...action.mylikes ]
        default:
            return state;
    }
}

// Export the reducer
export default myLikeReducer;
