#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    max1 = - math.inf
    max_ = 0
    l = []
    for i in range(len(arr)):
        if i+2 > len(arr)-1:
            break
        print(i+2)
        for j in range(len(arr[i])):
            if j+2 > len(arr[i])-1:
                break
            a = arr
            max_ = a[i][j]+a[i][j+1]+a[i][j+2]
            max_ = max_  + a[i+1][j+1]
            max_ = max_ + a[i+2][j] + a[i+2][j+1] + a[i+2][j+2]
            if max_ > max1:
                max1 = max_ 
                l = [a[i][j], a[i][j+1], a[i][j+1], a[i+1][j+1], a[i+2][j], a[i+2][j+1], a[i+2][j+2]]
    print (l)
    return max1
        



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
