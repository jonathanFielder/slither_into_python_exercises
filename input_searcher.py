def text_searcher():
    text = input('Enter a lot of text here to search through: ')
    search = input('What word would you like to search for in the last entry? ')
    found = 0
    start = 0
    start = text.find(search)
    while start != -1:
        found += 1
        start = text.find(search, start+1)
    print('Search item found', found, 'times.')

while True:
    text_searcher()
