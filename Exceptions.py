# Enter your code here. Read input from STDIN. Print output to STDOUT

n=int(input())
for i in range(n):
    try:
        data=input().split()
        d=int(data[0])//int(data[1])
        print(d)
    except ZeroDivisionError as e:
        print("Error Code:",e)
    except ValueError as e:
        print("Error Code:",e)
