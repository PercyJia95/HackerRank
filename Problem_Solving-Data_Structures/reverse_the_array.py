#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the reverseArray function below.
# It is called array but in Python it is actually the "List data structure".
def reverseArray(a):
    length = len(a)
    i = 0
    b = []
    while i < length:
        b.append(a[length-1-i])
        i = i+1
    return b

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = reverseArray(arr)

    fptr.write(' '.join(map(str, res)))
    fptr.write('\n')

    fptr.close()