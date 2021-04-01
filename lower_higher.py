#not proud of this, could definitely use improvement

def lower_higher():
    i = 0
    keep_going = True
    while keep_going == True:
        if i == 0:
            try:
                number = float(input('Enter first number: '))
                if number == 0:
                    print('this is 0... bye')
                    keep_going = False
                i += 1
            except:
                print('Not valid number!')
        
        if i != 0 and keep_going == True: #checking if i incremented as a non number entry won't add to i
            try:
                compare = float(input('Enter number to compare to the last number: '))
                if compare == 0:
                    print('this is 0... bye')
                    keep_going = False
                elif compare < number:
                    print('Number is less than the last one.')
                elif compare > number:
                    print('Number is greater than the last one.')
                elif compare == number:
                    print('This is the same number stupid.')
                else:
                    print('Something broke...')
                number = compare
            except:
                print('Not valid number!')

lower_higher()
        
