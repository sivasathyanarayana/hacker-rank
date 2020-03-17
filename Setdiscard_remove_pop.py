n = int(input())
s = set(map(int, input().split()))

n1=int(input())
for i in range(n1):
    data=input().split()
    if(data[0]=="remove"):
        s.remove(int(data[1]))
    elif(data[0]=="discard"):
        s.discard(int(data[1]))
    elif(data[0]=="pop"):
        s.pop()
    
print(sum(s))
