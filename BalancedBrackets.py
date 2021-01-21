#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the isBalanced function below.
def isBalanced(s):
    
    s = s.replace('(', '1')
    s = s.replace('[', '2')
    s = s.replace('{', '3')
    s = s.replace(')', '4')
    s = s.replace(']', '5')
    s = s.replace('}', '6')
    
    # print(s)
    
    mstack = []
    for i in range(len(s)) :
        if int(s[i]) < 4 :
            mstack.append(s[i])
        else :
            if len(mstack) == 0 :
                return 'NO'
            if int(mstack.pop())%3 != int(s[i])%3 :
                return 'NO'
# print(mstack)
    if len(mstack) > 0 :
        return 'NO'
                    
    return 'YES'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()
