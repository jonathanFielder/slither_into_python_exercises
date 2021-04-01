import sys
import string


file = open('abraham.txt', 'r', encoding='utf-8')
content = file.read()
#print(content)


symbols = string.punctuation

#print(symbols)
content = content.lower()


for i in content:
    if i in string.punctuation:
        content = content.replace(i, ' ')
    if i.isalpha() == False and i.isnumeric() == False: #catching the pesky punctuation from wierd quotes
        content = content.replace(i, ' ')
        
    
        
        
        

list_words = content.split()

word_count = {}
for i in list_words:
    if i in word_count:
        word_count[i] += 1
    else:
        word_count[i] = 1
        
for (k,v) in sorted(word_count.items()):
    print(k,v)
    
    








    


