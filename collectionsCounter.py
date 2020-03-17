from collections import Counter
n=int(input())
arr=list(map(int,input().split()))
data=Counter(arr)
d=int(input())
total=0
for i in range(d):
    size,cost=list(map(int,input().split()))
    if(size in data and data[size]>0):
        total=total+cost
        data[size]-=1
print(total)

