def one_plus(a):
    if a == 0:
        return 0
    else:
        return a + one_plus(a-1)
        
        


def main():
    print(one_plus(100))



if __name__ == '__main__':
    main()
