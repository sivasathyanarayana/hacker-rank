# Enter your code here. Read input from STDIN. Print output to STDOUT
input1=list(map(int,input().split()))
data=list(map(int,input().split()))
A=set(map(int,input().split()))
B=set(map(int,input().split()))
happiness=0
for i in data:
    if(i in A):
        happiness+=1
    elif(i in B):
        happiness-=1
print(happiness)
