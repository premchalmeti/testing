import os
import json
import logging

import config
import constants


def get_logger(logger_name):
    """
    Initialize and returns a logger instance with,
    file handler (in config.LOG_DIR/<logger_name>.log) and
    console logging
    """
    logger = logging.getLogger(logger_name)
    logger.setLevel(config.LOG_LEVEL)

    logger.disabled = not config.FILE_LOGGING and not config.CONSOLE_LOGGING

    formatter = logging.Formatter('%(asctime)s | %(name)s | %(funcName)s() | %(levelname)s | %(message)s')

    if config.CONSOLE_LOGGING and len(logger.handlers) == 0:
        console_handler = logging.StreamHandler()
        console_handler.setLevel(config.LOG_LEVEL)
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

    if config.FILE_LOGGING and (
        (config.CONSOLE_LOGGING and len(logger.handlers) == 1) \
        or (not config.CONSOLE_LOGGING and len(logger.handlers) == 0)
    ):
        file_handler = logging.FileHandler(
            filename=os.path.join(config.LOG_DIR, f'{logger_name}.log')
        )
        file_handler.setLevel(config.LOG_LEVEL)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    return logger


def is_param(cell):
    return "<" in cell or "[" in cell


def is_optional_param(param):
    return "[" in param


def get_param(param):
    import re
    return re.sub("[\[\]<>]", "", param)


def get_bool_value(v):
    if isinstance(v, str):
        v = v.lower()
    if v in constants.TRUE_VALUE:
        return True
    elif v in constants.FALSE_VALUE:
        return False
    return v


def get_clish_instance():
    if config.MOCK_RUN:
        from unittest.mock import Mock
        import constants

        ClishManager = Mock()
        ClishManager.return_value = ClishManager
        ClishManager().run.return_value = json.dumps({'STATUS': constants.SUCCESS_VAL})

    from clish_mgr import ClishManager
    return ClishManager()


def pprint(obj):
    print(json.dumps(obj, indent=4))


def transform_cmd_look(cmd):
    import re
    return re.sub('-', '_', cmd)
