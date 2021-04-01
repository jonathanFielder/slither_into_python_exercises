import math
class Shape:
    def __init__(self, num_sides, side_len):
        self.num_sides = float(num_sides)
        self.side_len = float(side_len)

    def show_type(self):
        sides = self.num_sides
        shapes = ['void', 'line', 'non shape', 'triangle', 'square', 'pentagon', 'hexagon', 'heptagon']
        if sides <= 7:
            print('I am a {}'.format(shapes[int(sides)]))
        else:
           print('I am a shape.')

class Triangle(Shape):
    def __init__(self, side_len):
        super().__init__(3, side_len)
    
    def area(self):
        a = (math.sqrt(3)/ 4)*(self.side_len * self.side_len)
        print(a)

class Pentagon(Shape):
    def __init__(self, side_len):
        super().__init__(5, side_len)

    def area(self):
        a = (math.sqrt(5 * (5 + 2 * (math.sqrt(5)))) * self.side_len * self.side_len) / 4
        print(a)

def main():
    shape = Shape(7, 2)
    shape.show_type()
    triangle = Triangle(3)
    triangle.show_type()
    triangle.area()
    pent = Pentagon(4)
    pent.show_type()
    pent.area()

if __name__ == '__main__':
    main()