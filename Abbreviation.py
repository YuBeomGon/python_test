https://www.hackerrank.com/challenges/abbr/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dynamic-programming

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the abbreviation function below.
def abbreviation(a, b):
    
    dp = [ [0]*(len(b)+1) for i in range(len(a)+1)]
    dp[0][0] = 1
    # print(dp)
    # for i in range(1,len(b)+1) :
    #     dp[0][i] = 0
    for i in range(1, len(a)+1) :
        if a[i-1].islower() and dp[i-1][0] > 0 :
            dp[i][0] = 1
        # else :
        #     dp[i][0] = 0
    # print(dp)
    
    for i in range(1, len(a)+1) :
        for j in range(1, len(b)+1) :
            if dp[i-1][j-1] > 0 and a[i-1].upper() == b[j-1] :
                dp[i][j] = 1
            if dp[i-1][j] > 0 and a[i-1].islower() :
                dp[i][j] = 1
    
    return 'YES' if dp[-1][-1] == 1 else 'NO'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    q = int(input())
    for q_itr in range(q):
        a = input()
        b = input()
        result = abbreviation(a, b)
        fptr.write(result + '\n')
    fptr.close()
