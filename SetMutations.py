# Enter your code here. Read input from STDIN. Print output to STDOUT

n=int(input())
set1=set(map(int,input().split()))
n1=int(input())
for i in range(n1):
    data=input().split()
    if(data[0]=="update"):
        set2=set(map(int,input().split()))
        set1.update(set2)
    elif(data[0]=="intersection_update"):
        set2=set(map(int,input().split()))
        set1.intersection_update(set2)
    elif(data[0]=="symmetric_difference_update"):
        set2=set(map(int,input().split()))
        set1.symmetric_difference_update(set2)
    elif(data[0]=="difference_update"):
        set2=set(map(int,input().split()))
        set1.difference_update(set2)
print(sum(set1))
