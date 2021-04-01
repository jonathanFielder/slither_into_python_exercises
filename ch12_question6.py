def rep_all(lis,targ,des):
    i = 0
    while i < len(lis):
        if lis[i] == int(targ):
            lis[i] = int(des)
        i += 1

        
            
        

a = [4, 2, 3, 3, 7, 8]
rep_all(a, 3, 10)
print(a)
