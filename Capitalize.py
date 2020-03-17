#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    result=""
    result=result+s[0].upper()
    for i in range(1,len(s)):
        if(s[i-1]==" "):
            result=result+s[i].upper()
        else:
            result+=s[i]
    return result
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
