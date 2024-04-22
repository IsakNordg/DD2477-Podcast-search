# development.py
# A sample file for development (modified from initial main.py)

from es.client import ESClient
from es.indexer import Indexer
from es.searcher import Searcher
from es.config.config import configs

client = ESClient()  # Create an instance of the Elasticsearch client.

#Only index "podcast" json files once so we can test search!
index_exists = client.Get_es().indices.exists(index="podcast")
#Comment this to override
#index_exists = False
if not index_exists:
    print("Indexing...")
    indexer = Indexer(client)  # Create an instance of the Indexer class with the Elasticsearch client.
    indexer.index_podcasts("podcast")

searcher = Searcher(client)  # Create an instance of the Searcher class with the Elasticsearch client.
#First arg is the name of index, second is the query we want to search for, third seconds
seconds = 35
segments = searcher.search_podcasts("podcast", "hi", seconds)
if segments:
    print(f"Found {len(segments)} relevant {seconds}-second segments:")
    for segment in segments:
        print(f"Document ID: {segment['doc_id']}")
        print(f"Path: {segment['path']}")
        print(f"Transcript: {segment['transcript']}")
        print(f"Start Time: {segment['startTime']}, End Time: {segment['endTime']}")
        print("=" * 50)
else:
    print("No relevant segments found for the query.")
