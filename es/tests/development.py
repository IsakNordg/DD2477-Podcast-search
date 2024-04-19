# development.py
# A sample file for development (modified from initial main.py)

from es.client import ESClient
from es.indexer import Indexer
from es.searcher import Searcher
from es.config.config import configs

client = ESClient()  # Create an instance of the Elasticsearch client.
indexer = Indexer(client)  # Create an instance of the Indexer class with the Elasticsearch client.
searcher = Searcher(client)  # Create an instance of the Searcher class with the Elasticsearch client.

# Get the index name from the configuration.
index_name = configs["dev_idx_name"]

# Index sample data into Elasticsearch with the specified index name.
response = indexer.index_sample(idx_name=index_name)
# Print the indexing response.
print("Indexing response:", response)

# Search for sample data in Elasticsearch using the specified index and query.
search_results = searcher.search_sample(index=index_name, query="Hello")
# Print the search results.
searcher.print_es_results(search_results["hits"]["hits"])