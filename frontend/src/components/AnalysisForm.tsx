import React, { useState } from 'react'

const AnalysisForm: React.FC = () => {
  const [url, setUrl] = useState('')
  const [loading, setLoading] = useState(false)
  
  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault()
    setLoading(true)
    
    try {
      // Здесь будет логика отправки запроса к API
      console.log('Analyzing URL:', url)
      // Имитация задержки API
      await new Promise(resolve => setTimeout(resolve, 1000))
    } catch (error) {
      console.error('Error analyzing URL:', error)
    } finally {
      setLoading(false)
    }
  }
  
  return (
    <div className="max-w-md mx-auto bg-white rounded-lg shadow-md p-6">
      <h2 className="text-xl font-semibold mb-4">Analyze Website</h2>
      <form onSubmit={handleSubmit}>
        <div className="mb-4">
          <label htmlFor="url" className="block text-sm font-medium text-gray-700 mb-1">
            Website URL
          </label>
          <input
            type="url"
            id="url"
            value={url}
            onChange={(e) => setUrl(e.target.value)}
            placeholder="https://example.com"
            className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
            required
          />
        </div>
        <button
          type="submit"
          disabled={loading}
          className="w-full bg-blue-500 text-white py-2 px-4 rounded-md hover:bg-blue-600 focus:outline-none focus:ring-2 focus:ring-blue-700 focus:ring-opacity-50 disabled:bg-blue-300"
        >
          {loading ? 'Analyzing...' : 'Analyze'}
        </button>
      </form>
    </div>
  )
}

export default AnalysisForm