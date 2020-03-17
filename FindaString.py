def count_substring(string, sub_string):
    sl=len(sub_string)
    nl=len(string)
    c=0
    for i in range(nl):
        if(string[i:i+sl]==sub_string):
            c=c+1

    return c

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
