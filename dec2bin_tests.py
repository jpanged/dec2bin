# Decimal to Binary Conversion Test Cases
# Author: Josiah Pang
# File: dec2bin_tests.py
# Date: 2017-06-22
# Description: Test cases for the dec2bin.py file

import unittest
from dec2bin import *

class TestCase(unittest.TestCase):
    # Tests convert function
    def test_convert(self):
        self.assertEqual(convert(0), 0)
        self.assertEqual(convert(10), 1010)
        self.assertEqual(convert(42), 101010)
        self.assertEqual(convert(5), 101)
        self.assertEqual(convert(9999), 10011100001111)

if __name__ == '__main__':
   unittest.main()
