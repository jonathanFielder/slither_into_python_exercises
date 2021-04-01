def power_check(num):
    print(num)
    if (num % 2) != 0 and (num != 1):
        return('Not a power of two!')
    elif (num == 1):
        return('Number is a power of two.')
    else:
        return(power_check(num/2))



def main():
    #runtime testing
    test = 4
    while test < 200:
        print(power_check(test))
        test += 7
    



if __name__ == '__main__':
    main()


    
        
    
