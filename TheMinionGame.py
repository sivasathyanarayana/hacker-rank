def minion_game(string):
    # your code goes here
    p=0
    k=0
    stuart=0
    con="bcdfghijklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    vowel="AEIOUaeiou"
    for i in string:
        if((i not in vowel)or(p==1)):
            if(i not in vowel):
                k=k+1
            stuart=stuart+k
            p=1
    p=0
    k=0
    kevin=0
    for i in string:
        if((i in vowel)or(p==1)):
            if(i in vowel):
                k=k+1
            kevin=kevin+k
            p=1
    if(stuart>kevin):
        print("Stuart {}".format(stuart))
    elif(stuart<kevin):
        print("Kevin {}".format(kevin))
    else:
        print("Draw")
if __name__ == '__main__':
    s = input()
    minion_game(s)
