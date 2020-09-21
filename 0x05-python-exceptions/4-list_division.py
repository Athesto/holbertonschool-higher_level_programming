#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    list_out = []
    for idx in range(list_length):
        tmp = 0
        try:
            tmp = my_list_1[idx] / my_list_2[idx]
        except IndexError:
            print("out of range")
        except ZeroDivisionError:
            print("division by 0")
        except TypeError:
            print("wrong type")
        finally:
            list_out.append(tmp)
    return list_out
