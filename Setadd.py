# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
set1=set()
for i in range(n):
    d=input()
    set1.add(d)
print(len(set1))
