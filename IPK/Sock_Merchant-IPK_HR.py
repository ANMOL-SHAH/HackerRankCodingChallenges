import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
#logic Starts from here
def sockMerchant(n, ar):
    dict = {}
    se = list(set(ar))
    #Looping and checking the frequency of each item
    for i in range(0,len(se)):
        dict[se[i]] = 0
        for x in range(0,len(ar)):
            if(se[i]==ar[x]):
                dict[se[i]] = dict[se[i]] + 1
    result = 0            
    for x in dict.values():
        
        y = x%2
        result = result + y
        #result shows no of unpaired items
    #x is final answer    
    x = (n - result)/2
    return x
    
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input())

    ar = map(int, raw_input().rstrip().split())

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()

