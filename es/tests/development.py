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
#First arg is the name of index, second is the query we want to search for
clips = searcher.search_podcasts("podcast", "hi")
print("Documents containing the phrase:")
print(clips)

