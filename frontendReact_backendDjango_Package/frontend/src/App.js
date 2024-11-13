import React, { useState } from 'react';
import api from './api';
import Plot from 'react-plotly.js';
import './App.css'; // Import the CSS file

function App() {
    const [getData, setGetData] = useState(null);
    const [postData, setPostData] = useState("");
    const [response, setResponse] = useState(null);

    const [file, setFile] = useState(null);
    const [uploadMessage, setUploadMessage] = useState("");
    const [downloadFileName, setDownloadFileName] = useState("");
    const [downloadLink, setDownloadLink] = useState(null);

    // State to store plot data
    const [plotData, setPlotData] = useState(null);

    const fetchData = async () => {
        try {
            const result = await api.get('get-data/');
            setGetData(result.data.message);
            
            // Assuming the fetched data includes x and y coordinates for plot
            const xData = result.data.x || []; // Replace with actual data fields
            const yData = result.data.y || []; // Replace with actual data fields
            setPlotData({ x: xData, y: yData });
        } catch (error) {
            console.error("Error fetching data:", error);
        }
    };

    const sendData = async () => {
        try {
            const result = await api.post('post-data/', { message: postData });
            setResponse(result.data.message);
        } catch (error) {
            console.error("Error posting data:", error);
        }
    };

    const handleFileChange = (e) => {
        setFile(e.target.files[0]);
    };

    const handleFileUpload = async () => {
        if (!file) {
            alert("Please select a file first");
            return;
        }

        const formData = new FormData();
        formData.append('file', file);

        try {
            const response = await api.post('upload-file_1/', formData, {
                headers: {
                    'Content-Type': 'multipart/form-data',
                    'Content-Disposition': `attachment; filename=${file.name}`,
                }
            });
            setUploadMessage(response.data.message);
        } catch (error) {
            console.error("File upload error:", error);
            setUploadMessage("Failed to upload file");
        }
    };

    const handleFileDownload = async () => {
        try {
            const response = await api.get(`download-file/${downloadFileName}/`, {
                responseType: 'blob'
            });
            const url = window.URL.createObjectURL(new Blob([response.data]));
            setDownloadLink(url);
        } catch (error) {
            console.error("File download error:", error);
            alert("Failed to download file");
        }
    };

    return (
        <div className="container">
            <div className="main-content">
                <h1 className="title">React & Django Example with File Upload/Download and Plotly Chart</h1>

                {/* Section to Fetch Data from Django */}
                <div className="section">
                    <button onClick={fetchData} className="button">Fetch Data from Django</button>
                    {getData && <p className="response">Response: {getData}</p>}
                </div>

                {/* Plotly Chart */}
                {plotData && (
                    <div className="section">
                        <h2 className="section-header">Data Visualization</h2>
                        <Plot
                            data={[
                                {
                                    x: plotData.x,
                                    y: plotData.y,
                                    type: 'scatter',
                                    mode: 'lines+markers',
                                    marker: { color: 'blue' },
                                },
                            ]}
                            layout={{ title: 'Plotly Chart from Django Data' }}
                            style={{ width: '100%', height: '400px' }}
                        />
                    </div>
                )}

                {/* Section to Send Data to Django */}
                <div className="section">
                    <h2 className="section-header">Send Data</h2>
                    <input
                        type="text"
                        value={postData}
                        onChange={(e) => setPostData(e.target.value)}
                        placeholder="Enter data to send"
                        className="input"
                    />
                    <button onClick={sendData} className="button">Send Data to Django</button>
                    {response && <p className="response">Response: {response}</p>}
                </div>

                {/* Section for File Upload */}
                <div className="section-box">
                    <h2 className="section-header">Upload File</h2>
                    <input type="file" onChange={handleFileChange} style={{ marginBottom: '10px' }} />
                    <button onClick={handleFileUpload} className="button">Upload File</button>
                    {uploadMessage && <p className="response">{uploadMessage}</p>}
                </div>

                {/* Section for File Download */}
                <div className="section-box" style={{ marginTop: '30px' }}>
                    <h2 className="section-header">Download File</h2>
                    <p>Enter the name of the file to download (same as uploaded above):</p>
                    <input
                        type="text"
                        value={downloadFileName}
                        onChange={(e) => setDownloadFileName(e.target.value)}
                        placeholder="Enter filename to download"
                        className="input"
                    />
                    <button onClick={handleFileDownload} className="button">Download File</button>
                    {downloadLink && (
                        <a href={downloadLink} download={downloadFileName} className="download-link">
                            Click here to download {downloadFileName}
                        </a>
                    )}
                </div>
            </div>
        </div>
    );
}

export default App;
