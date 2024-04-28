"""
Define functions for indexing data into Elasticsearch.

File: <indexer.py>
Author: <NAME>
Purpose: Index data into Elasticsearch
Description: This file contains functions to index data into Elasticsearch,
             such as adding documents to the index.
"""

import os
import csv
import json

from es.client import ESClient
from es.config.config import configs


class Indexer:

    def __init__(self, client=ESClient()):
        self.metadata = self.read_metadata()  # Update metadata (v2.0)
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

    @staticmethod  # (v2.0)
    def read_metadata(file_path=configs["metadata_tsv_path"]):
        data = {}  # Initialize an empty dictionary to store the data
        try:
            with open(file_path, 'r', newline='', encoding='utf-8') as tsv_file:
                tsv_reader = csv.reader(tsv_file, delimiter='\t')  # Create a reader with tab delimiter
                header = next(tsv_reader)  # Read the header row
                for row in tsv_reader:
                    key = row[11]  # Use the first column as the key
                    value = {header[i]: row[i] for i in [1, 2, 3, 5, 7, 8, 9, 10]}
                    data[key] = value  # Store the data in the dictionary
                print("Metadata are loaded successfully.")
            return data
        except Exception as e:
            print(f"Error occurred while reading the TSV file: {e}")
            return None

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

    def index_podcasts(self, idx_name=configs["idx_name"], **kwargs):
        """
        Index podcast data into the specified Elasticsearch index.

        Args:
            idx_name (str): The name of the Elasticsearch index to index the
            data into (specified in configs).
            kwargs: Additional arguments for indexing.
                'limit' (int): The maximum number of podcasts to index into.
                'force_indexing' (bool): Whether to force the indexing of podcasts.

        Returns:
            boolean: True if successful, False otherwise.
        """
        # TODO(Simon): Implementation of indexing logic

        # Extract limit and force_indexing from kwargs if provided
        limit = kwargs.get('limit', configs["idx_limit"])  # Default value is 10 if not provided
        force_indexing = kwargs.get('force_indexing', False)  # Default value is False if not provided

        # If the index does exist, and force indexing is avoided
        if self.client.index_exists(configs['idx_name']) and not force_indexing:
            print("Index loaded from elastic search.")
            return True

        print("Indexing podcasts, please wait...")

        # Initialize a counter to count the number of indexed files
        count = 0

        # Traverse through the directory containing podcast transcripts
        for root, dirs, files in os.walk(configs["podcasts_transcripts_path"]):
            for file in files:
                # Process only JSON files
                if file.endswith('.json'):
                    file_name = file[:-5]
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

                                # Initialize metadata (v2.0)
                                rss_link, title, episode_name = "", "", ""

                                # Integrate metadata (v2.0)
                                if file_name in self.metadata:
                                    episode_name = self.metadata[file_name]['episode_name']
                                    rss_link = self.metadata[file_name]['rss_link']
                                    title = self.metadata[file_name]['show_name']

                                # Prepare data for indexing
                                indexed_data = {
                                    "transcript": transcript,
                                    "path": file_path,
                                    "startTime": startTime,
                                    "endTime": endTime,
                                    # Update metadata (v2.0)
                                    "episode_name": episode_name,
                                    "rss_link": rss_link,
                                    "title": title,
                                }

                                # Index the data into Elasticsearch
                                self.es.index(index=idx_name, id=doc_id, body=indexed_data)

                        # Increment the counter
                        count += 1

                        # Print a progress message
                        if count % 10 == 0:
                            print(f"{count} podcasts indexed.")

                        # Limit the number of indexed files (for testing purposes)
                        if count >= limit:
                            return True

                    except IOError as e:
                        print(f"Error indexing file '{file_path}': {e}")
                        return False
                    except Exception as e:
                        print(f"Unexpected error occurred in: {e} while indexing.")
                        return False

        # Refresh the Elasticsearch index
        self.refresh_index(idx_name)

        # Return True if indexed successfully
        print("Indexing podcasts, done.")
        return True
