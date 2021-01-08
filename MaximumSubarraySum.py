
hackerrank
Maximum Subarray Sum
https://www.hackerrank.com/challenges/maximum-subarray-sum/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=search

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maximumSum function below.
def maximumSum(arr, m):
    arr = [a%m for a in arr]
    maxarr = max(arr)
    prefix = []
    cur = 0
    # print(arr)
    # prefix = [cur for i in range(len(arr)) ]
    for i in range(0,len(arr)) :
        cur = (cur + arr[i])%m
        # if cur != 0:
        #     prefix.append(cur)
        prefix.append(cur)
    # prefix.insert(0,0)
    # prefix.append(0)
    print('누적값 ' ,prefix)
    maxpre = max(prefix)
    predict = {}
    for i in range(len(prefix)) :
        predict[prefix[i]] = i
    # print('dictionary ', predict)
    
    keylist = list(predict.keys())
    # print(keylist)
    keylist.sort()
    print('keylist sorting ' ,keylist)  
    
    diff = m
    # prev = keylist[0]
# 누적값  [0, 3, 6, 1, 3, 1]
# dictionary  {0: 0, 3: 4, 6: 2, 1: 5}
# [0, 3, 6, 1]
# keylist sorting  [0, 1, 3, 6]   
    difflist = []
    # for i in range(1, len(keylist)) :
    #     difflist.append((keylist[i] - keylist[i-1]))
    # print(difflist)
    for i in range(1, len(keylist)) :
        # print(keylist[i],predict[keylist[i]] )
        # print(keylist[i] - keylist[i-1])
        if keylist[i] - keylist[i-1] < diff and predict[keylist[i]] < predict[keylist[i-1]] and keylist[i] - keylist[i-1] > 0 :
            diff = keylist[i] - keylist[i-1]
    return max(m-diff, maxarr, maxpre)
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    q = int(input())
    for q_itr in range(q):
        nm = input().split()
        n = int(nm[0])
        m = int(nm[1])
        a = list(map(int, input().rstrip().split()))
        result = maximumSum(a, m)
        fptr.write(str(result) + '\n')
    fptr.close()    
