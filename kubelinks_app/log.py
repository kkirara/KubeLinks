import logging, os
from kubernetes import config

LOGLEVEL = os.environ.get('LOGLEVEL', 'INFO').upper()
logger = logging.getLogger(__name__)
logger.setLevel(LOGLEVEL)

error = None

try:
    config.load_config()
except Exception as e:
    error = e
    logger.error(f'CONFIG: {e}')
