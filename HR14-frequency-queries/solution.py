#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the freqQuery function below.
def freqQuery(queries):
    dict1 = {}
    output = []
    for item in queries:
        operation = item[0]
        number = item[1]
        if operation == 1:
            if number in dict1.keys():
                dict1[number] += 1
            else:
                dict1[number] = 1
        elif operation == 2:
            if number in dict1.keys() and dict1[number] > 0:
                dict1[number] -= 1
        elif operation == 3:
            if number in dict1.values():
                output.append(1)
            else:
                output.append(0)
    return output

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    ans = freqQuery(queries)

    fptr.write('\n'.join(map(str, ans)))
    fptr.write('\n')

    fptr.close()
