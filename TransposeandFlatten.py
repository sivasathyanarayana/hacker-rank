import numpy
arr=[]
ar=list(map(int,input().split()))
for i in range(ar[0]):
    arr1=list(map(int,input().split()))
    arr.append(arr1)
arr=numpy.array(arr)
print(numpy.transpose(arr))
print(arr.flatten())

