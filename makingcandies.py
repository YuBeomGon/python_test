https://www.hackerrank.com/challenges/making-candies/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=search


#!/bin/python3

import math
import os
import random
import re
import sys

def add_days (x,y,works):
#     if x < y :
#         return x+works, y
#     else :
#         return x,y+works
    
# def add_days1 (x,y,works) :
#     if x < y :
#         x = y+math.ceil((works-y+x)//2)
#         y = y+math.floor((works-y+x)//2)
#     else :
#         x = x+math.ceil((works-x+y))//2
#         y = x+math.floor((works-x+y))//2
#     return x,y
        
# def checkPasses(m, w, p, n, midday) :
#     left = 0
#     works = 0
#     # 3 1 2 12  

#     for i in range(midday) :
#         # print(m, w, p, n)
#         if m*w + left > n :
#             return True        
#         works = (m*w+left)//p
#         left = (m*w+left)%p
#         if abs(m-w) >= works :
#             m,w = add_days(m,w,works)
#         else :
#             m,w = add_days1(m,w,works)

#     return False

# # Complete the minimumPasses function below.
# binary search, but time out, and wrong answer
# def minimumPasses(m, w, p, n):
#     # minday = 0
#     minday = max(math.floor(math.sqrt(n)/m), math.floor(math.sqrt(n)/w) )
#     maxday = n//(m*w) + 1
#     # 3 1 2 12    
#     while ( minday < maxday) :
#         midday = (minday + maxday)//2
#         if checkPasses(m, w, p, n, midday) :
#             maxday = midday
#         else :
#             minday = midday+1
#         print(minday, maxday)
#     return minday


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    mwpn = input().split()
    m = int(mwpn[0])
    w = int(mwpn[1])
    p = int(mwpn[2])
    n = int(mwpn[3])
    result = minimumPasses(m, w, p, n)
    fptr.write(str(result) + '\n')
    fptr.close()
