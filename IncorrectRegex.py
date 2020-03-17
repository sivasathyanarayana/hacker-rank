# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

n=int(input())
for i in range(n):
    d=input()
    try:
        print(bool(re.compile(d)))
    except:
        print(False)
