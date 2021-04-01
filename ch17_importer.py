
from ch17_question1 import Lamp
import sys

lamp_inc = 1 #starting point
lamp_ar = []
current_lamp = ''
sec = True

invalid_txt = 'Invalid Entry!'

def new_lamp():
    global lamp_ar
    global lamp_inc
    lamp_ar.append( Lamp('lamp' + str(lamp_inc)))
    new_name = 'lamp' + str(lamp_inc)
    lamp_inc += 1
    return(new_name)

def lamp_selector(sel):
    global current_lamp
    global sec
    try:
        if int(sel) <= len(lamp_ar):
            sel = int(sel)
            sel = sel - 1
            print('You have selected {}'.format(lamp_ar[sel].name)) #sel in lamp_ar
            current_lamp = (lamp_ar[sel])
            sec = True
            #print(current_lamp)
        elif int(sel) == len(lamp_ar) + 1:
            first_level()
        else:
            print(invalid_txt)
            first_level()
    except:
        print('An error has occurred. Entry may not have been a valid number.')
        first_level()


def on_off(la):
    #global current_lamp
    if la.is_on == True:
        return('on')
    else:
        return('off')

def plug_state(la):
    #global current_lamp
    if la.plugged_in == False:
        return('unplugged')
    else:
        return('plugged in')


def first_level():
    
        print('Enter the number coresponding to your command:')
        print('1: Create New Lamp \n2: Select Lamp \n3: List Lamps \n4: Exit')
                    
        current = input()

        if current == '1':
            print('{} has been created.'.format(new_lamp()))
            
            

        elif current == '2':
            if len(lamp_ar) > 0:
                inc = 1
                
                for item in lamp_ar:
                    print('{}: {}'.format(inc, item.name))
                    inc += 1
                print('{}: Main Menu'.format(len(lamp_ar)+1))
                lamp_selector(input('Enter the number for the lamp you want: '))
                second_level()
            else:
                print('No lamps exist yet! You must'
                    ' create a new lamp before picking one. \n')

        elif current == '3':
            if len(lamp_ar) > 0:
                for i in lamp_ar:
                    print('{} is turned {} and is {}.'.format(i.name,on_off(i), plug_state(i)))
            else:
                print('No lamps exist yet! You must'
                    ' create a new lamp before picking one. \n')

        elif current == '4':
            print('Goodbye! \nPress Enter key to exit...')
            input()
            sys.exit()

        else:
            print(invalid_txt)

def second_level():
    global sec
    while sec == True:
        global current_lamp
        #print(current_lamp.name) #test that lamp is selected
        print('Select the action you would like performed on {}:'.format(current_lamp.name))

        #eventually make choice to unplug lamp
        if current_lamp.plugged_in == False:
            print('1: Plugin Lamp')
        else:
            print('1: Unplug Lamp') 
        print('2: Toggle Switch \n3: Check Lamp \n4: Rename Lamp \n5: Delete Lamp \n6: Main Menu')

        current = input()
        
        if current == '1':
            current_lamp.plug()
            #print(current_lamp.is_on)
            print('{} is turned {} and is {}.'.format(current_lamp.name,on_off(current_lamp), plug_state(current_lamp)))

        elif current == '2':
            current_lamp.toggle()
            print('{} is turned {} and is {}.'.format(current_lamp.name, on_off(current_lamp), plug_state(current_lamp)))

        elif current == '3':
            print('{} is turned {} and is {}.'.format(current_lamp.name, on_off(current_lamp), plug_state(current_lamp)))

        elif current == '4':
            print('Enter the new name you would like for {}.'.format(current_lamp.name))
            temp = current_lamp.name
            current_lamp.name = input()
            print('{} will be renamed to {}.'.format(temp, current_lamp.name))
            print('Would you like to save this change?')
            print('1: Yes \n2: No')
            c = input()
            if c == '1':
                print('Henceforth, ye shall be known as {}.'.format(current_lamp.name))
            elif c == '2':
                print('Name will be reverted to {}.'.format(temp))
                current_lamp.name = temp
            else:
                print(invalid_txt, 'Name will be reverted to {}.'.format(temp))
                current_lamp.name = temp

        elif current == '5':
            print('Are you sure you want to delete {}?'.format(current_lamp.name))
            print('1: Yes \n2: No')
            c = input()
            if c == '1':
                
                lamp_ar.remove(current_lamp)
                print('{} has been destroyed.'.format(current_lamp.name))
                sec = False
            elif c == '2':
                print('{} thanks you for your mercy.'.format(current_lamp.name))
            else:
                print(invalid_txt, '{} will be spared.'.format(current_lamp.name))
            


        elif current == '6':
            print('Returning to the main menu.')
            sec = False
        
        else:
            print(invalid_txt)

while True:
    first_level()
    
            #do stuff with returned lamp



                
    
    
    
 


