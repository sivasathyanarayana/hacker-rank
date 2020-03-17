# Enter your code here. Read input from STDIN. Print output to STDOUT
k=int(input())
arr=list(map(int,input().split()))
data=set(arr)
sumdata=sum(data)*k
sumarr=sum(arr)
result=(sumdata-sumarr)//(k-1)
print(result)
