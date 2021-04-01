import sys


def file_set():
    #open file and create word list split
    try:
        with open(sys.argv[1], 'r') as file:
            words = {word.strip() for word in file}
            return(words)
    except:
        with open('words_alpha.txt', 'r') as file:
            words = {word.strip() for word in file}
            return(words)

def comp_list(words):
    #takes list and builds new list with only words greater than 18
    
    for_rev = [x for x in words if x[::-1] in words]
    return(for_rev)




def main():
    reversables = comp_list(file_set())
    print(reversables)
    print('Amount of words that also have backwards counterparts is:', len(reversables))





if __name__ == '__main__':
    main()

