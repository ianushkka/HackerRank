#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    new=""
    new+=s[0].capitalize()
    for i in range(1,len(s)) :
        if s[i-1]==" " :
            new+=s[i].capitalize() 
            
        else :
            new+=s[i]
            
    return new
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
