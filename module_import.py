import ch16_question3

power_check = ch16_question3.power_check
while True:
    try:
        print(power_check(float(input('Enter a number to see if it is a power of two: '))))
    except:
        print('Input must be a number!')
        
