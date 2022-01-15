#imports
import sys
from ast import literal_eval

#get input 
lines = sys.stdin.readlines()

#edge case: check for correct input length
if(len(lines) != 3):
    print(-1)
    
else:
    #initialize validity boolean
    isValid = True
    
    #edge case: check if A and B are sets, therefore no repeat elements
    #make sets for A and B to check
    arrAset = set(literal_eval(lines[0]))
    arrBset = set(literal_eval(lines[1]))
    
    #initialize arrA, arrB, and tuple
    arrA = literal_eval(lines[0])
    arrB = literal_eval(lines[1])
    tup = literal_eval(lines[2])
    
    #if set lengths do not equal arr lengths, then invalid
    if(len(list(arrAset)) != len(arrA)):
        isValid = False
        
    if(len(list(arrBset)) != len(arrB)):
        isValid = False
    
    #edge case: has to be integers
    for i in arrA:
        if not isinstance(i,int):
            isValid = False
            break
            
    for i in arrB:
        if not isinstance(i,int):
            isValid = False
            break
            
    #tuple must be integers
    for i in tup:
        if not isinstance(i,int):
            isValid = False
            break
            
            
    #tup must be of length 2
    if len(tup) != 2:
        isValid = False
        
        
    #If isValid is false then validity of inputs failed
    if not isValid:
        print(-1)
        
        
    else:
        #start is i * len(B). A[i] changes at every progression of len(B) 
        startIndex = tup[0] * len(arrB)
        
        #increment from start is equivalent to j, since B[j] changes at every increment in cartesian set
        increment = tup[1]
        
        print(startIndex + increment)