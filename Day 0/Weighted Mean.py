#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'weightedMean' function below.
#
# The function accepts following parameters:
#  1. INTEGER_ARRAY X
#  2. INTEGER_ARRAY W
#

def weightedMean(X, W):
    # Write your code here
    weighted_sum = sum(x * w for x, w in zip(X, W))
    # Calculate the sum of weights
    total_weight = sum(W)
    # Calculate weighted mean
    weighted_mean = weighted_sum / total_weight
    # Print result rounded to 1 decimal place
    print(f"{weighted_mean:.1f}")

if __name__ == '__main__':
    n = int(input().strip())

    vals = list(map(int, input().rstrip().split()))

    weights = list(map(int, input().rstrip().split()))

    weightedMean(vals, weights)
