import numpy

def arrays(arr):
    # complete this function
    # use numpy.array
    array=numpy.array(arr,float)
    return array[::-1]

arr = input().strip().split(' ')
result = arrays(arr)
print(result)
