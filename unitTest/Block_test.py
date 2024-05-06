import unittest

# command -> python -m unittest Block_test.py

class MyTest(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(1 + 1, 3)
