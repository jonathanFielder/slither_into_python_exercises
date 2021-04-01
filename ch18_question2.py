import math
class Line:
    def __init__(self, p1 = [0,0], p2 = [0,0]):
        self.p1 = p1
        self.p2 = p2

    def __len__(self):
        p1 = self.p1
        p2 = self.p2
        length = math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)
        
        return(int(length))

    def __add__(self, other):
        new_p1 = [0,0]
        new_p2 = [0,0]
        new_p1[0] = self.p1[0] + other.p1[0]
        new_p1[1] = self.p1[1] + other.p1[1]
        new_p2[0] = self.p2[0] + other.p2[0]
        new_p2[1] = self.p2[1] + other.p2[1]
        return(Line(new_p1, new_p2))

    def __sub__(self, other):
        new_p1 = [0,0]
        new_p2 = [0,0]
        new_p1[0] = self.p1[0] - other.p1[0]
        new_p1[1] = self.p1[1] - other.p1[1]
        new_p2[0] = self.p2[0] - other.p2[0]
        new_p2[1] = self.p2[1] - other.p2[1]
        return(Line(new_p1, new_p2))

    def __mul__(self, numb):
        new_p1 = [0,0]
        new_p2 = [0,0]
        new_p1[0] = self.p1[0] * numb
        new_p1[1] = self.p1[1] * numb
        new_p2[0] = self.p2[0] * numb
        new_p2[1] = self.p2[1] * numb
        return(Line(new_p1, new_p2))
    
    def __str__(self):
        p1 = self.p1
        p2 = self.p2
        return('Line Details: \nPoint 1: ({}, {}) \nPoint 2: ({}, {})'.format(p1[0], p1[1], p2[0], p2[1]))

    def __eq__(self, other):
        if self.p1 == other.p1 and self.p2 == other.p2:
            return(True)
        else:
            return(False)

def main():
    line_1 = Line([1,22], [2,3])
    line_2 = Line([2,5], [2,9])
    print(line_1)
    print(len(line_1))
    line_3 = line_1 + line_2
    print(line_3)
    line_4 = line_1 - line_2
    print(line_4)
    print(line_1 == line_2)
    line_5 = Line([1,22], [2,3])
    print(line_1 == line_5)
    

if __name__ == '__main__':
    main()