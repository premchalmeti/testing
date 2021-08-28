import os
import sys
import logging

BASE_DIR = os.path.abspath('.')
sys.path.append(BASE_DIR)

# log configs
LOG_LEVEL = logging.DEBUG
FILE_LOGGING = True
CONSOLE_LOGGING = False
LOG_DIR = os.path.join(BASE_DIR, 'logs')

try:
    os.makedirs(LOG_DIR)
except FileExistsError:
    pass

TEST_SRC_DIR = os.path.join(BASE_DIR, 'tests')

SETUP_HOOK = 'hooks.setup'
CLEANUP_HOOK = 'hooks.cleanup'

OPERANDS_DIR = os.path.join(BASE_DIR, 'operands')

MOCK_RUN = True
READ_ONLY_RUN = True
