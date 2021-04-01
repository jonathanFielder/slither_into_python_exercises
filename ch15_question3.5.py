import sys


def file_list():
    #open file and create word list split
    with open(sys.argv[1], 'r') as file:
        lines = file.read()
        words = lines.split()
        return(words)

def comp_list(los):
    #takes list and builds new list with only words greater than 18
    vowels = set('aeiou')
    all_vow = [x for x in los if all([char in x for char in vowels])]
    return(all_vow)




def main():
    all_vowels = comp_list(file_list())
    print(all_vowels)
    print('Amount of words with every vowel is:', len(all_vowels))





if __name__ == '__main__':
    main()

