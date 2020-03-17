# Enter your code here. Read input from STDIN. Print output to STDOUT
n,k=list(map(int,input().split()))
data=[]
for i in range(k):
    data.append(map(float,input().split()))
for i in zip(*data):
    print(sum(i)/len(i))
