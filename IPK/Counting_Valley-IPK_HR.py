import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    s_list = list(s)
    result = 0
    r = 0
    CHECK_V = ""
    for i in range(0,len(s)):
        if(s_list[i] == "U"):
            result = result + 1
            
        else:
            result = result -1 
    #Valley is formed when result is 0 which shows the sea level and when we are coming from down to up so last command should be up
    # So when s_list is U and count is 0 Valley count is incremented
        if(result == 0 and (s_list[i] =="U") ):
            r = r + 1
                

       
    return r        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input())

    s = raw_input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
