// --------------------------- Defined Action Types as Constants ---------------------

const ADD_PROFILE = 'users/NEW_PROFILE';
const GET_PROFILE = 'users/GET_PROFILE';
const GET_PROFILES = 'users/GET_PROFILES';
const EDIT_PROFILE = 'users/EDIT_PROFILE';
const DELETE_PROFILE = 'users/DELETE_PROFILE';


// --------------------------- Defined Action Creator(s) --------------------------

const addProfile = (profile) => ({ type: ADD_PROFILE, profile });
const getProfile = (profile) => ({ type: GET_PROFILE, profile });
const getProfiles = (profiles) => ({ type: GET_PROFILES, profiles });
const editProfile = (profile) => ({ type: EDIT_PROFILE, profile });
const deleteProfile = (profile) => ({ type: DELETE_PROFILE, profile });

// ---------------------------  Defined Thunk(s) --------------------------------

// create profile
export const createProfile = (newProfile) => async (dispatch) => {

};

// get one profile
export const listOneProfile = (profileId) => async (dispatch) => {

}

// get all sessionUsers profiles
export const listAllProfiles = () => async (dispatch) => {

}


// edit profile
export const changeProfile = (profile, profileId) => async (dispatch) => {

};

// delete profile
export const removeProfile = (profileId) => async (dispatch) => {

}


// ---------------------------  State & Reducer --------------------------------


// Image state
const initialState = [];


// profile reducer
const profileReducer = (state = initialState, action) => {
    let newState = [...state]

    switch (action.type) {
        case ADD_PROFILE:
            return [...newState, action.profile ]
        case GET_PROFILE:
            return [action.profile ]
        case GET_PROFILE:
            return [...action.profiles ]
        case EDIT_PROFILE:
            return newState
        case DELETE_PROFILE:
            return newState.filter((el) => action.profile.id !== el.id)
        default:
            return state;
    }
}
// Export the reducer
export default profileReducer;
