def fib(x):
    i = 0
    a = 1
    b = 0
    ind = int(x)
    while i <= ind:
        #below is to test a and b
        #print('a' + str(a))
        #print('b' + str(b))
        n = (a) + (b)
        if a < 1:
            a += 1
        elif i % 2 != 0:
            a = n
        else:
            b = n
        i += 1
        if i == ind or ind == 0:
            return(n)
    

def main():
    while True:
        print('This module returns the index from the Fib sequence based off of index input.')
        print(fib(input('Enter an index number for the Fib sequence: ')))


if __name__=='__main__':
    main()
