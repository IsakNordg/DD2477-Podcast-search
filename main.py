# project main.py

import sys

from backend.app import webapp
from es.indexer import Indexer
from es.config.config import configs


# Run the Flask application with specified parameters.
if __name__ == '__main__':

    # Default values for necessary parameters
    force = False
    debug = False
    limit = 105360
    hosts = "0.0.0.0"
    index = configs['index_name']

    # Check if command-line arguments are provided
    if len(sys.argv) > 1:
        # Parse command-line arguments
        for arg in sys.argv[1:]:
            key, value = arg.split('=')
            if key == 'force_idx':
                force = bool(value)
            elif key == 'debug':
                debug = bool(value)
            elif key == 'limit':
                limit = int(value)
            elif key == 'hosts':
                hosts = str(value)
            elif key == 'idx_name':
                index = str(value)

    # Create an instance of the Indexer class
    indexer = Indexer()

    # Index podcasts with the specified parameters
    indexer.index_podcasts(idx_name=index, limit=limit, force_indexing=force)

    webapp.run(host=hosts, debug=debug)