"""
Define Flask routes for the application.

File: <routes.py>
Author: <Wenqi Cao>
Purpose: Define Flask routes
Description: This file defines Flask routes for handling HTTP requests.
             Each route corresponds to a URL endpoint and calls a view
             function to generate an HTTP response.
"""

from flask import Blueprint, request, jsonify, render_template
from .views import search_example

api = Blueprint('api', __name__)

@api.route('/')
def home():
    """
    Render the home page (optional).

    Returns:
        str: Rendered HTML content for the home page.
    """
    return render_template("home.html")


@api.route('/search_sample', methods=['GET', 'POST'])
def search_sample():
    """
    Endpoint to perform search in Elasticsearch.

    Returns:
        Flask.Response: JSON response containing search results.
    """
    query = request.args.get('query', type=str)

    if not query:
        return jsonify({"error": "Query parameter is missing"}), 400

    results = search_example(query)

    return jsonify(results)

@api.route('/search', methods=['GET', 'POST'])
def search():
    pass

@api.errorhandler(404)
def page_not_found(e):
    """
    Handle 404 errors (optional).

    Args:
        e (Exception): The exception object.

    Returns:
        tuple: A tuple containing the error message and status code.
    """
    return 'Page not found', 404