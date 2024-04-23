# main.py

from backend.app import webapp


# Run the Flask application
if __name__ == '__main__':
    webapp.run(host="0.0.0.0", debug=True)