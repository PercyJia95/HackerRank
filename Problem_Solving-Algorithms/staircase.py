 #!/bin/python3

import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):
    for i in range(n):
        j=i+1
        print(' '*(n-j)+'#'*j)

if __name__ == '__main__':
    n = int(input())

    staircase(n)
