#calculates total amount of rabbits over a specified time based on begining number of rabbits input by user
while True:
    rabbits = int(input('enter num of rabbits:'))
    years = 4
    months_in_year = 12
    months_to_double = 3

    x = years * months_in_year / months_to_double   
    print(x)
    while x > 0:
        x = x - 1
        rabbits = rabbits * 2

    print(rabbits)
