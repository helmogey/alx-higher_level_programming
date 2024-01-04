#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    args = sys.argv[1:]
    res = 0
    if len(args) > 0:
        for ar in args:
            res += int(ar)
    print("{}".format(res))