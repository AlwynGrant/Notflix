import React, { useState, useEffect } from 'react';
import { useHistory } from 'react-router-dom'
import { useSelector } from 'react-redux';
import SignUpForm from '../auth/SignUpForm';
import './homepage.css'

import home_kids from './images/home_kids.png'
import mobile_0819 from './images/mobile_0819.jpg'
import tv_pg from './images/tv_bg.png'
import multi_device_bg from './images/multi_device_bg.png'
import down_arrow from './images/down_arrow.png'


function HomePage() {
    const history = useHistory()
    const accountHolder = useSelector(state => state.session.user);

    useEffect(() => {
        if (accountHolder) {
            history.push(`/profiles`)
        }
    })

    const handleGetStarted = () => {
        history.push('/signup')
    }

    return (
       <div className='home-container'>
           <div className='home-sub-container-1'>
               <div className='signup-form-container'>
                   <div className='landing-text-container-top'>
                        <div  className='landing-top-text'>
                            Unlimited movies, TV shows, and more.
                        </div>
                        <div className='landing-bottom-text'>
                            Watch anywhere. Watch anytime.
                        </div>
                   </div>
                    <div className='landing-text-container-bottom'>
                        <div className='under-landing-top-text'>
                            Ready to watch? Click below to register or login to continue.
                        </div>
                        <div className='under-landing-bottom-text'>
                            <button id='get-started' onClick={() => handleGetStarted()} className='landing-signup-button'>Get Started</button>
                        </div>
                   </div>
               </div>
           </div>

           <div className='home-sub-container-2'>
                <div className='container-2-text'>
                    <div className='sub-container-2-text'>
                        <div className='sub-container-2-top-text'>
                            Enjoy on your TV.
                        </div>
                        <div className='sub-container-2-bottom-text'>
                            Watch on Smart TVs, Playstation, Xbox, Chromecast, Apple TV, Blu-ray players, and more.
                        </div>
                    </div>
                </div>
                <div className='sub-container-2-img'>
                    <img className='container-2-img' src={tv_pg} alt='container-2-img'/>
                    <div className='container-2-inner-gif'></div>
                </div>
           </div>

            <div className='home-sub-container-3'>
                <div className='sub-container-3-img'>
                    <img className='container-3-img' src={mobile_0819} alt='container-3-img' />
                </div>
                <div className='container-3-text'>
                    <div className='sub-container-3-text'>
                        <div className='sub-container-3-top-text'>
                            Save favorited movies to your personalized list.
                        </div>
                        <div className='sub-container-3-bottom-text'>
                            Save your favorites easily and always have something to watch.
                        </div>
                    </div>
                </div>
            </div>

           <div className='home-sub-container-4'>
                <div className='container-4-text'>
                    <div className='sub-container-4-text'>
                        <div className='sub-container-4-top-text'>
                            Watch everywhere.
                        </div>
                        <div className='sub-container-4-bottom-text'>
                            Stream unlimited movies on your phone, tablet, laptop, and TV without paying.
                        </div>
                    </div>
                </div>
                    <div className='sub-container-4-img'>
                    <img className='container-4-img' src={multi_device_bg} alt='container-4-img' />
                    <div className='container-4-inner-gif'></div>
                    </div>
           </div>

            <div className='home-sub-container-5'>
                <div className='sub-container-5-img'>
                    <img className='container-5-img' src={home_kids} alt='container-5-img' />
                </div>
                <div className='container-5-text'>
                    <div className='sub-container-5-text'>
                        <div className='sub-container-5-top-text'>
                            Create profiles for kids.
                        </div>
                        <div className='sub-container-5-bottom-text'>
                            Send kids on adventures with their favorite characters in a space made just for them—free!.
                        </div>
                    </div>
                </div>
            </div>

            <div className='home-sub-container-6'>
                <div className='sub-inner-container-6'>
                    <div className='sub-container-6-FAQ'>
                        Frequently Asked Questions
                    </div>
                    <div className='sub-container-6-questions'>
                        <div className='q-1'>
                            <div className='q-1-q'>What is Notflix?</div>
                            <div className='a-1'>
                                <div>Well, it's definitely NOT Netflix! Notflix is however a direct clone of Netflix, showcasing trailers from some of the most popular movies.</div>
                            </div>
                            <button className='q-1-btn'>
                                <img className='q-1-img' src={down_arrow} />
                            </button>
                        </div>
                        <div className='q-2'>
                            <div className='q-2-q'>Where can I watch?</div>
                            <div className='a-2'>
                                <div>You can navigate to the <a href='#get-started'>Get Started</a> button on this page to create an account, or log in to choose a profile. After you have either created and/or chosen a profile, you will be redirected the browse feed, where you can choose from a selection of trailers.</div>
                            </div>
                            <button className='q-1-btn'>
                                <img className='q-1-img' src={down_arrow} />
                            </button>
                        </div>
                        <div className='q-3'>
                            <div className='q-3-q'>What can I watch on Notflix?</div>
                            <div className='a-3'>
                                <div>You can't watch full length movies. But you can watch trailers from popular movies from genres ranging from Action & adventure, Anime, Comedy, Documentaries, Horror, Romance, and Thriller.</div>
                            </div>
                            <button className='q-1-btn'>
                                <img className='q-1-img' src={down_arrow} />
                            </button>
                        </div>
                        <div className='q-4'>
                            <div className='q-4-q'>Is Notflix good for kids?</div>
                            <div className='a-4'>
                                <div>Notflix has a small selection of kids movie trailers to watch. For the future, Notflix will incorperate a kids only browse feed!</div>
                            </div>
                            <button className='q-1-btn'>
                                <img className='q-1-img' src={down_arrow} />
                            </button>
                        </div>
                        <div className='q-5'>
                            <div className='q-5-q'>Who developed Notflix?</div>
                            <div className='a-5'>
                                <div>Notflix was developed by me, Alwyn Grant! If you're interested in learning more, please checkout my <a target="_blank" rel="noreferrer" href={'https://github.com/AlwynGrant'}>Github</a> & <a target="_blank" rel="noreferrer" href={'https://www.linkedin.com/in/alwyn-grant-928b091a3/'}>LinkdIn</a> profiles! </div>
                            </div>
                            <button className='q-1-btn'>
                                <img className='q-1-img' src={down_arrow} />
                            </button>
                        </div>
                        <div className='q-6'>
                            <div className='q-6-q'>How can I contact the developer?</div>
                            <div className='a-6'>
                                <div>If you'd like to reach out, you can email me at marzgrant@gmail.com.</div>
                            </div>
                            <button className='q-1-btn'>
                                <img className='q-1-img' src={down_arrow} />
                            </button>
                        </div>
                    </div>
                    <div className='landing-text-container-bottom'>
                        <div className='under-landing-top-text'>
                            Ready to watch? Enter your email to create or restart your membership.
                        </div>
                        <div className='under-landing-bottom-text'>
                            <button onClick={() => handleGetStarted()} className='landing-signup-button'>Get Started</button>
                        </div>
                    </div>
                </div>
            </div>
       </div>
    );
}

export default HomePage;
