import axios from 'axios';

// Create an instance of axios with the base URL set to the API endpoint from the .env file
const api = axios.create({
    baseURL: process.env.REACT_APP_API_URL,
});

export default api;
