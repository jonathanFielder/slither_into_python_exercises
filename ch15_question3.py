import sys


def file_list():
    #open file and create word list split
    with open(sys.argv[1], 'r') as file:
        lines = file.read()
        words = lines.split()
        return(words)

def comp_list(los):
    #takes list and builds new list with only words greater than 18
    len_18_plus = [x for x in los if len(x) >= 18]
    return(len_18_plus)




def main():
    len_plus = comp_list(file_list())
    print(len_plus)
    print('Amount of words more than or equal to 18 character length is:', len(len_plus))





if __name__ == '__main__':
    main()

