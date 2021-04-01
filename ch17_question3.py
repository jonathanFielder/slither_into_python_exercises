class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.grades = {}

    def add_module(self, mod):
        self.grades[mod] = 0

    def update_module_grade(self, mod, grade):
        self.grades[mod] = grade

    def show_grades(self):
        print("{}'s grades are:".format(self.name))
        for i in self.grades:
            print('{}: {}'.format(i, self.grades[i]))


def main():
    print('This module contains class "Student" with 4 functions:'
        '\ninit("name","age") -when creating a student object it will take two arguments: name and age'
        '\nadd_module("module name") -adds a module to grades dict with default grade of 0'
        '\nupdate_module_grade("existing module name", "grade for that module") -updates grade for module in grades dict'
        '\nshow_grades() -prints modules and grades for selected student')

if __name__ == '__main__':
    main()



