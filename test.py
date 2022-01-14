import sys
import numpy as np
from ast import literal_eval



lines = sys.stdin.read().splitlines()

if len(lines) != 3:
    print("Invalid")

else:
    arr1 = literal_eval(lines[0])
    arr2 = literal_eval(lines[1])
    tup = literal_eval(lines[2])
    isDigit = False
    for i in arr1:
        if (type(i) == int):
            continue
        elif (not i.isdigit()):
            isDigit = True
    for i in arr2:
        if (type(i) == int):
            continue
        elif (not i.isdigit()):
            isDigit = True
            
    if isDigit:
        print('Invalid')
    else:
        print(list(product(arr1, arr2)))