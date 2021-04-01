def make_dict():
    contact_dict = {}
    with open('contacts.txt', 'r') as f:
    
        for line in f.readlines():
            contact = line.strip().split()
            #print(contact)
            name = ' '.join(contact[0:1])
            #print(name)
            info = contact[1:3]
            #print(info)
           
            
            contact_dict[name] = info
    return contact_dict


def dict_search(dic,q):
    if q in dic():
        return q, dic()[q]
    else:
        return 'No such name in contacts'




while True:
    con = dict_search(make_dict,input('Enter name to search contacts: '))
    try:
        print(' Name:',con[0],'\nEmail:', con[1][1],'\nPhone:', con[1][0])
    except:
        print(con)

        

        
     
