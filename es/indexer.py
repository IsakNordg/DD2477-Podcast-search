"""
Define functions for indexing data into Elasticsearch.

File: <indexer.py>
Author: <NAME>
Purpose: Index data into Elasticsearch
Description: This file contains functions to index data into Elasticsearch,
             such as adding documents to the index.
"""

from es.client import ESClient
from es.config.config import configs

class Indexer:

    def __init__(self, client=ESClient()):
        self.es = client.es
        pass

    def refresh_index(self, idx_name):
        """
        Refresh the specified Elasticsearch index to make the indexed docs
        searchable immediately.

        Args:
            idx_name (str): The name of the Elasticsearch index to refresh.

        Returns:
            None
        """
        self.es.indices.refresh(index=idx_name)

    def index_sample(self, idx_name=configs["example_idx_name"]):
        doc_id = "0"
        doc_body = {
            "title": "Hello Elasticsearch",
            "content": "This is a test document for Elasticsearch indexing."
        }
        response = self.es.index(index=idx_name, id=doc_id, body=doc_body)
        self.refresh_index(idx_name)
        return response

    def index_podcasts(self, idx_name=configs["idx_name"], args=None):
        """
        Index podcast data into the specified Elasticsearch index.

        Args:
            idx_name (str): The name of the Elasticsearch index to index the
            data into (specified in configs).
            args (dict): Additional arguments for indexing.

        Returns:
            dict: The response from Elasticsearch indexing operation.
        """
        # TODO(Simon): Implementation of indexing logic

        self.refresh_index(idx_name)
        return self.es.index()