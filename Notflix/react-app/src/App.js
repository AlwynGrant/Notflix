import React, { useState, useEffect } from 'react';
import { BrowserRouter, Route, Switch } from 'react-router-dom';
import { useDispatch, useSelector } from 'react-redux';
import { authenticate } from './store/session';
import ProtectedRoute from './components/auth/ProtectedRoute';

// import KidsVideoPlayerPage from './components/video-player/KidsVideoPlayerPage';
// import BrowseKidsPage from './components/browse-kids/BrowseKidsPage';
import VideoPlayerPage from './components/video-player/VideoPlayerPage';
import ProfileManagePage from './components/profile/ProfileManagePage.js';
import ProfileEditPage from './components/profile/ProfileEditPage';
import ProfileNewPage from './components/profile/ProfileNewPage';
import ProfilePage from './components/profile/ProfilePage';
import BrowsePage from './components/browse/BrowsePage';
// import MyListKidsPage from './components/browse-kids/MyListKidsPage';
import MyListPage from './components/browse/MyListPage';
import SignUpForm from './components/auth/SignUpForm';
import LoginForm from './components/auth/LoginForm';
import HomePage from './components/home/HomePage';
import NavBarProfile from './components/navbar/NavBarProfile';
import NavBarMovies from './components/navbar/NavBarMovies';
import NavBarAuth from './components/navbar/NavBarAuth';
import NavBar from './components/navbar/NavBar';

import './index.css'

function App() {
  const [loaded, setLoaded] = useState(false);
  const dispatch = useDispatch();

  const accountHolder = useSelector(state => state.session.user);

  useEffect(() => {
    (async() => {
      await dispatch(authenticate());
      setLoaded(true);
    })();
  }, [dispatch]);

  if (!loaded) {
    return null;
  }

  return (
    <BrowserRouter>
      <Switch>
        <Route path='/' exact={true} >
          <NavBar />
          <HomePage />
        </Route>

        <Route path='/login' exact={true}>
          <NavBarAuth />
          <LoginForm />
        </Route>

        <Route path='/signup' exact={true}>
          <NavBarAuth />
          <SignUpForm />
        </Route>

        <ProtectedRoute path='/profiles' exact={true}>
          <NavBarProfile />
          <ProfilePage />
        </ProtectedRoute>

        <ProtectedRoute path='/profiles/new' exact={true}>
          <NavBarProfile />
          <ProfileNewPage />
        </ProtectedRoute>

        <ProtectedRoute path='/profiles/manage' exact={true}>
          <NavBarProfile />
          <ProfileManagePage />
        </ProtectedRoute>

        <ProtectedRoute path='/profiles/:profile_id/edit' exact={true}>
          <NavBarProfile />
          <ProfileEditPage />
        </ProtectedRoute>

        <ProtectedRoute path='/profiles/:profile_id/my-list' exact={true}>
          <NavBarMovies />
          <MyListPage />
        </ProtectedRoute>

        {/* <ProtectedRoute path='/profiles/:profile_id/my_kids_list' exact={true}>
          <NavBarMovies />
          <MyListKidsPage />
        </ProtectedRoute> */}

        <ProtectedRoute path='/profiles/:profile_id/movies' exact={true}>
          <NavBarMovies />
          <BrowsePage />
        </ProtectedRoute>

        <ProtectedRoute path='/profiles/:profile_id/movies/:movieId' exact={true}>
          <VideoPlayerPage />
        </ProtectedRoute>

        {/* <ProtectedRoute path='/movies-kids' exact={true}>
          <BrowseKidsPage />
        </ProtectedRoute>

        <ProtectedRoute path='/movies-kids/:movieId' exact={true}>
          <KidsVideoPlayerPage />
        </ProtectedRoute> */}

      </Switch>
    </BrowserRouter>
  );
}

export default App;
