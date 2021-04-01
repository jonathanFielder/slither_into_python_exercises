from random import randint

def binary_search(arr,targ):
    h = len(arr)
    low = 0
    guesses = []
    i = 0
    

    while h > low and i < 20:
        mid = (h + low) // 2
        if targ > arr[mid]:
            low = mid + 1
        else:
            h = mid
        guesses.append(low)
        i += 1

    #if i < 20:
    return( guesses)
        



art = [x for x in range(0, 1000000)]
secret = randint(0, len(art))
answer = binary_search(art,secret)

print('Secret is:', secret)
print( 'List of guesses:', answer)
print('Amount of guesses:', len(answer))
