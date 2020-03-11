if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    arr2=[]
    for i in range(n):
        if arr[i] not in arr2:
            arr2.append(arr[i])
    arr2.sort()
    print(arr2[-2])
