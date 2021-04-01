s = 'hello world'

i = 0
while i < len(s) and s[i] != 'w':
    i += 1

if i < len(s):
    print("The letter 'W' was found at position", i,'in the string.')
else:
    print("The letter 'W' was not found in the string.")
