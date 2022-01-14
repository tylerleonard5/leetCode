#imports of sys, numpy, and literal_eval from ast

from pickletools import int4
import sys
import numpy as np
from ast import literal_eval
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
    arr1 = np.array(literal_eval(lines[0]))
    
    #if set length does not equal then not set
    if len(np.array(list(arr1evalSet))) != len(arr1):
        isValid = False

    #if dtype of array is not int32 then not valid
    if arr1.dtype != np.int32 and arr1.dtype != np.int64:
        isValid = False
       
   
    #arr2
    arr2 = np.array(literal_eval(lines[1]))
    
    #if set length does not equal then not set
    if len(np.array(list(arr2evalSet))) != len(arr2):
        isValid = False

    #if dtype of array is not int32 then not valid
    if arr2.dtype != np.int32 and arr2.dtype != np.int64:
        isValid = False
 

    #tup
    tup = np.array(literal_eval(lines[2]))

    #must be int32
    if tup.dtype != np.int32 and tup.dtype != np.int64:
        isValid = False

    #can be set but length must be 2
    if len(tup) != 2:
        isValid = False

        
    if not isValid:
        print(-1)
        
    else:
        cart = np.transpose([np.repeat(arr1, len(arr2)), np.tile(arr2, len(arr1))])

        tupVal = tuple([arr1[tup[0]], arr2[tup[1]]])

        ans = np.where((cart==tupVal).all(axis=1))[0]

        print(int(ans))

        