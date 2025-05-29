import axios from 'axios';

const api = axios.create({
  baseURL: 'http://localhost:8000',
});

export const fetchPlayer = (id) => api.get(`/players/${id}`);
export const getInventory = (id) => api.get(`/inventory/${id}`);
