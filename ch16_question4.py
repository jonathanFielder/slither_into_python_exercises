def is_palindrome(word):
    #print(word)
    if len(word) <= 1:
        return True
    if word[0] == word[-1]:
        return is_palindrome(word[1:-1])
    else:
        return False
    



def main():
    #runtime testing
    test = ['racecar', 'pizza', 'bob']
    
    for i in test:
        print(is_palindrome(i))
        



if __name__ == '__main__':
    main()


    
        
    
