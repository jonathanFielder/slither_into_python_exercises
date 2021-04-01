
class Student:
    STUDNUM = 19343553
    def __init__(self, name):
        self.name = name
        self.grades = {}
        self.student_number = Student.STUDNUM
        Student.setNextStudentNum()

    def add_module(self, module_name):
        self.grades[module_name] = 0

    def update_module(self, module_name, grade):
        self.grades[module_name] = grade

    @classmethod
    def setNextStudentNum(cls):
        cls.STUDNUM += 1

    def __str__(self):
        string = '{} \nStudent Number: {} \nGrades:'.format(self.name, self.student_number)
        for i in self.grades:
            string += ('\n{}: {}'.format(i, self.grades[i]))
        return(string)

    @staticmethod
    def isValidGrade(grade):
        return(0 <= grade <= 100)

def main():
    john = Student("John")
    john.add_module("Python")
    print(john.isValidGrade(88))
    print(Student.isValidGrade(101))
    john.update_module("Python", 88)
    print(john)
    adam = Student("Adam")
    adam.add_module("Java")
    adam.update_module("Java", 60)
    print(adam)

if __name__ == '__main__':
    main()