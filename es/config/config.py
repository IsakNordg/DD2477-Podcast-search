import yaml

def read_es_config():
    """
    Read configuration parameters from elasticsearch.yml.
    """
    with open("es/config/elasticsearch.yml", 'r') as f:
        _config = yaml.safe_load(f)
    return _config

configs = read_es_config()