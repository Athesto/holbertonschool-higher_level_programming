#!/usr/bin/python3
'''Task 1'''


class MyList(list):
    '''My list Class'''
    def print_sorted(self):
        '''print_sorted'''
        list_sorted = self[:]
        list_sorted.sort()
        print(list_sorted)

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/1-my_list.txt")
