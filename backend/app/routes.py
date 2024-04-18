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
from .views import search_podcast

api = Blueprint('api', __name__)

@api.route('/search')
def search():
    """
    Endpoint to perform search in Elasticsearch.
    """
    query = request.args.get('query', '')

    if not query:
        return jsonify({"error": "Query parameter is missing"}), 400

    results = search_podcast(query)

    print_es_results(results)

    return jsonify(results)

# Define custom error handlers (optional)
@api.errorhandler(404)
def page_not_found(e):
    return 'Page not found', 404

# Define routes
@api.route('/')
def home():
    return render_template("home.html")

def print_es_results(results):
    print("Search results:")
    for hit in results:
        print(hit)