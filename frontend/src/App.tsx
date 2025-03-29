import { Routes, Route } from 'react-router-dom'
import './App.css'
import HomePage from './pages/HomePage'

function App() {
  return (
    <div className="min-h-screen bg-gray-50">
      <Routes>
        <Route path="/" element={<HomePage />} />
        {/* Здесь можно добавить больше маршрутов */}
      </Routes>
    </div>
  )
}

export default App