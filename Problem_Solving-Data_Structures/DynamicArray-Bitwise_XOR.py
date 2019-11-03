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
    ''' n indicates the number of sequences that we will be using'''
    seqList = [[] for i in range(n)] 
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
            seqIndex = (query[1]^lastAnswer) % n 
            #print(query)
            #print(seqList)
            #print(lastAnswer)
            #print(seqIndex)
            #print(query[2]%n)
            #print(seqList)
            seq = seqList[seqIndex]
            length = len(seq)
            lastAnswer = seq[query[2]%length]
            result.append(lastAnswer)
    return result

if __name__ == '__main__':

    fp = open("test.txt")
    lines = fp.readlines()
    #print(line)
    first_multiple_input = lines[0].rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    queries = []

    for i in range(q):
        queries.append(list(map(int, lines[1+i].rstrip().split())))

    result = dynamicArray(n, queries)

    print('\n'.join(map(str, result)), end='')

    fp.close()
   
