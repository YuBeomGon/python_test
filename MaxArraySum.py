https://www.hackerrank.com/challenges/max-array-sum/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dynamic-programming

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maxSubsetSum function below.
def maxSubsetSum(arr):
    maxsum = []
    maxsum.append(max(arr[0], 0))
    maxsum.append(max(arr[1], maxsum[0]))
    # print(maxsum[0], maxsum[1])
    for i in range(2, len(arr)) :
        maxsum.append(max(maxsum[i-2]+arr[i], maxsum[i-1], maxsum[i-2]))
        
    # print(maxsum)
    return max(maxsum)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    res = maxSubsetSum(arr)
    fptr.write(str(res) + '\n')
    fptr.close()
