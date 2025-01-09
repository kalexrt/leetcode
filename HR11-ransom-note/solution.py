#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict
#
# Complete the 'checkMagazine' function below.
#
# The function accepts following parameters:
#  1. STRING_ARRAY magazine
#  2. STRING_ARRAY note
#

def checkMagazine(magazine, note):
    dict1 = defaultdict(int)
    for i in magazine:
        dict1[i] += 1
    for i in note:
        if i in dict1.keys() and dict1[i] >= 1:
            dict1[i] -= 1
        else:
            print("No")
            return None
    print("Yes")
if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    m = int(first_multiple_input[0])

    n = int(first_multiple_input[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)
