import React, { useState, useEffect } from 'react';
import api from './api';
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
            const response = await api.post('submit-form/', formData);
            setZ1Data(response.data.z1);
            setResponseData(response.data);
        } catch (error) {
            console.error('Error submitting form:', error);
        }
    };

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
        <div className="app-container">
            <h1>React Form with CSV upload, user input and Plotly graph</h1>

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


            <div id="plotDiv" className="plot-container"></div>
        </div>
    );
}

export default App;
