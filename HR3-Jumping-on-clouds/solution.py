#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'jumpingOnClouds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY c as parameter.
#

def jumpingOnClouds(c):
    i = 0
    step = 0
    while i <= len(c) - 2:
        if i == len(c) - 2:
            step += 1
            break
        if c[i+2] == 0:
            i = i + 2
            step += 1
            continue
        else:
            i += 1
            step +=1
    return step

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
