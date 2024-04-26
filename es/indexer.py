"""
Define functions for indexing data into Elasticsearch.

File: <indexer.py>
Author: <NAME>
Purpose: Index data into Elasticsearch
Description: This file contains functions to index data into Elasticsearch,
             such as adding documents to the index.
"""

import os
import json

from es.client import ESClient
from es.config.config import configs


class Indexer:

    def __init__(self, client=ESClient()):
        self.client = client
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
        doc_id = "1"
        doc_body = {
            "title": "Hello World",
            "content": "This is a test surprise for Elasticsearch indexing."
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
                        'limit' (int): The maximum number of podcasts to index into.
                        'force_indexing' (bool): Whether to force the indexing of podcasts.

        Returns:
            boolean: True if successful, False otherwise.
        """
        # TODO(Simon): Implementation of indexing logic

        # Initialize the limit for indexing files
        limit = configs["idx_limit"]
        force_indexing = False

        if isinstance(args, dict):
            if 'limit' in args and isinstance(args['limit'], int):
                limit = args['limit']
            if 'force_indexing' in args and isinstance(args['force_indexing'], bool):
                force_indexing = args['force_indexing']

        # If the index does exist, and force indexing is avoided
        if self.client.index_exists(configs['index_name']) and not force_indexing:
            return True

        print("Indexing podcasts, please wait...")

        # Initialize a counter to count the number of indexed files
        count = 0

        # Traverse through the directory containing podcast transcripts
        for root, dirs, files in os.walk(configs["podcasts_transcripts_path"]):
            for file in files:
                # Process only JSON files
                if file.endswith('.json'):
                    file_path = os.path.join(root, file)
                    try:
                        # Read JSON data from file
                        data = 0
                        with open(file_path, 'r', encoding='utf-8') as f:
                            data = json.load(f)

                        # Process each section of JSON data
                        for part in data['results']:
                            part = part["alternatives"][0]

                            # If transcript and word timestamps are available
                            if 'transcript' in part and "words" in part:
                                transcript = part["transcript"]
                                startTime = part['words'][0]['startTime']
                                endTime = part['words'][-1]['endTime']

                                # Generate a unique document ID
                                doc_id = os.path.basename(file_path) + f"_{startTime}_{endTime}"

                                # Prepare data for indexing
                                indexed_data = {
                                    "transcript": transcript,
                                    "path": file_path,
                                    "startTime": startTime,
                                    "endTime": endTime
                                }

                                # Index the data into Elasticsearch
                                self.es.index(index=idx_name, id=doc_id, body=indexed_data)

                        # Increment the counter
                        count += 1

                        # Limit the number of indexed files (for testing purposes)
                        if count >= limit:
                            return

                    except Exception as e:
                        print(f"Error indexing file '{file_path}': {e}")
                        return False

        # Refresh the Elasticsearch index
        self.refresh_index(idx_name)

        # Return True if indexed successfully
        print("Indexing podcasts, done.")
        return True
