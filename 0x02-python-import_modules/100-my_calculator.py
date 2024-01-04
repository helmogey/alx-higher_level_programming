#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div

    args = sys.argv[1:]
    if len(args) != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    else:
        op = args[1]
        a = int(args[0])
        b = int(args[2])
        if op not in ["+", "-", "*", "/"]:
            print("Unknown operator. Available operators: +, -, * and /")
            sys.exit(1)
        if op == "+":
            print("{} {} {} = {}".format(a, op, b, add(a, b)))
        elif op == "-":
            print("{} {} {} = {}".format(a, op, b, sub(a, b)))
        elif op == "*":
            print("{} {} {} = {}".format(a, op, b, mul(a, b)))
        elif op == "/":
            print("{} {} {} = {}".format(a, op, b, div(a, b)))
