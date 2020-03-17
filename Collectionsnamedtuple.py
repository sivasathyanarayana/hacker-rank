# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import namedtuple
n=int(input())
Student=namedtuple('Student',input().split())
s=[];sum=0
for i in range(n):
    sum+=int((Student(* (input().split()))).MARKS)
#data=Student.Marks.__doc__
print(sum/n)
