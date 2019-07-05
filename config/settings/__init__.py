import logging

from .base import *

logger = logging.getLogger()

mode = os.getenv('MODE', 'DEVELOPMENT')
logger.warn('Current mode: ' + mode)

if mode == "PRODUCTION":
    from .production import *
else:
    from .local import *
