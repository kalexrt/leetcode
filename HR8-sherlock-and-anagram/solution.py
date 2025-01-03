#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict
#
# Complete the 'sherlockAndAnagrams' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def sherlockAndAnagrams(s):
    # Optimization: Using sorted substrings to avoid repeatedly checking for anagrams
    substrings = defaultdict(int)
    count = 0

    # Generate all substrings
    for length in range(1, len(s)):  # From length 1 to len(s)-1
        for start in range(len(s) - length + 1):
            substring = s[start:start + length]
            # Sorting the substring creates a unique "key" for all anagrams
            sorted_substring = ''.join(sorted(substring))
            substrings[sorted_substring] += 1

    # Count the pairs of anagrams
    for freq in substrings.values():
        if freq > 1:
            # If there are `freq` occurrences of the same sorted substring,
            # The number of pairs is given by the combination formula: freq * (freq - 1) // 2
            count += (freq * (freq - 1)) // 2

    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')

    fptr.close()
