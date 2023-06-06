#!/usr/bin/python
"""testing module for max integer function"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """ max_integer Tests """
    def test_max_integer_empty(self):
        """ Testing for empty """
        self.assertIsNone(max_integer())
        self.assertIsNone(max_integer([]))

    def test_max_integer_negative(self):
        """ Testing list including negative """
        self.assertEqual(max_integer([-1, -2, -7, -5]), -1)
        self.assertEqual(max_integer([-1, 2, -3, 4, 9]), 9)

    def test_max_integer_one_number(self):
        """ Testing list with only one number """
        self.assertEqual(max_integer([6]), 6)

    def test_max_integer_dublicate_number(self):
        """ Testing list with dublicated numbers """
        self.assertEqual(max_integer([7, 7, 7, 7]), 7)

    def test_max_integer_non_int(self):
        """ Testing list with string types """
        with self.assertRaises(TypeError):
            max_integer([5, 6, "Abubakr"])


if __name__ == "__main__":
    unittest.main()
