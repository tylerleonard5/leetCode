import numpy as np
import sys
from ast import literal_eval

lines = sys.stdin.readlines()

print(lines)

if len(lines) != 3:
    print("Invalid")

else:
    arr1eval = literal_eval(lines[0])
    arr2eval = literal_eval(lines[1])
    tup = literal_eval(lines[2])
    isDigit = True

    for i in arr1eval:
        if (type(i) == int):
            continue
        else:
            isDigit = False

    for i in arr2eval:
        if (type(i) == int):
            continue
        else:
            isDigit = False

    for i in tup:
        if (type(i) == int):
            continue
        else:
            isDigit = False
    if not isDigit:
        print("Invalid")

    else:
        arr1 = np.array(literal_eval(lines[0]))
        arr2 = np.array(literal_eval(lines[1]))

        cart = np.transpose([np.repeat(arr1, len(arr2)), np.tile(arr2, len(arr1))])
        ans = []
        print(cart)

        for i in range(len(cart)):
            if(cart[i][0] == arr1[tup[0]] and cart[i][1] == arr2[tup[1]]):
                print(i)
                break

    