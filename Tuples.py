if __name__ == '__main__':
    n = int(input())
    sum=0
    integer_list = map(int, input().split())
    #print(integer_list)
    print(hash(tuple(integer_list)))
