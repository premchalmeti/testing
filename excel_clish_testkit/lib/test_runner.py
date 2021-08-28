import os

import utils
import config
import constants
import exceptions
from excel_mgr import ExcelManager
from testcase import TestCase


class TestRunner:
    """
        Main entrypoint for framework expose 2 main methods, `run_all()` and `run(tcname)`
        - `run_all()`` scans Excel testcases in `config.TEST_SRC_DIR` location which internally call `run(tcname)`
        - Uses with `ExcelManager` to parse TC excel
        - Prepare `TestCase` and run `TestCase().test()`
        - update TestCase results
    """
    def __init__(self):
        self.excel_mgr = None
        self.logger = utils.get_logger('testrunner')

    def run_all(self):
        self.logger.info(f'Looking for tests in {config.TEST_SRC_DIR} location')

        for entry in os.scandir(config.TEST_SRC_DIR):
            if entry.is_file() and entry.name.endswith('.xlsx') and not entry.name.startswith('~$'):
                self.run(entry.name.split('.')[0])

    def run(self, tcname):
        constants.CURRENT_TC = tcname

        self.excel_mgr = ExcelManager()

        test_row_cells = []

        try:
            test_row_cells = self.excel_mgr.get_tests()
        except exceptions.InvalidExcelException:
            self.logger.critical("Invalid excel", exc_info=True)
        except FileNotFoundError:
            self.logger.error("Excel not found", exc_info=True)

        should_update_excel = False

        for test_row_cell in test_row_cells:
            try:
                test_obj = TestCase(test_row_cell, self.excel_mgr.headers)

                if test_obj.skipped:
                    self.logger.warning(f"{test_obj.cmd_str} | Test is skipped")
                    continue
                elif not test_obj.readonly and config.READ_ONLY_RUN:
                    self.logger.warning(f"{test_obj.cmd_str} | Test is not read only. READ_ONLY flag is enabled")
                    continue

                self.logger.info(f"Running {test_obj.cmd_str} test")

                test_obj.test()
                should_update_excel = True
            except exceptions.SkipTestError as exc:
                self.logger.error("Skipping Test", exc_info=True)
            except exceptions.SkipTestCaseError as exc:
                self.logger.critical("Skipping Complete TestCase", exc_info=True)

        if should_update_excel:
            self.logger.info(f'Updating {tcname} test results')
            self.excel_mgr.update_test_result(test_row_cells)
            self.excel_mgr.save_excel()
        else:
            self.logger.info(f'All {tcname} tests skipped')


if __name__ == '__main__':
    TestRunner().run_all()

