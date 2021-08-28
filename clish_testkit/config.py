import logging

LOG_LEVEL = logging.DEBUG

LOG_LOCATION = 'logs'

import os

try:
    os.makedirs(LOG_LOCATION)
except FileExistsError:
    pass

# turn on this flag to mock `ClishManager()`
MOCK_RUN = True
