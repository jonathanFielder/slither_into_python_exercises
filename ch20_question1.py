#%%
class Person:
    def __init__(self, name = 'John Doe', age = 0):
        self.name = name
        self.age = age

    def __str__(self):
        return('Name is: {} \nAge is: {}'.format(self.name, self.age))


4
class Employee(Person):
    def __init__(self, name = 'John Doe', age = 0, employee_id = 0) :
        super().__init__(name, age)
        self.employee_id = employee_id
        self.clocked_in = False

    def clock_in(self):
        if self.clocked_in == False:
            self.clocked_in = True
            print('{} Has Clocked In.'.format(self.name))
        else:
            print('{} Is Already Clocked In.'.format(self.name))

    def clock_out(self):
        if self.clocked_in == True:
            self.clocked_in = False
            print('{} Has Clocked Out.'.format(self.name))
        else:
            print('{} Is Not Clocked In So Cannot Clock Out.'.format(self.name))

def main():
    man = Person()
    do = Employee('phil', 22, 4443)
    moo = Employee()
    print(man)
    print(do)
    do.clock_out()
    do.clock_in()
    do.clock_out()
    print(moo)


if __name__ == '__main__':
    main()



