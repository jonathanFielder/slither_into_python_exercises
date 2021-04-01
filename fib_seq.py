#an attempt at a pure functional Fib sequence that returns a list and no side effects
def fib_to(x):
    results = []
    i = 0
    a = 0
    b = 0
    while i < x:
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
        results.append(n)
    return results

while True:
    try:
        print(fib_to(int(input('Enter number to generate Fib: '))))
    except:
        print('Non numeric value!')
    
    
