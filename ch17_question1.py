
class Lamp:
    def __init__(self, name):
        self.name = name
        self.is_on = False
        self.plugged_in = False


    
    def plug(self):
        
        if self.plugged_in == False:
            self.plugged_in = True
        else:
            self.plugged_in = False
        
        
    def toggle(self):
        
        if self.is_on == True:
            self.is_on = False
        else:
            self.is_on = True
        



def main():
    #create lamp object here
    la = 'lamptest'
    lamp = Lamp(la)
    #plugin and turn on here
    lamp.plug()
    print(lamp.is_on)
    lamp.toggle()
    print(lamp.is_on)
    print(lamp.name)
    
    
   
    
        



if __name__ == '__main__':
    main()


    
        
    


