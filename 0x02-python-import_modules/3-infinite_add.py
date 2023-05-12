#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argc = len(sys.argv) - 1
    counter = 0
    i = 1
    if argc == 0:
        print("{}".format(counter))
    else:
        for arg in range(1, argc + 1):
            counter += int(sys.argv[i])
            i += 1
        print("{}".format(counter))
