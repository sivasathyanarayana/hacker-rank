cube = lambda x: x**3# complete the lambda function 

def fibonacci(n):
    # return a list of fibonacci numbers
    arr=[]
    a=0
    b=1
    if(n>=1):
        arr.append(a)
    if(n>1):
        arr.append(b)
    for i in range(n-2):
        c=a+b
        arr.append(c)
        a=b
        b=c
    return arr

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
