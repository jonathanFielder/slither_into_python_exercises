import sys
import string


file = open(sys.argv[1], 'r', encoding='utf-8')
content = file.read()
#print(content)


symbols = string.punctuation
#symbols += '"\''
print(symbols)
content = content.lower()


for i in content:
    if i in string.punctuation:
        content = content.replace(i, ' ')
    if i.isalpha() == False and i.isnumeric() == False: #catching the pesky punctuation from wierd quotes
        content = content.replace(i, ' ')
        
    
        
        
        
#print(content)
#print(len(content))
list_words = content.split()
#print(len(list_words))
no_rep = []
for i in list_words:
    if i not in no_rep:
        no_rep.append(i)
        
print(len(no_rep))
#print(no_rep)
    
    








    


