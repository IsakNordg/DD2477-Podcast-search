# project main

import sys

from backend.app import webapp
from es.indexer import Indexer
from es.config.config import configs


# Run the Flask application with specified parameters.
if __name__ == '__main__':

    # Default values for necessary parameters
    append = True
    force = False
    debug = False
    limit = 105360
    hosts = "0.0.0.0"

    # Check if command-line arguments are provided
    if len(sys.argv) > 1:
        # Parse command-line arguments
        for arg in sys.argv[1:]:
            key, value = arg.split('=')
            if key == 'append':
                append = value.lower() == 'true'
            elif key == 'force_idx':
                force = value.lower() != 'false'
            elif key == 'debug':
                debug = value.lower() != 'false'
            elif key == 'limit':
                limit = int(value)
            elif key == 'hosts':
                hosts = str(value)

    # Create an instance of the Indexer class
    indexer = Indexer()

    # Index podcasts with the specified parameters
    indexer.index_podcasts(idx_name=configs['idx_name'], limit=limit, force_indexing=force, append=append)

    webapp.run(host=hosts, debug=debug, use_reloader=False)