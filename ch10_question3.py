import sys


file = open(sys.argv[1], 'r')
content = file.read()
words = content.split()
print(content, len(words))






    


