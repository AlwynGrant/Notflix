import React, { useState, useEffect } from 'react';
import { BrowserRouter, Route, Switch } from 'react-router-dom';
import { useDispatch } from 'react-redux';
import { authenticate } from './store/session';
import ProtectedRoute from './components/auth/ProtectedRoute';

import KidsVideoPlayerPage from './components/video-player/KidsVideoPlayerPage';
import VideoPlayerPage from './components/video-player/VideoPlayerPage';
import ProfileManagePage from './components/profile/ProfileManagePage.Js';
import ProfileEditPage from './components/profile/ProfileEditPage';
import ProfilePage from './components/profile/ProfilePage';
import BrowseKidsPage from './components/browse-kids/BrowseKidsPage';
import BrowsePage from './components/browse/BrowsePage';
import MyListKidsPage from './components/browse-kids/MyListKidsPage';
import MyListPage from './components/browse/MyListPage';
import SignUpConfForm from './components/auth/SignUpConfForm';
import SignUpValForm from './components/auth/SignUpValForm';
import LoginForm from './components/auth/LoginForm';
import HomePage from './components/home/HomePage';
import NavBar from './components/navbar/NavBar';

import './index.css'

function App() {
  const [loaded, setLoaded] = useState(false);
  const dispatch = useDispatch();

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
          {/* SHARED NAVBAR FOR LOGIN/SIGNUP */}
          <LoginForm />
        </Route>

        <Route path='/sign-up-info' exact={true}>
          {/* SHARED NAVBAR FOR LOGIN/SIGNUP */}
          <SignUpConfForm />
        </Route>

        <Route path='/sign-up-validate' exact={true}>
          {/* SHARED NAVBAR FOR LOGIN/SIGNUP */}
          <SignUpValForm />
        </Route>

        <ProtectedRoute path='/profiles' exact={true}>
          <ProfilePage />
        </ProtectedRoute>

        <ProtectedRoute path='/profiles/manage' exact={true}>
          <ProfileManagePage />
        </ProtectedRoute>

        <ProtectedRoute path='/profiles/:profile_id/edit' exact={true}>
          <ProfileEditPage />
        </ProtectedRoute>

        <ProtectedRoute path='/profiles/:profile_id/my_list' exact={true}>
          <MyListPage />
        </ProtectedRoute>

        <ProtectedRoute path='/profiles/:profile_id/my_kids_list' exact={true}>
          <MyListKidsPage />
        </ProtectedRoute>

        <ProtectedRoute path='/movies' exact={true}>
          <BrowsePage />
        </ProtectedRoute>

        <ProtectedRoute path='/movies/:movieId' exact={true}>
          <VideoPlayerPage />
        </ProtectedRoute>

        <ProtectedRoute path='/movies-kids' exact={true}>
          <BrowseKidsPage />
        </ProtectedRoute>

        <ProtectedRoute path='/movies-kids/:movieId' exact={true}>
          <KidsVideoPlayerPage />
        </ProtectedRoute>

      </Switch>
    </BrowserRouter>
  );
}

export default App;
