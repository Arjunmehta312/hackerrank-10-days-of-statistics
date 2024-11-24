#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'quartiles' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def quartiles(arr):
    # Write your code here
    arr.sort()
    n = len(arr)
    
    # Calculate Q2
    if n % 2 == 0:
        q2 = (arr[n // 2 - 1] + arr[n // 2]) // 2
    else:
        q2 = arr[n // 2]
    
    # Split array into lower and upper halves
    if n % 2 == 0:
        lower_half = arr[:n // 2]
        upper_half = arr[n // 2:]
    else:
        lower_half = arr[:n // 2]
        upper_half = arr[n // 2 + 1:]
    
    # Calculate Q1
    m = len(lower_half)
    if m % 2 == 0:
        q1 = (lower_half[m // 2 - 1] + lower_half[m // 2]) // 2
    else:
        q1 = lower_half[m // 2]
    
    # Calculate Q3
    m = len(upper_half)
    if m % 2 == 0:
        q3 = (upper_half[m // 2 - 1] + upper_half[m // 2]) // 2
    else:
        q3 = upper_half[m // 2]
    
    return [q1, q2, q3]




if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    data = list(map(int, input().rstrip().split()))

    res = quartiles(data)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
