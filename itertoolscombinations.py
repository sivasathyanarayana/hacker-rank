# Enter your code here. Read input from STDIN. Print output to STDOUT

from itertools import combinations
inp=input().split()
string=inp[0]
string=list(string)
string.sort()
string="".join(string)
size=int(inp[1])
#print(size)
for i in range(size-1,-1,-1):
    #print(i)
    result=list(combinations(string,size-i))
    #print(result)
    result.sort()
    for i in result:
        print("".join(i))
        
