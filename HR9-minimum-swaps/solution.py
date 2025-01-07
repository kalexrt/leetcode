#!/bin/python3

import math
import os
import random
import re
import sys

        
# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    swaps=0
    for i in range(len(arr)):
        v = arr[i]
        while i != v-1:
            swaps += 1
            temp = arr[i]
            arr[i] = arr[v-1]
            arr[v-1] = temp
            v = arr[i]
    return swaps 
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
