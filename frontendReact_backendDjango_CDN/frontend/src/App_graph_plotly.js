import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './App.css'; // Importing the CSS file

function App() {
    const [z1Data, setZ1Data] = useState(null);
    const [file, setFile] = useState(null);
    const [opacity, setOpacity] = useState(0.9);
    const [userNumber, setUserNumber] = useState('');
    const [responseData, setResponseData] = useState(null);

    // File selection handler
    const handleFileChange = (event) => {
        setFile(event.target.files[0]);
    };

    // File upload handler
    const uploadFile = async () => {
        if (!file) {
            alert("Please select a file first.");
            return;
        }

        const formData = new FormData();
        formData.append("file", file);

        try {
            const response = await axios.post('http://127.0.0.1:8000/api/upload-file/', formData, {
                headers: { 'Content-Type': 'multipart/form-data' },
            });
            alert("File uploaded successfully!");
        } catch (error) {
            console.error("Error uploading file:", error);
            alert("Failed to upload file.");
        }
    };

    // Data fetching handler
    const fetchData = async () => {
        if (!userNumber) {
            alert("Please enter a number.");
            return;
        }

        try {
            const response = await axios.post('http://127.0.0.1:8000/api/get-z1-data/', { number: userNumber });
            setZ1Data(response.data.z1);
            setResponseData(response.data);
        } catch (error) {
            console.error("Error fetching z1 data:", error);
        }
    };

    // Plot rendering logic
    const renderPlot = () => {
        if (z1Data && window.Plotly) {
            const z2 = z1Data.map(row => row.map(value => value + 1));
            const z3 = z1Data.map(row => row.map(value => value - 1));

            const data_z1 = { z: z1Data, type: 'surface', name: 'z1' };
            const data_z2 = { z: z2, showscale: false, opacity: opacity, type: 'surface', name: 'z2' };
            const data_z3 = { z: z3, showscale: false, opacity: opacity, type: 'surface', name: 'z3' };

            window.Plotly.newPlot('plotDiv', [data_z1, data_z2, data_z3], { title: '3D Surface Plot' });
        }
    };

    useEffect(() => {
        renderPlot();
    }, [z1Data, opacity]);

    return (
        <div className="container">
            <div className="main-content">
                <h1 className="title">3D Surface Plot with React and Django</h1>

                {/* File Upload Section */}
                <div className="section">
                    <h2 className="section-header">Upload CSV File (z1_data.csv)</h2>
                    <input type="file" accept=".csv" onChange={handleFileChange} className="file-input" />
                    <button onClick={uploadFile} className="button">Upload File</button>
                </div>

                {/* User Number Input Section */}
                <div className="section">
                    <h2 className="section-header">Enter a Number</h2>
                    <input
                        type="number"
                        value={userNumber}
                        onChange={(e) => setUserNumber(e.target.value)}
                        placeholder="Enter number"
                        className="input-field"
                    />
                    <button onClick={fetchData} className="button">Fetch Data and Plot</button>
                </div>

                {/* Opacity Slider Section */}
                <div className="section">
                    <h2 className="section-header">Adjust Plot Opacity</h2>
                    <label htmlFor="opacity-slider" style={{ marginRight: '10px' }}>Opacity: {opacity}</label>
                    <input
                        id="opacity-slider"
                        type="range"
                        min="0.0"
                        max="1.0"
                        step="0.1"
                        value={opacity}
                        onChange={(e) => setOpacity(parseFloat(e.target.value))}
                        className="slider"
                    />
                </div>

                {/* Server Response */}
                {responseData && (
                    <div className="section">
                        <h3 className="section-header">Server Response</h3>
                        <p>Entered Number: {responseData.number}</p>
                        <p>Data: {JSON.stringify(responseData.z1)}</p>
                    </div>
                )}

                {/* Plotly Container */}
                <div id="plotDiv" className="plot-container"></div>
            </div>
        </div>

   );
}


export default App;