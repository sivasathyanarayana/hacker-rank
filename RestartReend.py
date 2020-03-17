# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
n=input()
s=input()
p=re.compile(s)
#print(p)
r=p.search(n)
#print(r)
if not r:
    print((-1,-1))
while(r):
    print("({}, {})".format(r.start(),r.end()-1))
    r=p.search(n,r.start()+1)
#m=re.search(s,n)
#print(m.start(),m.end())
