def largest(num):
        if len(num) == 1:
            return num[0]
        else:
            m = largest(num[1:])
            print(m)
            if m > num[0]:
                return m
            else:
                return num[0]
    



def main():
    #runtime testing
    test = [3,45,6,4,35,6,34,546,4,7,868,98,678,578,58,6446,36,36,54,47,45,35,54,58,65,734636,568,3]
    
    print(largest([3,45,6,4,35,6,34,546,4,7,868,98,678,578,58,6446,36,36,54,47,45,35,54,58,65,734636,568,3]))
        



if __name__ == '__main__':
    main()


    
        
    
