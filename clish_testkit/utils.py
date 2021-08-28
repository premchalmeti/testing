# built-in imports
import string
import random
import os
import logging
import unittest
from unittest.mock import Mock

# third-party imports

# custom imports
import config
import constants


__author__ = 'premchalmeti'


def get_logger(logger_name, log_console=True, log_file=True):
    """
    Initialize and returns a logger instance with, 
    file handler (in config.LOG_LOCATION/<logger_name>.log) and 
    console logging
    """
    logger = logging.getLogger(logger_name)
    logger.setLevel(config.LOG_LEVEL)

    formatter = logging.Formatter(
        '%(asctime)s | %(name)s | %(levelname)s | %(message)s'
    )

    if log_console:
        console_handler = logging.StreamHandler()
        console_handler.setLevel(config.LOG_LEVEL)
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

    if log_file:
        file_handler = logging.FileHandler(
            filename=os.path.join(config.LOG_LOCATION, f'{logger_name}.log')
        )
        file_handler.setLevel(config.LOG_LEVEL)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    return logger


class SequentialTestCaseLoader(unittest.TestLoader):
    """
    The python's unittest library executes the tests in alphabetical order 
    to override this behaviour and execute tests in (defined) order. 
    Use `unittest.main(testLoader=SequentialTestCaseLoader())` to 
    the trigger execution.
    """
    def getTestCaseNames(self, tcCls):
        tcnames = super().getTestCaseNames(tcCls)
        tc_mtds = list(tcCls.__dict__.keys())
        tcnames.sort(key=tc_mtds.index)
        return tcnames


def get_random_string(N):
    return "".join(random.choices(string.ascii_letters, k=N))


def get_clish_instance():
    """
    Provide CLISH execution instance based on config.MOCK_RUN flag
    to run commands
    """
    if config.MOCK_RUN:
        clish_obj = Mock()
        clish_obj.return_value = clish_obj

        clish_obj.run.return_value = (
            '{"header": {"status": "%s"}}' % constants.SUCCESS_VAL
        ).encode('utf-8'), ""
    else:
        from clish_manager import ClishManager

        clish_obj = ClishManager()
 
    return clish_obj
