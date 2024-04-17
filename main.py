import os
from elasticsearch import Elasticsearch
from dotenv import load_dotenv
load_dotenv()

username = "elastic"
password = os.getenv("password")
client = Elasticsearch("http://localhost:9200/", basic_auth=(username, password))

#print(client.info())
index_name = "my_index"
doc_id = "1"
doc_body = {
    "title": "Hello Elasticsearch",
    "content": "This is a test document for Elasticsearch indexing."
}
response = client.index(index=index_name, id=doc_id, body=doc_body)
print("Indexing response:", response)


search_query = {
    "query": {
        "match": {
            "title": "Hello"
        }
    }
}

search_results = client.search(index=index_name, body=search_query)
print("Search results:")
for hit in search_results['hits']['hits']:
    print(hit['_id'], hit['_source'])
