#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'dynamicArray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

def dynamicArray(n, queries):
    # n indicates the number of sequences that we will be using
    seqList = [[] for i in range(n)] # Creating the Dynamic Arrray
    lastAnswer = 0
    result = []
    for query in queries:
        if query[0] == 1:
            seqIndex = (query[1]^lastAnswer) % n
            #print (n)
            #print (seqIndex)
            #print (seqList)
            #print (query)
            seqList[seqIndex].append(query[2])
        if query[0] == 2:
            seqIndex = (query[1]^lastAnswer) % n # N1^N2 is the right way to use bitwise XOR operator
            #print(query)
            #print(lastAnswer)
            #print(seqIndex)
            #print(query[2]%n)
            #print(seqList)
            lastAnswer = seqList[seqIndex][query[2]%n]
            result.append(lastAnswer)
    return result   # the function is expected to return an iterator, and a list of lastAnswers are returned

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    result = dynamicArray(n, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
