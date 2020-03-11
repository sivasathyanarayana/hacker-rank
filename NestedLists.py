if __name__ == '__main__':
    l=[]
    v=[]
    n=int(input())
    for _ in range(n):
        name = input()
        score = float(input())
        l.append([name,score])
        v.append(score)
    k=[]
    for i in v:
        if i not in k:
            k.append(i)
    
    k.sort()
    p=k[1]
    
    l.sort()
    for i in range(n):
        if(l[i][1]==p):
            print(l[i][0])
