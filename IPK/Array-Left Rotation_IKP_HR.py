#!/bin/python

import math
import os
import random
import re
import sys

# Complete the rotLeft function below.
def rotLeft(a, d):
    modo = d%len(a)
    print(modo)
    arr1 = []
    print(a[0])
    s = 0
    for k in range(0,len(a)):
        s= (k-modo)%len(a)
        
        arr1.insert(s,a[k])
        
    return arr1    
#Less Optimal Solution which results in time out for some of the cases
    # if(d == len(a)):
    #     return a
    # else:
    #     d = d%n
    #     while(d>0):
    #         temp = 0
    #         last = a[0]
    #         change = a[len(a)-1]
    #         for i in range(len(a)-1,0,-1):
    #             temp = a[i-1]
    #             a[i-1] = change
    #             change = temp
    #         a[len(a)-1] = last
    #         d = d -1    
    #     return a    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = raw_input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = map(int, raw_input().rstrip().split())

    result = rotLeft(a, d)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
