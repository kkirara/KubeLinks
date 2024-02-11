import logging
import os

LOGLEVEL = os.environ.get('LOGLEVEL', 'INFO').upper()
logger = logging.getLogger(__name__)
logger.setLevel(LOGLEVEL)
logger.debug(f'loglevel {LOGLEVEL}')
