# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque
n=int(input())
data=deque()
for i in range(n):
    arr=input().split()
    if(arr[0]=="append"):
        data.append(int(arr[1]))

    if(arr[0]=="appendleft"):
        data.appendleft(int(arr[1]))

    if(arr[0]=="pop"):
        data.pop()

    if(arr[0]=="popleft"):
        data.popleft()   

    if(arr[0]=="reverse"):
        data.reverse()
print(*list(data))

