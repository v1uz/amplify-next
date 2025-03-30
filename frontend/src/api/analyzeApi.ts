import axios from 'axios';

const API_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000/api/v1';

export const analyzeUrl = async (data: { url: string }) => {
  const response = await axios.post(`${API_URL}/analysis/analyze`, data);
  return response.data;
};