from base_test import BaseTest


class ChildCmdTest(BaseTest):
    def __init__(self, testmtd):
        super().__init__(self.__class__.__name__, testmtd)

    def test_cmd1(self):
        """
        TEST: storage disk list
        """
        self.execute_assert_success("echo cmd 1")
    
    def test_cmd2(self):
        """
        TEST: storage pool list
        """
        self.execute_assert_success("echo cmd 2")
