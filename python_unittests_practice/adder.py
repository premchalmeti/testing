

def add(n1, n2):
    return n1 + n2


def sub(n1, n2):
    return n1 - n2


import unittest


class AddTest(unittest.TestCase):
    def setUp(self):
        print('\nTesting', self._testMethodName)

    def test_negative(self):
        self.assertEqual(add(-5, 2), -3)
    
    def test_positive(self):
        self.assertEqual(add(5, 2), 7)
    
    def test_zero(self):
        self.assertEqual(add(5, 0), 5)


class SubTest(unittest.TestCase):
    def setUp(self):
        print('\nTesting', self._testMethodName)

    def test_negative(self):
        self.skipTest("Skipping from code")
        self.assertEqual(sub(-5, 2), -7)
    
    @unittest.skip('demonstrating skip')
    def test_positive(self):
        self.assertEqual(sub(5, 2), 3)
    
    @unittest.skipIf(True, "Not running test_zero")
    def test_zero(self):
        self.assertEqual(sub(0, 5), -5)


def suite():
    math_suite = unittest.TestSuite()

    # math_suite.addTests([AddTest('test_negative'), AddTest('test_zero')])
    # math_suite.addTests([SubTest('test_zero'), SubTest('test_negative')])

    math_suite.addTest(unittest.makeSuite(AddTest))
    math_suite.addTest(unittest.makeSuite(SubTest))

    runner = unittest.TextTestRunner()
    test_result = runner.run(math_suite)

    print(
        'run =', test_result.testsRun, 
        'errors =', len(test_result.errors),
        'failures =', len(test_result.failures)
    )

if __name__ == '__main__':
    suite()
