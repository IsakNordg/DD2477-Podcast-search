import yaml

from es.config.config import configs as _

def read_app_config(path="backend/config/settings.yml"):
    """
    Read configuration parameters from settings.yml.
    """
    with open(path, 'r') as f:
        _config = yaml.safe_load(f)

    _config.update(_)
    return _config

configs = read_app_config()