#user imputs sides of a triangle and code prints if it is a right angle triangle or not
import math #for math.sqrt
def right_angle_triangle_check():
    a = float(input('Enter shortest length: '))
    b = float(input('Enter second shortest length: '))
    c = float(input('Enter longest length: '))
    
    x = math.sqrt(a**2 + b**2)

    if c == x:
        print('This is a right angle triangle.')
    elif c < (x+0.1) and c > (x-0.1): #this is to widen tolerance for decimals
        print('This is aproximatly a right angle triangle.')
    else:
        print('This is not a right angle triangle.')

while True:
    right_angle_triangle_check()
