import sys
inform = 'Run with "-info" as only argument to learn more.'

#script information
def info():
    print('This script needs to be run in command line with at least one int arguement.')
    print('It will print the arguement mulitplied in a range from 1 to 10.')
    print('-s can be used as an arguement before the number to print without the equation.')
    print('-f can be used as an arguement before the number to neatly format the information.')


#returns multiples of num arguement from 1 to 10
def multiples(num):
    mults = []
    i = 1
    while i <= 10:
       mults.append(i * num)
       i += 1
    return(mults)


#returns int version of number argument
def make_int(num):
    try:
        num = int(num)
        return(num)
        
    except:
        raise Exception('Input not a valid number!', inform)


#checks that formatting arguements are valid
def check_in(syn):
    if syn != '-f' and syn != '-s':
        raise Exception('Invalid syntax arguements!\nMust be "-s" or "-f".', inform)


#prints formatted answer based on arguements given by user
def printing(f,s,inp,nums):
    #find longest num
    num_form = 0
    for p in nums:
        if len(str(p)) > num_form:
            num_form = len(str(p))
           


    
    i = 1
    while i <= 10:
        if s == True:
            if f == True:
                print('{bum:{width}}'.format(bum = nums[i-1], width = num_form))
                #format answers no eqasion
            else:
                print(nums[i-1])
        elif f == True:
                print('{:>2}'.format(i),'*',inp,'=','{bum:{width}}'.format(bum = nums[i-1], width = num_form))
            #format answer and equation

        elif f == False and s == False:
            print(i,'*',inp,'=',nums[i-1])
            

        i += 1
       

        
#handles arguements given by user and if all is valid calls printing() for output
def arguement_handling():
    argu = sys.argv
    syn1 = 0
    syn2 = 0
    f = False
    s = False
    
    
    if len(argu) < 2:
        raise Exception('Needs an arguement to work properly!', inform)
    if len(argu) == 2:
        if argu[1] == '-info':
            info()
            return
        else:
            num = make_int(argu[1])
    elif len(argu) == 3:
        num = make_int(argu[2])
        syn1 = argu[1]
        check_in(syn1)
    elif len(argu) == 4:
        num = make_int(argu[3])
        syn1 = argu[1]
        syn2 = argu[2]
        check_in(syn1)
        check_in(syn2)
    elif len(argu) > 4:
        raise Exception('Too many arguements!', inform)

    if syn1 == '-f' or syn2 == '-f':
        f = True
    if syn1 == '-s' or syn2 == '-s':
        s = True

    answers = multiples(num)
    
    printing(f,s,num,answers)
        

        
            
            
def main():
    arguement_handling()
    
    



   
        





if __name__=='__main__':
    main()
