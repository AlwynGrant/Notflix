// --------------------------- Defined Action Types as Constants ---------------------

const GET_MYLIST = 'users/GET_MYLIST';

// --------------------------- Defined Action Creator(s) --------------------------

const getMylist = (mylist) => ({ type: GET_MYLIST, mylist });

// ---------------------------  Defined Thunk(s) --------------------------------

// get current profiles list
export const listMyList= (profileId) => async (dispatch) => {
    const response = await fetch(`/api/profiles/${profileId}/my-list`, {
        method: 'GET'
    });

    if (response.ok) {
        const data = await response.json();
        dispatch(getMylist(data.my_list));
        return response;
    }
}

// ---------------------------  State & Reducer --------------------------------


// movie state
const initialState = [];


// movie reducer
const mylistReducer = (state = initialState, action) => {
    let newState = [ ...state ]

    switch (action.type) {
        case GET_MYLIST:
            return [ ...action.movie ]
        default:
            return state;
    }
}

// Export the reducer
export default mylistReducer;
