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

    def search_podcasts(self, index_name, query, seconds = 30, args=None):
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
        try:
            #Query
            es_query = {
                "query": {
                    "match": {
                        "transcript": query
                    }
                }
            }

            response = self.es.search(index=index_name, body=es_query)

            #Retrieve relevant segments
            segments = []
            for hit in response['hits']['hits']:
                segment = {
                    "doc_id": hit['_id'],
                    "transcript": hit['_source']['transcript'],
                    "startTime": hit['_source']['startTime'],
                    "endTime": hit['_source']['endTime']
                }
                segments.append(segment)

            #Filter segments based on desired duration (seconds)
            filtered_segments = []
            for segment in segments:
                start_seconds = float(segment['startTime'][:-1])  #Convert "X.XXXs" to seconds
                end_seconds = float(segment['endTime'][:-1])
                duration_seconds = end_seconds - start_seconds
                if duration_seconds <= seconds:
                    filtered_segments.append(segment)

            return filtered_segments

        except Exception as e:
            print(f"Error searching for segments: {e}")
            return []