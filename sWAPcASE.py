def swap_case(s):
    v=""
    for i in s:
        #print(i)
        if(i.isalpha()):
            
            if(i.isupper()):
                
                v+=i.lower()
            else:
                v+=i.upper()
        else:
            v+=i
    return v

if __name__ == '__main__':
