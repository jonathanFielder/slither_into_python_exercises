def countdown(n):
    i = 0
    while i < n:
        print(n-i)
        n-1 #after print so the number entered prints before subtracting
        i+=1

while True:
    countdown(int(input('Enter number to count down from: ')))
