# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
regrex=r'^[+-]?[0-9]*\.[0-9]+$'
for i in range(int(input())):
    d=re.search(regrex,input())
    if(d):
        print(True)
    else:
        print(False)
