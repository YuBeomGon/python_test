https://www.hackerrank.com/challenges/candies/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dynamic-programming

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the candies function below.
def candies(n, arr):
    candy1 = [1]
    for i in range(len(arr)-1) :
        if arr[i+1] > arr[i] :
            candy1.append(candy1[i]+1)
        else : 
            candy1.append(1)
    # print(candy1)
    candy2 = [1]
    for i in range(len(arr)-1, 0, -1) :
        if arr[i-1] > arr[i] :
            candy2.append(candy2[len(arr)-1-i]+1)
        else :
            candy2.append(1)
    # print(candy2)
    candy2 = candy2[::-1]
    
    candy = []
    for i, j in zip(candy1, candy2) :
        candy.append(max(i,j))
    
    # print(candy)
    return sum(candy)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())
    arr = []
    for _ in range(n):
        arr_item = int(input())
        arr.append(arr_item)
    result = candies(n, arr)
    fptr.write(str(result) + '\n')
    fptr.close()
