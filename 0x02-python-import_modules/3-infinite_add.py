#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    args = sys.argv
    res = 0
    for ar in args:
        res += int(ar)
    print(res)