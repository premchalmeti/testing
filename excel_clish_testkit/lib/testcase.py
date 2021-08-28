import json
import importlib

import config
import utils
import constants
from command import Command
from excel_mgr import ExcelManager

# extract cmd (admin show [username])
# call setup hook
# create Command()
# run command and assert test result
# perform cleanup hook


class TestCase:
    """
    The `TestCase` class is represents the tests(rows) in the given excel TC.
    Does the following things,
    - The actual class which do the testcase assertions
    - The command is passed to `Command()` obj
    - call setup hook before test case run
    - test():
        - calls `Command().run()`
        - and `do_assertions()`
    - call cleanup hook after test case run
    """
    def __init__(self, test_row, headers):
        self.headers = headers
        self.test_row = test_row
        self.cmd = ExcelManager.get_complete_cmd(self.test_row)
        self.cmd_str = " ".join(self.cmd)

        if self.skipped:
            return

        self.logger = utils.get_logger(f"{constants.CURRENT_TC}.{self.__class__.__name__}")
        self.cmd_obj = Command(self.cmd)
        self.logger.debug(f"{self.cmd_str} | Testcase Initialized")

    def call_setup_hook(self):
        self.logger.info(f"{self.cmd_str} | Calling Setup hook")
        import_path = f'{config.SETUP_HOOK}.{constants.CURRENT_TC}'
        self._call_hook(import_path)

    def call_cleanup_hook(self):
        self.logger.info(f"{self.cmd_str} | Calling Cleanup hook")
        import_path = f'{config.CLEANUP_HOOK}.{constants.CURRENT_TC}'
        self._call_hook(import_path)

    def set_output(self):
        if self.cmd_obj.is_error():
            self.logger.warning(f"{self.cmd_str} | Updating error output in excel")
            error_col_index = self.headers.index(constants.ERROR_COL)
            self.test_row[error_col_index] = self.output
        else:
            self.logger.debug(f"{self.cmd_str} | Updating success output in excel")
            success_col_index = self.headers.index(constants.SUCCESS_COL)
            self.test_row[success_col_index] = self.output

    def do_assertions(self):
        self.test_result = constants.TEST_FAILED if self.cmd_obj.is_error() else constants.TEST_SUCCESS
        self.logger.info(f"{self.cmd_str} | Test result: {self.test_result}")

    def update_test_result(self):
        if constants.TEST_RESULT_COL in self.headers:
            self.logger.debug(f"{self.cmd_str} | Updating test result in excel")
            test_result_index = self.headers.index(constants.TEST_RESULT_COL)
            self.test_row[test_result_index] = self.test_result
        else:
            self.logger.warning(f"{self.cmd_str} | Excel has no {constants.TEST_RESULT_COL} column")
            self.test_row.append(self.test_result)

    def test(self):
        self.logger.info(f"{self.cmd_str} | Running test")
        # call setup
        self.call_setup_hook()

        # test and assert
        self.output, stderr = self.cmd_obj.run()

        if stderr:
            self.logger.error(f"{self.cmd_str} | Got stderr: {stderr}")

        self.do_assertions()
        self.update_test_result()
        self.set_output()

        # call cleanup
        self.call_cleanup_hook()

    def _import_mod(self, import_path):
        try:
            self.logger.info(f'{self.cmd_str} | Importing {import_path} module')
            return importlib.import_module(import_path)
        except ImportError:
            self.logger.info(f'{self.cmd_str} | Unable import {import_path} module')

    def _call_hook(self, import_path):
        setup_mod = self._import_mod(import_path)

        func = getattr(setup_mod, utils.transform_cmd_look(self.cmd_obj.lookup_cmd_str), None)

        if func:
            self.logger.info(f'{self.cmd_obj.lookup_cmd_str} | calling hook')
            func(
                testcase=self, clish=self.cmd_obj.clish, operands=self.cmd_obj.operands
            )
        else:
            self.logger.info(f'{self.cmd_obj.lookup_cmd_str} | No hook found')

    @property
    def skipped(self):
        i = self.headers.index(constants.SKIP_COL) if constants.SKIP_COL in self.headers else -1
        return i > 0 and utils.get_bool_value(self.test_row[i])

    @property
    def readonly(self):
        return self.cmd_obj.readonly
