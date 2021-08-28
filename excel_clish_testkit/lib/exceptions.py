
class InvalidExcelException(Exception):
    """
    Custom Exception class if excel file is missing either Visible \
    or Restricted Column
    """
    pass


class SkipTestError(Exception):
    """
    Custom Exception to be raised to skip test in TestRunner.py
    """
    pass


class SkipTestCaseError(Exception):
    """
    Custom Exception to be raised to skip complete testcase in TestRunner.py
    """
    pass
