# project main.py

from backend.app import webapp
from es.indexer import Indexer
from es.config.config import configs


# Run the Flask application
if __name__ == '__main__':
    indexer = Indexer()
    indexer.index_podcasts(idx_name=configs['index_name'], args={"limit": 105360, "force_indexing": False})
    webapp.run(host="0.0.0.0", debug=False)