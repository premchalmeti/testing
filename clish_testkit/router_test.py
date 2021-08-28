# built-in imports

# third-party imports

# custom imports
import constants
from base_testcase import BaseTest
from utils import SequentialTestCaseLoader


__author__ = 'premchalmeti'


class RouterTest(BaseTest):
    """
    This class contains all Router related tests,
    router set hostname <hostname>, 
    router enable, 
    show ip

    more commands: https://www.geeksforgeeks.org/cisco-router-basic-commands/
    """
    @classmethod
    def setUpClass(cls):
        super().setUpClass(cls.__name__)

    def test_router_enable(self):
        """
        TEST: router enable
        """
        result_json = self._enable_router()
        self.assert_success(result_json)

    def _setup_test_show_ip(self):
        self._enable_router()
        self._assign_ip()

    def test_show_ip(self):
        """
        TEST: show ip
        """
        CMD = "show ip"
        self.execute_assert_success(CMD)

    def _cleanup_test_show_ip(self):
        self._release_ip()
        self._disable_router()

    def _enable_router(self):
        CMD = 'router enable'
        return self.execute_cmd(CMD)

    def _disable_router(self):
        CMD = 'router disable'
        return self.execute_cmd(CMD)

    def _assign_ip(self):
        CMD = f'router ip address {constants.IP} {constants.NETMASK}'
        return self.execute_cmd(CMD)

    def _release_ip(self):
        CMD = 'router ip unset'
        return self.execute_cmd(CMD)


if __name__ == '__main__':
    import unittest
    unittest.main(testLoader=SequentialTestCaseLoader())
