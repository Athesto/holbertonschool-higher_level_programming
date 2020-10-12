#!/usr/bin/python3
'''module test'''
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    '''test class for Base'''

    def test_create(self):
        '''creation test'''
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base(20)
        self.assertEqual(b2.id, 20)
        b3 = Base()
        self.assertEqual(b3.id, 2)


if __name__ == "__main__":
    __import__("sys").path.append('.')
    unittest.main()
