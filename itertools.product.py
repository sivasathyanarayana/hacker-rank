# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product
def prod(arr1,arr2):
    result=product(arr1,arr2)
    print(*list(result))

arr1=list(map(int,input().split()))
arr2=list(map(int,input().split()))
arr=[]
arr.append(arr1);arr.append(arr2)
prod(arr1,arr2)
