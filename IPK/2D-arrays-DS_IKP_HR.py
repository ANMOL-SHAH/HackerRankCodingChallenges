#!/bin/python

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    arr1 = [];
    
    for i in range(0,len(arr)-2):
        for j in range(0,len(arr)-2):
            result = 0
            
            result = arr[i][j] + arr[i][j+1]+ arr[i][j+2]+ arr[i+1][j+1]+ arr[i+2][j] + arr[i+2][j+1]+ arr[i+2][j+2]
            arr1.append(result)
    arr12 = sorted(arr1)    
    return arr12[len(arr12)-1]
    



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in xrange(6):
        arr.append(map(int, raw_input().rstrip().split()))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
