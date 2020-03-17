def print_formatted(number):
    # your code goes here
    w = len("{0:b}".format(number))
    #print(w)
    for i in range(1,number+1):
        #print("{0:{wi}d} {0:{width}o} {0:{width}X}  {0:{width}b}".format(i,oct(i),hex(i),bin(i)))
        print("{} {} {} {}".format((str(i)).rjust(w," "),(str(oct(i)[2:])).rjust(w," "),((str(hex(i)[2:])).upper()).rjust(w," "),(str((bin(i)[2:]))).rjust(w," ")))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
