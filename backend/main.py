# main.py

from flask import Flask
from app.routes import api

# Create Flask application instance
app = Flask(__name__)

# Register the Blueprint with the Flask application
app.register_blueprint(api)

# Define other routes or configurations as needed

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)