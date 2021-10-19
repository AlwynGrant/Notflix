import React, { useState, useEffect } from 'react';
import './homepage.css'

function HomePage() {

    return (
       <div className='home-container'>
           <div className='home-sub-container-1'>
               <div className='signup-form-container'>
                   <div className='landing-text-container-top'>
                        <div  className='landing-top-text'>
                            Unlimited movies, TV shows, and more.
                        </div>
                        <div className='landing-bottom-text'>
                            Watch anywhere. Cancel anytime.
                        </div>
                   </div>
                    <div className='landing-text-container-bottom'>
                        <div className='under-landing-top-text'>
                            Ready to watch? Enter your email to create or restart your membership.
                        </div>
                        <div className='under-landing-bottom-text'>
                            <input className='landing-signup-input' placeholder='Email address'></input>
                            <button className='landing-signup-button'>Get Started</button>
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
                <div className='sub-container-3-img'>
                    <img src={null} alt='container-3-img'/>
                </div>
           </div>

            <div className='home-sub-container-3'>
                <div className='sub-container-3-img'>
                    <img src={null} alt='container-3-img' />
                </div>
                <div className='container-3-text'>
                    <div className='sub-container-3-text'>
                        <div className='sub-container-3-top-text'>
                            Download your shows to watch offline.
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
                            Stream unlimited movies and TV shows on your phone, tablet, laptop, and TV without paying more.
                        </div>
                    </div>
                    <div className='sub-container-4-img'>
                        <img src={null} alt='container-4-img' />
                    </div>
                </div>
           </div>

            <div className='home-sub-container-5'>
                <div className='sub-container-5-img'>
                    <img src={null} alt='container-5-img' />
                </div>
                <div className='container-5-text'>
                    <div className='sub-container-5-text'>
                        <div className='sub-container-5-top-text'>
                            Create profiles for kids.
                        </div>
                        <div className='sub-container-5-bottom-text'>
                            Send kids on adventures with their favorite characters in a space made just for them—free with your membership.
                        </div>
                    </div>
                </div>
            </div>

            <div className='home-sub-container-6'>
                <div className='sub-container-6-FAQ'>
                    Frequently Asked Questions
                </div>
                <div className='sub-container-6-questions'>
                    <div><div>What is Notflix?</div></div>
                    <div><div>Where can I watch?</div></div>
                    <div><div>What can I watch on Notflix?</div></div>
                    <div><div>Is Notflix good for kids?</div></div>
                    <div><div>Who developed Notflix?</div></div>
                    <div><div>How can I contact the developer?</div></div>
                </div>
                <div className='landing-text-container-bottom'>
                    <div className='under-landing-top-text'>
                        Ready to watch? Enter your email to create or restart your membership.
                    </div>
                    <div className='under-landing-bottom-text'>
                        <input className='landing-signup-input' placeholder='Email address'></input>
                        <button className='landing-signup-button'>Get Started</button>
                    </div>
                </div>
            </div>
       </div>
    );
}

export default HomePage;
