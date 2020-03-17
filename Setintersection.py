# Enter your code here. Read input from STDIN. Print output to STDOUT
n1=int(input())
data1=set(map(int,input().split()))
n2=int(input())
data2=set(map(int,input().split()))
d=data1.intersection(data2)
print(len(d))
