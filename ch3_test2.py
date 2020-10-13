#flips x y assignment from user input
x = int(input('enter 1st num:'))
y = int (input('enter second num:'))


z = x
x = y
y = z

print(str(x) +' ' + str(y))
