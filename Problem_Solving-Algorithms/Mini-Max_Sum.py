#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    sum = 0
    min = math.inf
    max = -math.inf
    for i in arr:
        sum = sum + i
        if i < min:
            min = i
        if i > max:
            max = i
    print(str(sum-max)+" "+str(sum-min))

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
