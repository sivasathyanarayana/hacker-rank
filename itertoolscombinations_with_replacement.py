# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations,combinations_with_replacement
inp=input().split()
string=inp[0]
size=int(inp[1])
string=list(string)
#print(string)
string.sort();string="".join(string)

result1=combinations_with_replacement(string,size)
for i in result1:
    print("".join(i))
