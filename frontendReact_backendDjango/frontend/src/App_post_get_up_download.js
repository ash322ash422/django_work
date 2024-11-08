import React, { useState } from 'react';
import api from './api';  // Import the axios instance with base URL

function App() {
    const [getData, setGetData] = useState(null);
    const [postData, setPostData] = useState("");
    const [response, setResponse] = useState(null);

    const [file, setFile] = useState(null);
    const [uploadMessage, setUploadMessage] = useState("");
    const [downloadFileName, setDownloadFileName] = useState("");
    const [downloadLink, setDownloadLink] = useState(null);

    // Function to GET data from Django API
    const fetchData = async () => {
        try {
            const result = await api.get('get-data/');
            setGetData(result.data.message);
        } catch (error) {
            console.error("Error fetching data:", error);
        }
    };

    // Function to POST data to Django API
    const sendData = async () => {
        try {
            const result = await api.post('post-data/', { message: postData });
            setResponse(result.data.message);
        } catch (error) {
            console.error("Error posting data:", error);
        }
    };

    // Function to handle file input change
    const handleFileChange = (e) => {
        setFile(e.target.files[0]);
    };

    // Function to handle file upload
    const handleFileUpload = async () => {
        if (!file) {
            alert("Please select a file first");
            return;
        }

        const formData = new FormData();
        formData.append('file', file);

        try {
            const response = await api.post('upload-file/', formData, {
                headers: {
                    'Content-Type': 'multipart/form-data',
                    'Content-Disposition': `attachment; filename=${file.name}`,  // Adding Content-Disposition header
                }
            });
            setUploadMessage(response.data.message);
        } catch (error) {
            console.error("File upload error:", error);
            setUploadMessage("Failed to upload file");
        }
    };

    // Function to handle file download
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
        <div style={{ padding: "20px" }}>
            <h1>React & Django Example with File Upload/Download</h1>

            {/* Section to Fetch Data from Django */}
            <div>
                <button onClick={fetchData}>Fetch Data from Django</button>
                {getData && <p>Response: {getData}</p>}
            </div>

            {/* Section to Send Data to Django */}
            <div style={{ marginTop: "20px" }}>
                <input
                    type="text"
                    value={postData}
                    onChange={(e) => setPostData(e.target.value)}
                    placeholder="Enter data to send"
                />
                <button onClick={sendData}>Send Data to Django</button>
                {response && <p>Response: {response}</p>}
            </div>

            {/* Section for File Upload */}
            <div style={{ marginTop: "20px" }}>
                <h2>Upload File</h2>
                <input type="file" onChange={handleFileChange} />
                <button onClick={handleFileUpload}>Upload File</button>
                {uploadMessage && <p>{uploadMessage}</p>}
            </div>

            {/* Section for File Download */}
            <div style={{ marginTop: "20px" }}>
                <h2>Download File</h2>
                <p>Make sure it is the same name as uploaded file as above.</p>
                <input
                    type="text"
                    value={downloadFileName}
                    onChange={(e) => setDownloadFileName(e.target.value)}
                    placeholder="Enter filename to download"
                />
                <button onClick={handleFileDownload}>Download File</button>
                {downloadLink && (
                    <a href={downloadLink} download={downloadFileName}>
                        Click here to download {downloadFileName}
                    </a>
                )}
            </div>
        </div>
    );
}

export default App;
