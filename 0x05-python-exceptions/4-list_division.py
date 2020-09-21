#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    list_out = []
    for idx in range(list_length):
        try:
            tmp = my_list_1[idx] / my_list_2[idx]
        except IndexError:
            print("out of range")
        except ZeroDivisionError:
            print("division by 0")
            tmp = 0
        except TypeError:
            print("wrong type")
            tmp = 0
        finally:
            list_out.append(tmp)
    print()
    return list_out
