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
import os
import json
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
        count = 0
        for root, dirs, files in os.walk("es/data/podcasts-no-audio-13GB/spotify-podcasts-2020/podcasts-transcripts"):
            for file in files:
                if file.endswith('.json'):
                    file_path = os.path.join(root, file)
                    try:
                        data = 0
                        with open(file_path, 'r', encoding='utf-8') as f:
                            data = json.load(f)
                        #For each file go through each json section
                        for part in data['results']:
                            part = part["alternatives"][0]
                            #If transcript remember transcript, startTime of first word and endTime of last word
                            if 'transcript' in part and "words" in part:
                                transcript = part["transcript"]
                                startTime = part['words'][0]['startTime']
                                endTime = part['words'][-1]['endTime']
                                doc_id = os.path.basename(file_path) + f"_{startTime}_{endTime}"
                                indexed_data = {
                                    "transcript": transcript,
                                    "path": file_path,
                                    "startTime": startTime,
                                    "endTime": endTime
                                    }
                                self.es.index(index=idx_name, id=doc_id, body=indexed_data)
                        count += 1
                        if count >= 10:
                            return
                    except Exception as e:
                        print(f"Error indexing file '{file_path}': {e}")

        self.refresh_index(idx_name)
        return