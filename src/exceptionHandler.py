import os
import sys


def exceptionhandler(exception_type):
    path = (sys.path[0] + r'/../dates/')
    with open((path + "ERROR"), 'w') as f:
        f.write("Error: 500 \n" + exception_type)
    f.close()
    raise
