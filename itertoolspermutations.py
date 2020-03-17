# Enter your code here. Read input from STDIN. Print output to S
from itertools import permutations
inp=input().split()
string=inp[0]
size=int(inp[1])
result=list(permutations(string,size))
result.sort()
for i in result:
    print("".join(i))

