// src/api/api.js
import axios from 'axios';

const api = axios.create({
    baseURL: "/api",  // Assuming you will use a proxy to point to the Django backend
});

export default api;
