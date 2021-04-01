def read_file(file):
    line_list = []
    with open(file, 'r') as f:
        for line in f.readlines():
            line_list.append(line.strip('\n'))
        return(line_list)



lines = read_file('contacts.txt')
print(lines)
