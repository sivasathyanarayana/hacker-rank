if __name__ == '__main__':
    N = int(input())
    v=[]
    for i in range(N):
        name, *list=input().split()
        if(name=="insert"):
            index=int(list[0])
            value=int(list[1])
            v.insert(index,value)
        #print(v)
        if(name=="print"):
            print(v)
        if(name=="remove"):
            val=int(list[0])
            v.remove(val)
        if(name=="append"):
            val=int(list[0])
            v.append(val)
        if(name=="sort"):
            v.sort()
        if(name=="pop"):
            v.pop(-1)
        if(name=="reverse"):
            v=v[::-1]

