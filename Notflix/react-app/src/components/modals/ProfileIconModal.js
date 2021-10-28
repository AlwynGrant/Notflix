import React, { useState, useEffect } from 'react';
import './modal.css'

function IconModal(props) {

    const iconArr = [
        'https://kickrbucket.s3.us-west-1.amazonaws.com/1634746455038.jpg',
        'https://kickrbucket.s3.us-west-1.amazonaws.com/1634746460342.png',
        'https://kickrbucket.s3.us-west-1.amazonaws.com/1634746449917.png',
        'https://kickrbucket.s3.us-west-1.amazonaws.com/1634746445926.png',
        'https://kickrbucket.s3.us-west-1.amazonaws.com/1634746441814.png',
        'https://kickrbucket.s3.us-west-1.amazonaws.com/1634746437849.png',
        'https://kickrbucket.s3.us-west-1.amazonaws.com/1634746431496.png',
        'https://kickrbucket.s3.us-west-1.amazonaws.com/1634746427415.png',
        'https://kickrbucket.s3.us-west-1.amazonaws.com/1634746421357.png',
        'https://kickrbucket.s3.us-west-1.amazonaws.com/1634746854870.jpg'
    ]

    if (!props.show) {
        return null
    }

    const handleSelection = (e, icon) => {
        e.preventDefault()
        props.set(icon)
        props.onClose()
    }

    return (
        <div className='icon-modal' onClick={props.onClose}>
            <div className='icon-modal-content' onClick={e => e.stopPropagation()}>
                <div className='icon-modal-header'>
                    <h4 className='icon-modal-title'>Select an Icon</h4>
                </div>
                <div className='icon-modal-body'>
                    {
                        iconArr.map((p_icon, index) => {
                            return <img
                                onClick={(e) => handleSelection(e, p_icon)}
                                className='modal-icon-img'
                                key={index}
                                src={p_icon}
                            />
                        })
                    }
                </div>
            </div>
        </div>
    )
}

export default IconModal;
