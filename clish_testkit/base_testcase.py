# built-in imports
import json
import unittest

# third-party imports

# custom imports
import utils
import constants


__author__ = 'premchalmeti'


class BaseTest(unittest.TestCase):
    """
    BaseTest is a utility class which inherits from `unittest.TestCase` class
    and does some heavy lifting,
    1. Initialize and Provide a logger object for logging
    2. Provide systematic setup and cleanup for each test
        - define _setup_<complete_test_name>()
        - define _cleanup_<complete_test_name>()
    3. Fetch appropriate clish instance (based on config.MOCK_RUN flag) 
        to run commands
    4. overrides run(testresult) method to hook test results in 
        `self._test_result`
    5. Provides utility functions to execute clish cmd,
        1. execute_cmd(cmd): runs cmd and returns result json
        2. assert_success(result_json): assert `constants.SUCCESS_VALUE` 
                                        in `result_json`
        3. execute_assert_success(cmd):
            - it runs execute_cmd(cmd) and then assert_success(result_json)
    """
    @classmethod
    def setUpClass(cls, tcname):
        cls.tcname = tcname
        cls.init_logger()

        cls.clish_obj = utils.get_clish_instance()

    def setUp(self):
        cls = self.__class__
        cls.logger.info('Testing ' + self._testMethodName)

        test = self._testMethodName
        setup_fun_name = f"_setup_{test}"

        if not hasattr(self, setup_fun_name):
            return

        setup_func = getattr(self, setup_fun_name)
        cls.logger.info(f'Setting up TC, calling {setup_func.__name__}()')
        setup_func()

    @classmethod
    def init_logger(cls):
        cls.logger = utils.get_logger(cls.tcname)

    def run(self, result=None):
        self._test_result = result
        super().run(result)

    def execute_cmd(self, cmd):
        cls = self.__class__

        cls.logger.info(f'Executing "{cmd}"')

        stdout, stderr = cls.clish_obj.run(cmd)

        if not stdout:
            cls.logger.error(
                f"\nNo output received \n Output: {stdout}", 
            )
            raise Exception(f'No output for "{cmd}"')

        cmd_res = stdout.decode('utf-8')

        cls.logger.info(
            f"\nStdout: {cmd_res} \nStderr: {stderr}"
        )

        cmd_json = {}

        try:
            cmd_json = json.loads(cmd_res)
        except json.JSONDecodeError as exc:
            cls.logger.error(
                "\nJSONDecodeError: "+ str(exc) + "\nOutput: " + cmd_res
            )

        return cmd_json

    def assert_success(self, result_json):
        self.assertEqual(
            result_json['header']['status'], constants.SUCCESS_VAL
        )

    def execute_assert_success(self, cmd):
        result_json = self.execute_cmd(cmd)
        self.assert_success(result_json)

    def tearDown(self):
        cls = self.__class__
        test = self._testMethodName
        cleanup_fun_name = f"_cleanup_{test}"

        if not hasattr(self, cleanup_fun_name):
            return

        cleanup_func = getattr(self, cleanup_fun_name)
        cls.logger.info(f'Cleaning up TC, calling {cleanup_func.__name__}()')
        cleanup_func()
