def length(a):
    i = 0
    for item in a:
        i += 1
    return(i)


def main():
    lis = [1,2,3,4,5,6,7,8]
    dic ={1:'a',2:'b',3:'c',4:'d'}
    word = 'hello'
    #testing
    print(length(lis),length(dic),length(word))
        
if __name__=='__main__':
    main()
