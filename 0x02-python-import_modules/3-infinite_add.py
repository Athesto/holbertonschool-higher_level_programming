#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv = sys.argv
    argc = len(argv)
    val = 0
    for v_idx in range(1, argc):
        val += int(argv[v_idx])
    print(val)
