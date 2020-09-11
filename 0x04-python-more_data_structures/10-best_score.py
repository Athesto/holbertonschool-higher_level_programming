#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary == None:
        return None
    k,v = sorted(a_dictionary.items(), key = lambda x: x[1], reverse=True)[0]
    return (k)
