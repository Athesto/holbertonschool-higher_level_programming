#!/usr/bin/python3
'''module test rectangle'''

import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    '''Testing Rectangle'''

    def test_str_width(self):
        '''TypeError: str_width'''
        with self.assertRaises(TypeError) as ar:
            Rectangle("11", 10)
        self.assertEqual(str(ar.exception), "width must be an integer")

    def test_bol_width(self):
        '''TypeError: bol_width'''
        with self.assertRaises(TypeError) as ar:
            Rectangle(True, 10)
        self.assertEqual(str(ar.exception), "width must be an integer")

    def test_str_height(self):
        '''TypeError: str_height'''
        with self.assertRaises(TypeError) as ar:
            Rectangle(10, "11")
        self.assertEqual(str(ar.exception), "height must be an integer")


if __name__ == "__main__":
    __import__("sys").path.append('.')
    unittest.main()
