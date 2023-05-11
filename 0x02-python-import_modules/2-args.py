#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argc = len(sys.argv) - 1
    if argc == 0:
        print("{} arguments.".format(argc))
    elif argc == 1:
        print("{} argument:".format(argc))
        print("{}: {}".format(argc, sys.argv[argc]))
    else:
        counter = 1
        print("{} arguments:".format(argc))
        for arg in range(1, argc + 1):
            print("{}: {}".format(counter, sys.argv[arg]))
            counter += 1
