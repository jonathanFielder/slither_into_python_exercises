import sys


file = open(sys.argv[1], 'r')
content = file.readlines()
#print(content)


for i in range(len(content)):
    pal = True
    a = 0
    b = -1
    while a < len(content[i]) and pal == True:
        content[i] = content[i].lower()
        content[i] = content[i].strip('\n')
        content[i] = content[i].replace(' ','')
        #print(content[i])
        #print(content[i][a]) #these three lines are for testing
        #print(content[i][b])
        if content[i][a] == content[i][b]:
            a += 1
            b -= 1
        else:
            pal = False
    print(pal)







    


