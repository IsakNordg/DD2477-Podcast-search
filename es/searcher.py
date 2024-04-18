"""
Define functions for searching data in Elasticsearch.

File: <searcher.py>
Author: <NAME>
Purpose: Search data in Elasticsearch
Description: This file contains functions to search for data in Elasticsearch,
             such as querying documents based on specific criteria.
"""

from es.client import client

class Searcher:

    def __init__(self):
        pass

    @staticmethod
    def print_es_results(results):
        print("Search results: ")
        for hit in results:
            print(hit)

    @staticmethod
    def search_sample(index, query, es=client):
        es_query = {
            "query": {
                "match": {
                    "title": query,
                }
            }
        }
        return es.search(index=index, body=es_query)

    def search_documents(self, index, query, es, etc):
        # Implementation of searching logic
        pass


searcher = Searcher()