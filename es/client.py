"""
Define Elasticsearch client setup.

File: <client.py>
Author: <Wenqi Cao>
Purpose: Initialize Elasticsearch client
Description: This file initializes the Elasticsearch client for
             interacting with Elasticsearch.
"""

from elasticsearch import Elasticsearch
from es.config.config import configs

class ESClient:
    def __init__(self, hosts=configs["hosts"],
                 username=configs["username"],
                 password=configs["password"],
                 crt_path='config/' + configs["http_crt"],
                 fingerprint=configs["fingerprint"]):

        if configs["http_crt"] == "":
            self.es = Elasticsearch(
                hosts=hosts,
                basic_auth=(username, password),
                ssl_assert_fingerprint=fingerprint
            )
        else:
            self.es = Elasticsearch(
                hosts=hosts,
                basic_auth=(username, password),
                ca_certs=crt_path
            )


client = ESClient()