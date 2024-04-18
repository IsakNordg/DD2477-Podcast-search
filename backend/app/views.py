"""
Define view functions for the Flask application.

File: <views.py>
Author: <Wenqi Cao>
Purpose: Define view functions
Description: This file contains view functions that handle HTTP requests
             and generate HTTP responses. Each view function corresponds
             to a specific route defined in routes.py.
"""

from es.searcher import searcher
from backend.config.config import configs

def search_podcast(query):
    """
    Perform search in Elasticsearch for books with given query.
    """

    # Perform search using Elasticsearch
    es_results = searcher.search_sample(index=configs["idx_name"], body=query)

    # Extract search results from Elasticsearch response
    results = [{'id': hit['_id'],
                'title': hit['_source']['title'],
                'content': hit['_source']['content']} for hit in es_results['hits']['hits']]

    return results