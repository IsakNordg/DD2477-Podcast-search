"""
Define functions for searching data in Elasticsearch.

File: <searcher.py>
Author: <NAME>
Purpose: Search data in Elasticsearch
Description: This file contains functions to search for data in Elasticsearch,
             such as querying documents based on specific criteria.
"""

from es.client import ESClient

class Searcher:

    def __init__(self, client=ESClient()):
        self.es = client.es
        pass

    @staticmethod
    def print_es_results(results):
        print("Search results: ")
        for hit in results:
            print(hit)

    def search_sample(self, index, query):
        es_query = {
            "query": {
                "match": {
                    "title": query,
                }
            }
        }
        return self.es.search(index=index, body=es_query)

    def search_podcasts(self, index_name, query, args=None):
        """
        Search for podcasts in the specified index based on the given query.

        Args:
            index (str): The name of the Elasticsearch index to search in.
            query (str): The search query string (NOT the body of search).
            args (dict): Other parameters or options for the search (optional).

        Returns:
            dict: The search results returned by Elasticsearch.
        """
        # TODO(Isak): Implementation of searching logic
        es_query = {
            "query": {
                "match": {
                    "transcript": query
                }
            },
            "_source": ["_id"]  # Return only the document IDs
        }

        # Execute the search query
        try:
            search_results = self.es.search(index=index_name, body=es_query)
            hits = search_results['hits']['hits']
            document_ids = [hit['_id'] for hit in hits]  # Extract document IDs from search results
            return document_ids
        except Exception as e:
            print(f"Error occurred during search: {e}")
            return []

        return relevant_clips