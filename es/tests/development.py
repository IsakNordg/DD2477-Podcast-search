# development.py
# A sample file for development (modified from initial main.py)

from es.client import ESClient
from es.indexer import Indexer
from es.searcher import Searcher
from es.config.config import configs

# Create an instance of the Elasticsearch client.
client = ESClient()

# Check if the "podcast" index exists in Elasticsearch.
index_exists = client.Get_es().indices.exists(index="podcast")

# If the index does not exist, index podcast data.
# Comment out the line below to override and force reindexing.
if not index_exists:
    print("Indexing...")
    # Create an instance of the Indexer class with the Elasticsearch client.
    indexer = Indexer(client)
    # Index podcast data into the "podcast" index.
    indexer.index_podcasts("podcast")

# Create an instance of the Searcher class with the Elasticsearch client.
searcher = Searcher(client)

# Define the duration (in seconds) for the segments to search for.
seconds = 35

# Search for segments containing the query "hi" within the specified duration.
# The third argument is a dictionary with additional search parameters, in this case, the duration.
segments = searcher.search_podcasts("podcast", "hi", {"seconds": seconds})

# If relevant segments are found, print information about each segment.
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