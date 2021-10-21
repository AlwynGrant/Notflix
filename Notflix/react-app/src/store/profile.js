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
    const { username, profile_img, kids } = newProfile;

    const formData = new FormData();
    formData.append("username", username);
    formData.append("profile_img", profile_img);
    formData.append("kids", kids);

    const response = await fetch('/api/profiles/new', {
        method: "POST",
        body: formData
    });

    if (response.ok) {
        const data = await response.json();
        dispatch(addProfile(data));
    };
};

// get one profile
export const listOneProfile = (profileId) => async (dispatch) => {
    const response = await fetch(`/api/profiles/${profileId}`, {
        method: 'GET'
    });

    if (response.ok) {
        const data = await response.json();
        dispatch(getProfile(data));
        return response;
    }
}

// get all sessionUsers profiles
export const listAllProfiles = () => async (dispatch) => {
    const response = await fetch(`/api/profiles`, {
        method: 'GET'
    });

    if (response.ok) {
        const data = await response.json();
        const profiles = data.profiles
        dispatch(getProfiles(profiles));
        return response;
    }
}


// edit profile
export const changeProfile = (profile, profileId) => async (dispatch) => {
    const { username, profile_img, kids } = profile;

    const formData = new FormData();
    formData.append("username", username);
    formData.append("profile_img", profile_img);
    formData.append("kids", kids);

    const response = await fetch(`/api/profiles/${profileId}/edit`, {
        method: "PATCH",
        body: formData
    });

    if (response.ok) {
        const data = await response.json();
        dispatch(editProfile(data));
    };
};

// delete profile
export const removeProfile = (profileId) => async (dispatch) => {
    const response = await fetch(`/api/profiles/${profileId}/delete`, {
        method: 'DELETE'
    });

    if (response.ok) {
        const data = await response.json();
        dispatch(deleteProfile(data));
    }
}


// ---------------------------  State & Reducer --------------------------------


// Image state
const initialState = [];


// profile reducer
const profileReducer = (state = initialState, action) => {
    let newState = [ ...state ]

    switch (action.type) {
        case ADD_PROFILE:
            return [ ...newState, action.profile ]
        case GET_PROFILE:
            return [ action.profile ]
        case GET_PROFILES:
            return [ ...action.profiles ]
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
