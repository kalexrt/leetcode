#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumBribes' function below.
#
# The function accepts INTEGER_ARRAY q as parameter.
#

def minimumBribes(q):
    count = 0
    index = len(q) - 1
    while index != 0:
        if q[index] == index + 1:
            pass
        elif q[index-1] == index + 1:
            count += 1
            q[index], q[index - 1] = q[index - 1], q[index]
        elif q[index-2] == index + 1:
            count += 2
            q[index-1], q[index - 2] = q[index - 2], q[index-1]
            q[index], q[index - 1] = q[index - 1], q[index] 
        else:
            print("Too chaotic")
            return None  
        index -= 1
    print(count)
    return count
                
            
            
            

if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
