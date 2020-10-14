#!/usr/bin/python3
'''module test rectangle'''

import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    '''Testing Rectangle'''

    def test_width_str(self):
        '''TypeError: width="11"'''
        with self.assertRaises(TypeError) as ar:
            Rectangle("11", 10)
        self.assertEqual(str(ar.exception), "width must be an integer")

    def test_width_neg(self):
        '''ValueError: width=-10'''
        with self.assertRaises(ValueError) as ar:
            Rectangle(-10, 10)
        self.assertEqual(str(ar.exception), "width must be > 0")

    def test_width_zero(self):
        '''ValueError: width=0'''
        with self.assertRaises(ValueError) as ar:
            Rectangle(0, 10)
        self.assertEqual(str(ar.exception), "width must be > 0")

    def test_height_str(self):
        '''TypeError: height="11"'''
        with self.assertRaises(TypeError) as ar:
            Rectangle(10, "11")
        self.assertEqual(str(ar.exception), "height must be an integer")

    def test_height_neg(self):
        '''ValueError: height=-10'''
        with self.assertRaises(ValueError) as ar:
            Rectangle(10, -10)
        self.assertEqual(str(ar.exception), "height must be > 0")

    def test_height_zero(self):
        '''ValueError: height=0'''
        with self.assertRaises(ValueError) as ar:
            Rectangle(10, 0)
        self.assertEqual(str(ar.exception), "height must be > 0")

    def test_x_str(self):
        '''TypeError: x = "hello"'''
        with self.assertRaises(TypeError) as ar:
            Rectangle(10, 11, "hello")
        self.assertEqual(str(ar.exception), "x must be an integer")

    def test_x_neg(self):
        '''ValueError: x=-92'''
        with self.assertRaises(ValueError) as ar:
            Rectangle(10, 10, -19)
        self.assertEqual(str(ar.exception), "x must be >= 0")

    def test_y_str(self):
        '''TypeError: y="hello"'''
        with self.assertRaises(TypeError) as ar:
            Rectangle(10, 11, 10, "hello")
        self.assertEqual(str(ar.exception), "y must be an integer")

    def test_y_neg(self):
        '''ValueError: y=-92'''
        with self.assertRaises(ValueError) as ar:
            Rectangle(10, 10, 0, -19)
        self.assertEqual(str(ar.exception), "y must be >= 0")

    def test_area(self):
        '''Area(4,3) = 12'''
        r = Rectangle(4, 3)
        self.assertEqual(r.area(), 12)

    def test___str__(self):
        '''Rectangle(1,2,3,4,5)'''
        r = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(str(r), "[Rectangle] (5) 3/4 - 1/2")

    def test_display(self):
        '''Area(4,3) = 12'''
        pass

    # ------------------UNUSEFUL--------------------

    def test_width_bool(self):
        '''TypeError: width = True'''
        with self.assertRaises(TypeError) as ar:
            Rectangle(True, 10)
        self.assertEqual(str(ar.exception), "width must be an integer")


if __name__ == "__main__":
    __import__("sys").path.append('.')
    unittest.main()
