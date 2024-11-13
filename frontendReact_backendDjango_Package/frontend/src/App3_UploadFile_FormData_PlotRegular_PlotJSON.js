import React, { useState, useEffect } from 'react';
import api from './api';
import Plot from 'react-plotly.js';
import './App.css'; // Importing the CSS file for styling

function App() {
    const [z1Data, setZ1Data] = useState(null);
    const [opacity, setOpacity] = useState(0.9);
    const [number1, setNumber1] = useState('');
    const [number2, setNumber2] = useState('');
    const [number3, setNumber3] = useState('');
    const [selectedOption, setSelectedOption] = useState('option1');
    const [radioValue, setRadioValue] = useState('radio1');
    const [checkboxValue, setCheckboxValue] = useState(false);
    const [responseData, setResponseData] = useState(null);
    const [file, setFile] = useState(null);
    const [uploadMessage, setUploadMessage] = useState('');
    const [figureData, setFigureData] = useState(null);

    const handleFileChange = (e) => {
        setFile(e.target.files[0]);
    };

    const handleFileUpload = async () => {
        if (!file) {
            alert('Please select a file first');
            return;
        }

        const formData = new FormData();
        formData.append('file', file);

        try {
            const response = await api.post('upload-file/', formData, {
                headers: { 'Content-Type': 'multipart/form-data' }
            });
            setUploadMessage('File uploaded successfully!');
        } catch (error) {
            console.error('Error uploading file:', error);
            setUploadMessage('Failed to upload file');
        }
    };

    const handleSubmit = async (e) => {
        e.preventDefault();

        const formData = {
            number1,
            number2,
            number3,
            selectedOption,
            radioValue,
            checkboxValue
        };

        try {
            const response = await api.post('plot/', formData);
            console.log("Response data:", response.data); // Check if data is received
            setZ1Data(response.data.z1);
            setResponseData(response.data);
        } catch (error) {
            console.error('Error submitting form:', error);
        }
    };

    // Prepare data for Plotly surface plot using `react-plotly.js`
    const preparePlotData = () => {
        if (!z1Data) return null;
        
        const z2 = z1Data.map(row => row.map(value => value + 1));
        const z3 = z1Data.map(row => row.map(value => value - 1));
        
        return [
            { z: z1Data, type: 'surface', name: 'z1' },
            { z: z2, showscale: false, opacity: opacity, type: 'surface', name: 'z2' },
            { z: z3, showscale: false, opacity: opacity, type: 'surface', name: 'z3' },
        ];
    };

    // Function to fetch plot data from backend on button click
    const fetchPlotData = () => {
        fetch('http://localhost:8000/api/plot-data/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        })
        .then(response => response.json()) //The response object is converted from JSON format to a JavaScript objec
        .then(data => setFigureData(data))
        .catch(error => console.error("Error fetching figure data:", error));
    };

    const plotData = preparePlotData();

    return (
        <div className="app-container">
            <h1>React Form with CSV Upload, User Input, and Plotly Graph</h1>

            <div className="upload-section">
                <input type="file" accept=".csv" onChange={handleFileChange} />
                <button onClick={handleFileUpload}>Upload CSV (z1_data.csv)</button>
                {uploadMessage && <p className="upload-message">{uploadMessage}</p>}
            </div>

            <form onSubmit={handleSubmit} className="form-container">
                <div className="form-group">
                    <label>Number 1:</label>
                    <input type="number" value={number1} onChange={(e) => setNumber1(e.target.value)} />
                </div>
                <div className="form-group">
                    <label>Number 2:</label>
                    <input type="number" value={number2} onChange={(e) => setNumber2(e.target.value)} />
                </div>
                <div className="form-group">
                    <label>Number 3:</label>
                    <input type="number" value={number3} onChange={(e) => setNumber3(e.target.value)} />
                </div>

                <div className="form-group">
                    <label>Select Option:</label>
                    <select value={selectedOption} onChange={(e) => setSelectedOption(e.target.value)}>
                        <option value="option1">Option 1</option>
                        <option value="option2">Option 2</option>
                        <option value="option3">Option 3</option>
                    </select>
                </div>

                <div className="form-group">
                    <label>Radio Option:</label>
                    <div className="radio-group">
                        <input type="radio" name="radio" value="radio1" checked={radioValue === 'radio1'} onChange={(e) => setRadioValue(e.target.value)} /> Radio 1
                        <input type="radio" name="radio" value="radio2" checked={radioValue === 'radio2'} onChange={(e) => setRadioValue(e.target.value)} /> Radio 2
                    </div>
                </div>

                <div className="form-group">
                    <label>
                        <input type="checkbox" checked={checkboxValue} onChange={(e) => setCheckboxValue(e.target.checked)} /> Checkbox
                    </label>
                </div>

                <button type="submit" className="submit-button">Submit Form and Plot</button>
            </form>

            {responseData && (
                <div className="response-container">
                    <h2>Response from Server:</h2>
                    <pre>{JSON.stringify(responseData, null, 2)}</pre>
                </div>
            )}

            {/* Opacity Slider Section */}
            <div className="section">
                <h2 className="section-header">Adjust Plot Opacity</h2>
                <label htmlFor="opacity-slider" style={{ marginRight: '10px' }}>Opacity: {opacity}</label>
                <input id="opacity-slider" type="range" min="0.0" max="1.0" step="0.1" value={opacity}
                    onChange={(e) => setOpacity(parseFloat(e.target.value))}
                    className="slider"
                />
            </div>

            {/* Plotly Graph */}
            <div>
            {plotData ? (
                <Plot
                    data={plotData}
                    layout={{
                        title: '3D Surface Plot',
                        scene: { zaxis: { title: 'Z-axis' } },
                    }}
                    className="plot-container"
                    style={{ width: '100%', height: '500px' }}  // Ensure a fixed height
                />
            ) : ( <p>Waiting for data...</p> )
            }
            </div>

            <div>
                <button onClick={fetchPlotData}>Submit and Plot</button>
                {figureData ? (
                    <Plot
                    data={figureData.data}
                    layout={figureData.layout}
                    style={{ width: "100%", height: "100%" }}
                    config={{ responsive: true }}
                    />
                ) : ( 
                      <div>Click "Submit and Plot" to load the figure.</div> 
                    )
                }
            </div>

        </div>
    );
}

export default App;
