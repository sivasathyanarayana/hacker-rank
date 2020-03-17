# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
for i in range(n):
    n1=int(input())
    set1=set(map(int,input().split()))
    n2,set2=int(input()),set(map(int,input().split()))
    print(set1.issubset(set2))
