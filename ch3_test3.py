ch = 12
x = 0
print('1st sequence:')

while ch > 0:
    ch = ch - 1
    x = x + 2
    print('x = ' + str(x))


ch = 12
x = 0
print('2nd sequence:')

while ch > 0:
    ch = ch - 1
    x = x - 1
    print('x = ' + str(x))


ch = 12
x = -6
print('3rd sequence:')

while ch > 0:
    ch = ch - 1
    x = -x
    print('x = ' + str(x))


ch = 12
x = -9
print('4th sequence:')

while ch > 0:
    ch = ch - 1
    x = x + 3
    if x > 0:
        x = -6
    print('x = ' + str(x))
