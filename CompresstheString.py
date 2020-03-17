# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import groupby
inp=input()
result=groupby(inp)
for i,j in result:
    print((len(list(j)),int(i)),end=" ")
