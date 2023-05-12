#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, div, mul
    import sys
    argc = len(sys.argv) - 1
    if argc != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    else:
        operator = sys.argv[2]
        num_1 = int(sys.argv[1])
        num_2 = int(sys.argv[3])
    
        if operator not in ['/', '-', '*', '+']:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
        else:
            if operator == "+":
                print("{} {} {} = {}".format(num_1, operator, num_2, add(num_1, num_2)))
            elif operator == "-":
                print("{} {} {} = {}".format(num_1, operator, num_2, sub(num_1, num_2)))
            elif operator == "*":
                print("{} {} {} = {}".format(num_1, operator, num_2, mul(num_1, num_2)))
            elif operator == "/":
                print("{} {} {} = {}".format(num_1, operator, num_2, div(num_1, num_2)))
