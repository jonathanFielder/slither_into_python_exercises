def add(*a):
    result = 0
    for arg in a:
        result += arg
    return(result)

def subtract(*a):
    result = a[0]
    i = 1
    if len(a) >= 2:
        while i < len(a):
            result = result - a[i]
            i += 1
    else:
        result = -a[0]
    return(result)

def multiply(*a):
    result = 1
    for arg in a:
        result = result * arg
    return(result)

def divide(*a):
    if len(a) == 2:
        result = a[0]/a[1]
        return(result)
    else:
        return('Must divide 2 numbers.')





def main():
    
    
   
    print('add example:', add(5,3,6,4,6))
    print('subtract example:', subtract(5,3,6,4,6))
    print('multiply example:', multiply(5,3,6,4,6))
    print('divide example:', divide(5,3,6,4,6))
    print('dividing only the first two numbers:', divide(5,3))
    


if __name__=='__main__':
    main()
