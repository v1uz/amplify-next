import axios from 'axios'

// Базовый URL API
const API_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000/api/v1'

// Создаем экземпляр Axios с настройками
export const apiClient = axios.create({
  baseURL: API_URL,
  headers: {
    'Content-Type': 'application/json',
  },
})

// Добавляем перехватчики ответов для обработки ошибок
apiClient.interceptors.response.use(
  (response) => response,
  (error) => {
    // Здесь можно глобально обрабатывать ошибки API
    console.error('API Error:', error.response?.data || error.message)
    return Promise.reject(error)
  }
)