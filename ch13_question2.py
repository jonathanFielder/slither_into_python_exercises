def insert(lis, elem):
    h = len(lis)
    low = 0
    i = 0

    while h > low:
        mid = (h + low) // 2
        if elem > lis[mid]:
            low = mid + 1
        else:
            h = mid
        #print(low)
    lis.insert(low,elem)
    return(lis)




listen = [1,2,3,4,5,6,7,8,10]
print(insert(listen, 9))




    
