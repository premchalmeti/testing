RESTRICTED_COL = 'Restricted'
VISIBLE_COL = 'Visible'
TEST_RESULT_COL = 'Test Result'
SUCCESS_COL = 'Success Output'
ERROR_COL = 'Error Output'
SKIP_COL = 'Skip'

EXCEL_CMD_CELL_LIMIT = 30
EXCEL_ROW_OFFSET = 1

CELL_EMPTY_VALUES = [None, "", " "]

TRUE_VALUE = [True, "yes", 'true', 'y', 't']

FALSE_VALUE = [False, "no", 'false', 'n', 'f']

# this is a global variable which will be set by TestManager
CURRENT_TC = ""

SUCCESS_VAL = 'SUCCESS'
ERROR_VAL = 'ERROR'

TEXT_OUTPUT = "txt"
JSON_OUTPUT = 'json'

OUTPUT_ERROR_KEYWORDS = ['error', 'exception', 'failed', 'failure']

TEST_FAILED = 'Failed'
TEST_SUCCESS = 'Success'

TEST_HEADER = [f'LEVEL_{i+1}' for i in range(EXCEL_CMD_CELL_LIMIT)] + [SUCCESS_COL, ERROR_COL, TEST_RESULT_COL, SKIP_COL]
