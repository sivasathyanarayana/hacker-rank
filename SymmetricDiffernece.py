# Enter your code here. Read input from STDIN. Print output to STDOUT

n1=int(input())
d1=list(map(int,input().split()))
d1=set(d1)
n2=int(input())
d2=list(map(int,input().split()))
d2=set(d2)
d3=d1.union(d2)
d4=d1.intersection(d2)
d=d3-d4
d=list(d)
d.sort()
for i in d:
    print(i)
