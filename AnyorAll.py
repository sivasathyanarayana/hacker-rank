# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
list1=list(map(int,input().split()))
a=all([i>0 for i in list1])
b=any([str(i)==str(i)[::-1] for i in list1])
print(a and b)

