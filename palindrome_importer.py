import ch16_question4

power_check = ch16_question4.power_check
while True:
    try:
        print(power_check(float(input('Enter word to find out if it is a palendrome: '))))
    except:
        print('Um... what?')
        
