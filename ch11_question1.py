
stock_dict = {}
with open('stock.txt', 'r') as f:
    longest = 0
    for line in f.readlines():
        item_and_stock = line.strip().split()

        item = ' '.join(item_and_stock[:-1])
        
        if len(item) > longest:
            longest = len(item)
        stock = item_and_stock[-1]
        stock_dict[item] = stock
        #print(longest)
for (k,v) in sorted(stock_dict.items()):
    print('{:>{}} : {}'.format(k,longest,v))
        
        
