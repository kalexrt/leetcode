#!/bin/python3

import math
import os
import random
import re
import sys
# Complete the countTriplets function below.

def countTriplets(arr, r):
    arr.sort()
    dict1 = {}
    keys = []
    for i in arr:
        if i in dict1.keys():
            dict1[i] += 1
        else:
            dict1[i] = 1
            
    keys = list(dict1.keys())
    print(dict1)

    count = 0
    if r != 1:
        for i in keys:
            try:
                first = dict1[i]
                second = dict1[i*r]
                third = dict1[i*r*r]
                count += 1 + first - 1 + second -1 + third -1
            except:
                continue
    else:
        count = 0
        for i in keys:
            if dict1[i] > 2:
                count += math.comb(dict1[i],3)
    return count
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nr = input().rstrip().split()

    n = int(nr[0])

    r = int(nr[1])

    arr = list(map(int, input().rstrip().split()))

    ans = countTriplets(arr, r)

    fptr.write(str(ans) + '\n')

    fptr.close()
