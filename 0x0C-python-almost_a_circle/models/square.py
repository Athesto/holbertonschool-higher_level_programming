#!/usr/bin/python3
""" Define Square Class """


from models.rectangle import Rectangle


class Square(Rectangle):
    """ Define Square Class """

    def __init__(self, size, x=0, y=0, id=None):
        """ Constructor """

        if type(size) is not int:
            raise TypeError("size must be an integer")

        if not size > 0:
            raise ValueError("size must be > 0")
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")

        if not value > 0:
            raise ValueError("size must be > 0")
        self.width = value
        self.height = value

    def __str__(self):
        '''square information'''
        return '[Square] ({}) {}/{} - {}'.format(self.id,
                                                 self.x,
                                                 self.y,
                                                 self.width)
