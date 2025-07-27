#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumAbsoluteDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#
def calc_min_abs_diff(a,b):
    option1 = abs(a-b)
    option2 = abs(b-a)
    if option1 > option2:
        return option2
    return option1

def minimumAbsoluteDifference(arr):
    minimum = 9999999999
    length = len(arr)
    set1 =  set(arr)
    if len(set1) != length:
        return 0
    sort_arr = arr.sort()
    for index1 in range(0,length-1):
        temp = calc_min_abs_diff(arr[index1],arr[index1 + 1])
        
        if temp < minimum:
            minimum = temp

    return minimum
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = minimumAbsoluteDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
