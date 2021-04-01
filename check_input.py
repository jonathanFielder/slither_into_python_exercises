#checks if number or letter input then prints result
while True:
    user_in = input('Enter something here: ')
    if user_in.isalpha():
        print('This is letters.')
    elif user_in.isdigit():
        print('This is numbers.')
        print(str(int(user_in) * 2) + ' I multiplied it by two for you.')
    else:
        print('Non valid input')
