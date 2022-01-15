import sys 
from ast import literal_eval

#create n-ary tree.  Traverse tree for leafnodes and if leafnode
#is target currency get value in an array.  get max value in that
#array

#node class
class Node(object):
    def __init__(self, name, value):
        self.name = name
        self.value = value
        self.children = []
        
        
#function that takes in root and creates tree
def createTree(root):
    for i in arrRates:
        #we want to have leaf nodes equal to targCurr. Base case
        if(root.name == targCurr):
            return
        
        #if first index and not in visited then multply rates
        if(i[0] == root.name and not i in visited):
            temp = Node(i[1], i[2] * root.value)
            root.children.append(temp)
            visited.append(i)
            #recursion on this node in case alt path
            createTree(temp)
        
        #if second we need to get inverse because that is valid conversion
        elif (i[1] == root.name and not i in visited):
            #round to two decimals
            temp = Node(i[0], round(1 / i[2], 2) * root.value)
            root.children.append(temp)
            visited.append(i)
            createTree(temp)
    #if the passed in root is not targcurr or in the conversion
    #array we have the case of a leafnode that does not equal target
    #the returnvalFrmTree function will acount for this when calculating
    #values
    return

#function that gets leafnodes and adds target curr values to array
def returnValfrmTree(root):
    #we are manipulating values so attach global keyword
    global values
    
    #evaluate children
    for i in root.children:
        #if leaf node
        if(len(i.children) == 0):
            #if name of leaf node is targ then append value
            if(i.name == targCurr):
                values.append(i.value)
            #else do nothing
        
        
        #else there are children so call recursive to check its 
        #children
        else:
            returnValfrmTree(i)
    #returns if leafnode, outside of for loop
    return


#start
lines = sys.stdin.readlines()


rates = lines[0].splitlines()[0]
listInput = rates.split(';')

arrRates = []


#add values into arrRates
for i in listInput:
    temp = i.split(',')
    #conversion to float for rate
    temp[2] = literal_eval(temp[2])
    arrRates.append(temp)

    
#orig and targ currency
origCurr = lines[1].splitlines()[0]
targCurr = lines[2].splitlines()[0]

#edge case: currencies equal so print 1
if(origCurr == targCurr):
    print(float(1))
    
else:
    #create root node that is origCurr and value of 1
    root = Node(origCurr, 1)
    #initiliaze a visited array to properly create tree
    #in create tree the program traverses the array given
    #we want to ensure that we do not access the same 
    #conversion in the array more than once
    visited = []
    
    createTree(root)
    
    #initialize a values array that will store values from orig
    #curr to target curr from leafnodes in tree
    values = []
    
    #pass in root to this function.  this will traverse tree
    #to lead nodes.  If leaf node is target curr, add the value
    #at that leaf node to the values array
    returnValfrmTree(root)
    
    #initialize max
    max = 0
    
    #if there are no values in the values array, that indicates
    #that there was not a valid conversion. print -1
    if (len(values) == 0):
        print(float(-1))
    
    
    #else find and print max value in array
    else:
        for i in values:
            if i > max:
                max = i
        print(max)