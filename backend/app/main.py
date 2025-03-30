"""
Main entry point for the Amplify-Next backend application.
"""
import os
from app import create_app

# Get environment from environment variable or default to development
environment = os.getenv('FLASK_ENV', 'development')

# Create the application instance
app = create_app(environment)

if __name__ == "__main__":
    # Get port from environment variable or use default
    port = int(os.environ.get("PORT", 5000))
    
    # Run the application
    app.run(host="0.0.0.0", port=port, debug=app.config.get('DEBUG', False))