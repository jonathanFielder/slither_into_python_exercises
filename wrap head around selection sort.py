a = [4,6,3,6,3,4,23,53,6,363,45]
i = 0
while i < len(a):
    p = i
    j = i + 1
    while j < len(a):
        if a[j] < a[p]:
            p = j
        j += 1
    
    tmp = a[p] #set lowest number to temp
    print('tmp',tmp)
    a[p] = a[i] #set lowest num position to number at start of sequence
    print('a[p]',a[p])
    a[i] = tmp #set first position of sequence to lowest num from pass
    print('a[i]',a[i])
    i += 1
    print(a)
    
print(a)
