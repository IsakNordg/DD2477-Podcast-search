import unittest
import es.config.config as config

from elasticsearch import Elasticsearch
from es.searcher import searcher
from es.indexer import indexer


class TestExample(unittest.TestCase):

    configs = config.read_es_config()
    filepath = 'es/config/' + configs["http_crt"]
    username = configs["username"]
    password = configs["password"]

    client = Elasticsearch(
        hosts=configs["hosts"],
        basic_auth=(username, password),
        ca_certs=filepath
    )

    def test_connection(self):
        print(self.client.info())
        tagline = self.client.info()["tagline"]
        self.assertEqual("You Know, for Search", tagline)

    def test_indexing(self):
        response = indexer.index_sample(self.client)
        self.assertEqual(response["_index"], self.configs["idx_name"])

    def test_search(self):
        indexer.index_sample(self.client)
        es_results = searcher.search_sample(
            index=self.configs["idx_name"], query="Hello", es=self.client
        )
        self.assertEqual(es_results['hits']['hits'][0]['_source']['title'],
                         "Hello Elasticsearch")

if __name__ == '__main__':
    unittest.main()