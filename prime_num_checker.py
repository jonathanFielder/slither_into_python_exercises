#checks if user input number is prime

def prime_num_check(x):
    i = 2
    while i < x and (x % i) != 0:
        i += 1
        #the below is to check if incrementing correctly
        #print('i' + str(i))
        #print('x' + str(x))
    if i < x:
        return('Your number is not a prime number.')
    else:
        return('Your number is a prime number!')

while True:
    res = prime_num_check(int(input('Enter number to check if it is prime: ')))
    print(res)
    
