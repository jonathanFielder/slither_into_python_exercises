def contains(lis, elem):
    h = len(lis)
    low = 0
    i = 0

    while h > low:
        mid = (h + low) // 2
        if elem > lis[mid]:
            low = mid + 1
        else:
            h = mid
        print(low)
    if elem == lis[low]:
        return(True)
    else:
        return(False)




listen = [1,2,3,4,5,6,7,8,10]
print(contains(listen, 9))




    
