import React, { useState, useEffect } from 'react';
import './browse-styles/browse.css'

function BrowsePage() {

    return (
        <>
        <div className='browse-preview-container'>
            <div className='browse-preview-feature-info'>
                <div className='browse-preview-feature-title'>FEATURED_TITLE_DIV</div>
                <div className='browse-preview-feature-summary'>FEATURED_SUMMARY_DIV</div>
                <div className='browse-preview-feature-btn-container'>
                    <button className='browse-preview-play-btn'>PLAY_BUTTON</button>
                    <button className='browse-preview-more-info-btn'>MORE_INFO_BUTTON</button>
                </div>
            </div>
            <h1>FIRST_FEATURED_PREVIEW_CONTAINER</h1>
        </div>
        <div>TEST</div>
        </>
    );
}
export default BrowsePage;
