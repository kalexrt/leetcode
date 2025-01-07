#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'arrayManipulation' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

def arrayManipulation(n, queries):
    a = [0] * (n + 1)  # Initialize array with zeros
    
    # Apply the range updates
    for r in queries:
        a[r[0] - 1] += r[2]  # Convert to 0-based indexing
        if r[1] < n:  # Only update the end+1 index if it's within bounds
            a[r[1]] -= r[2]
    
    # Find the maximum value after computing prefix sums
    big = 0
    current = 0
    for i in range(n):
        current += a[i]
        if current > big:
            big = current
    
    return big

        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()
