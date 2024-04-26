"""
Define view functions for the Flask application.

File: <views.py>
Author: <Wenqi Cao>
Purpose: Define view functions
Description: This file contains view functions that handle HTTP requests
             and generate HTTP responses. Each view function corresponds
             to a specific route defined in routes.py.
"""

from es.searcher import Searcher
from backend.config.config import configs

searcher = Searcher()

def search_example(query, method=0):
    """
    Perform search in Elasticsearch for books with given query.
    """
    print("New search query:", query)

    # Perform search using Elasticsearch
    es_results = searcher.search_sample(index=configs["example_idx_name"], query=query)

    # Extract search results from Elasticsearch response
    results = [{'id': hit['_id'], 'score': hit['_score'], 'title': hit['_source']['title'],
                'content': hit['_source']['content']} for hit in es_results['hits']['hits']]

    print("Method: " + str(method))
    print("Result: " + str(results))
    return results

def search_podcast(query, method=0, sec=120):
    es_results = searcher.search_podcasts(index=configs["idx_name"],
                                          query=query,
                                          seconds=sec,
                                          metahod=method,
                                          )

    results = [{'id': hit['doc_id'], 'score': hit['score'], 'title': hit['doc_id'],
                'start@': hit['startTime'], 'end@': hit['endTime'],
                'content': hit['transcript']} for hit in es_results]

    return results