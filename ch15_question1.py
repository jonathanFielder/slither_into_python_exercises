import sys

def file_list():
    #open file in read and return list
    with open(sys.argv[1], 'r') as file:
        items = file.read()#need to make a list with each word
        list_items = items.split()
    return(list_items)

def list_set(lis):
    #make set out of list and return
    unique_names = set(lis())
    
    return(unique_names)






def main():
       #print(list_set(file_list))
       print(len(list_set(file_list)))
   




if __name__=='__main__':
    main()
