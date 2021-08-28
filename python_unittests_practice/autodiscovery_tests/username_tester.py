import unittest


def upper(username):
    return username.upper()


def lower(username):
    return username.lower()


class UserNameGreetTester(unittest.TestCase):
    def setUp(self):
        print('\nRunning', self._testMethodName, 'Test\n')
        # self.username = input('Give input: \n')
        self.username = 'Hello World'

    def test_upper(self):
        self.assertEqual(self.username.upper(), upper(self.username))
    
    def test_lower(self):
        self.assertEqual(self.username.lower(), lower(self.username))

    def test_splitting(self):
        self.assertEqual(self.username.split(' '), ['Hello', 'World'])
