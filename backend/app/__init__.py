# __init__.py

from flask import Flask
from es.client import client
from backend.config.config import configs


# Create Flask application instance
app = Flask(
    import_name=__name__,
    static_folder='../frontend/static',
    template_folder='../frontend/templates'
)

# Set configuration (example: using environment variables)
configs = configs

# Initialize Elasticsearch client
es_client = client

# Import views (routes) to make them accessible
from . import routes