def fizz_buzz():
    x = 1
    total = 100
    while x <= total:
        if x % 3 == 0 and x % 5 != 0:
            print('fizz')
        elif x % 5 == 0 and x % 3 != 0:
            print('buzz')
        elif x % 3 == 0 and x % 5 == 0:
            print('fizz-buzz')
        else:
            print(str(x))
        x += 1



def fizz_buzz_1():
    x = 1
    total = 100
    div1 = 3
    div2 = 5
    while x <= total:
        if x % div1 == 0 and x % div2 == 0:
            print('fizz-buzz')
        elif x % div1 == 0:
            print('fizz')
        elif x % div2 == 0:
            print('buzz')
        else:
            print(str(x))
        x += 1

fizz_buzz_1()
        
