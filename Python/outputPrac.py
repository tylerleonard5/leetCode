import sys

arrLines = []
for lines in sys.stdin.readlines(): 
    arrLines.append(lines.strip())

print(arrLines)