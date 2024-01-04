#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    len = len(sys.argv) - 1
    if len == 1:
        print("{} argument:".format(len))
    elif len == 0:
        print("{} arguments.".format(len))
    else:
        print("{} arguments:".format(len))

    for i, ar in enumerate(sys.argv):
        if i > 0:
            print("{}: {}".format(i, ar))
