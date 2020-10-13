def odd_even_checker():
    number = int(input('Enter a number: '))
    if (number % 2) == 0:
        print(str(number) + ' is an even number.')
    else:
        print(str(number) + ' is an odd number.')


while True:
    odd_even_checker()
             
