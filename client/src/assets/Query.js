import React, { useState, useEffect } from 'react';
import axios from "axios"

function Query(props) {
    const [response, setResponse] = useState(null);
    const [error, setError] = useState(null);

    useEffect(() => {
        console.log('Starting API call');          
        axios({
            method: "GET",
            url: "http://127.0.0.1:5000/hello",
        })
        .then((response) => {
            console.log('API response:', response)
            setResponse(response.data.message);
        })
        .catch((error) => {
            console.error('API error:', error);
            setError("An error occurred.");
        });
    }, []);
    return (
        <div>
            {error ? (
                <div>Error: {error}</div>
            ) : (
                <div>{props.previousStep.metadata.userPreviousMessage}</div>
            )}
        </div>
    );
    
}

export default Query;