# Enter your code here. Read input from STDIN. Print output to STDOUT
n,m=input().split()
s=".|."
n=int(n)
m=int(m)
for i in range(1,(n//2)+1):
    print((s*(2*i-1)).center(m,"-"))
string="WELCOME".center(m,"-")
print(string)
for i in range(n//2,0,-1):
    print((s*(2*i-1)).center(m,"-"))
