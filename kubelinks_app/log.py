import logging
from kubernetes import config

logger = logging.getLogger(__name__)
error = None

try:
    config.load_config()
except Exception as e:
    error = e
    logger.error(f'CONFIG: {e}')
