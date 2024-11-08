import React, { useState } from 'react';
import axios from 'axios';

function App() {
    const [z1Data, setZ1Data] = useState(null);
    const [file, setFile] = useState(null);
    const [opacity, setOpacity] = useState(0.9); // Default opacity
    const [userNumber, setUserNumber] = useState(''); // Store user input number
    const [responseData, setResponseData] = useState(null); // Store server response

    // Function to handle file selection
    const handleFileChange = (event) => {
        setFile(event.target.files[0]);
    };

    // Function to upload the selected file to the Django API
    const uploadFile = async () => {
        if (!file) {
            alert("Please select a file first.");
            return;
        }

        const formData = new FormData();
        formData.append("file", file);

        try {
            const response = await axios.post('http://127.0.0.1:8000/api/upload-file/', formData, {
                headers: {
                    'Content-Type': 'multipart/form-data',
                },
            });
            alert("File uploaded successfully!");
        } catch (error) {
            console.error("Error uploading file:", error);
            alert("Failed to upload file.");
        }
    };

    // Function to fetch data when the "Fetch Data" button is clicked
    const fetchData = async () => {
        if (!userNumber) {
            alert("Please enter a number.");
            return;
        }

        try {
            const response = await axios.post('http://127.0.0.1:8000/api/get-z1-data/', {
                number: userNumber
            });
            setZ1Data(response.data.z1);
            setResponseData(response.data); // Store the response data
        } catch (error) {
            console.error("Error fetching z1 data:", error);
        }
    };

    // Plotly rendering logic when z1Data is available
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

    // Re-render the plot whenever z1Data or opacity changes
    React.useEffect(() => {
        renderPlot();
    }, [z1Data, opacity]);

    return (
        <div style={{ padding: "20px" }}>
            <h1>3D Surface Plot with React and Django</h1>
            
            {/* File Upload Section */}
            <div style={{ marginBottom: "20px" }}>
                <input type="file" accept=".csv" onChange={handleFileChange} />
                <button onClick={uploadFile}>Upload File</button>
            </div>

            {/* User Input Number Section */}
            <div style={{ marginBottom: "20px" }}>
                <label htmlFor="userNumber">Enter a number: </label>
                <input
                    id="userNumber"
                    type="number"
                    value={userNumber}
                    onChange={(e) => setUserNumber(e.target.value)}
                    style={{ marginLeft: "10px", width: "100px" }}
                />
            </div>

            {/* Data Fetch Section */}
            <div style={{ marginBottom: "20px" }}>
                <button onClick={fetchData}>Fetch Data and Plot</button>
            </div>

            {/* Opacity Slider Section */}
            <div style={{ marginBottom: "20px" }}>
                <label htmlFor="opacity-slider">Select Opacity: {opacity}</label>
                <input
                    id="opacity-slider"
                    type="range"
                    min="0.0"
                    max="1.0"
                    step="0.1"
                    value={opacity}
                    onChange={(e) => setOpacity(parseFloat(e.target.value))}
                    style={{ width: "300px", marginLeft: "10px" }}
                />
            </div>

            {/* Server Response */}
            {responseData && (
                <div>
                    <h3>Server Response:</h3>
                    <p>Entered Number: {responseData.number}</p>
                    <p>Data: {JSON.stringify(responseData.z1)}</p>
                </div>
            )}

            {/* Plotly Container */}
            <div id="plotDiv" style={{ width: '100%', height: '500px', marginTop: '20px' }}></div>
        </div>
    );
}

export default App;
