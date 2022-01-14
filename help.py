#imports of sys, numpy, and literal_eval from ast
import sys
import numpy as np
from ast import literal_eval
from itertools import product
# import pandas as pd
# from sklearn import ...

#get input
lines = sys.stdin.readlines()

#check for correct length of inputs
if(len(lines) != 3):
    print(-1)
   
else:
    #Must be O(1) so no loops to check, use numpy dtype
    #checks for valid, must be set so no repeating, and must be int32 dtype
    isValid = True

    #initialize set
    arr1evalSet = set(literal_eval(lines[0]))
    arr2evalSet = set(literal_eval(lines[1]))

    #arr1
    arr1 = literal_eval(lines[0])
    
    #if set length does not equal then not set
    if len((list(arr1evalSet))) != len(arr1):
        isValid = False

    #if element in array is letter then not valid
    for i in arr1:
        if not isinstance(i, int):
            isValid = False
            break
       
   
    #arr2
    arr2 = literal_eval(lines[1])
    
    #if set length does not equal then not set
    if len((list(arr2evalSet))) != len(arr2):
        isValid = False

    #if element in array is letter then not valid
    for i in arr2:
        if not isinstance(i, int):
            isValid = False
            break
 

    #tup
    tup = literal_eval(lines[2])

    #must be int
    for i in tup:
        if not isinstance(i, int):
            isValid = False
            break

    #can be set but length must be 2
    if len(tup) != 2:
        isValid = False

    #If the input is not valid print -1    
    if not isValid:
        print(-1)

    #else valid.  i * len(B) represents start point in cartesian set. add j to that to
    #get proper index
    else:
        print((tup[0] * len(arr2)) + tup[1])

        