import React from 'react'
import AnalysisForm from '../components/AnalysisForm'

const HomePage: React.FC = () => {
  return (
    <div className="container mx-auto px-4 py-8">
      <h1 className="text-3xl font-bold text-center mb-8">Amplify Next</h1>
      <p className="text-center text-gray-700 mb-8">
        Your advanced SEO analysis tool
      </p>
      
      <AnalysisForm />
    </div>
  )
}

export default HomePage