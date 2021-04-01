
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    @classmethod
    def fromBirthYear (cls, name, year):
        age = 2020 - year
        return(cls(name, age))


    def __str__ (self):
        return('{} is {} years old.'.format(self.name, self.age))


def main():
    p1 = Person('bill', 46)
    print(p1)
    p2 = Person.fromBirthYear('bob', 1990)
    print(p2)
    print(p1)

if __name__ == '__main__':
    main()