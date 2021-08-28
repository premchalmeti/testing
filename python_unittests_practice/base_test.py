import unittest


class BaseTest(unittest.TestCase):
    def __init__(self, tcname, testmtd):
        super().__init__(testmtd)
        self.tcname = tcname
        self.init_logger()

    def init_logger(self):
        print('logger initialized for', self._testMethodName)
        pass

    def setUp(self):
        print('\nRunning Test:', self._testMethodName)
    
    def execute_cmd(self, cmd):
        print('executing', cmd)

    def execute_assert_success(self, cmd):
        self.execute_cmd(cmd)
        print('asserting successing')
