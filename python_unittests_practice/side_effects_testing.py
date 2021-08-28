import unittest
from unittest.mock import Mock
from requests.exceptions import Timeout

from custom_mock_obj import MockedResponse

# side effects
def get_holidays():
    r = requests.get('https://jsonplaceholder.typicode.com/todos/')

    if r.status_code == 200:
        return r.json()
    
    return None


requests = Mock()
# requests.get.return_value = MockedResponse()
requests.get.side_effect = Timeout


class HolidayTestCase(unittest.TestCase):
    def test_get_holiday(self):
        with self.assertRaises(Timeout):
            get_holidays()


# if __name__ == '__main__':
    # unittest.main() #=> trigger tc execution
