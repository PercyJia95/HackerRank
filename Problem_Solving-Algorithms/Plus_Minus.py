#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr, n):
    positive = 0
    negative = 0
    zeros = 0
    for i in arr:
        if i>0:
            positive = positive +1
            continue
        if i<0:
            negative = negative +1
            continue
        else:
            zeros = zeros +1
    print (positive/n)
    print (negative/n)
    print (zeros/n)

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr, n)
