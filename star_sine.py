#prints stars in a row up to the entered number then back down to 1 incrementing 1 each row
def star_sine(x):
    i = 1
    star = '*'
    while i < x:
        print (star*i)
        i += 1
    while i > 0:
        print (star*i)
        i -= 1


while True:
    try:
        star_sine(int(input('Enter max of star sine: ')))
    except:
        print('Non intiger value!')
        
    
