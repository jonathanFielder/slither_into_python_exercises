
import math

class Circle:
    def __init__(self, x_c, y_c, radius):
        self.x_c = x_c
        self.y_c = y_c
        self.radius = radius

    def calc_area(self):
        area = (self.radius * math.pi)**2
        return(area)

        

    def calc_perim(self):
        circ = 2 * math.pi * self.radius
        return(circ)

    def calc_overlaps(self, circ_2):
        that = circ_2
        this = self
        dist_cent = math.sqrt(((this.x_c - that.x_c) ** 2) + ((this.y_c - that.y_c)**2))
        comb_rad = this.radius + that.radius
        dist_edge = dist_cent - comb_rad
        if dist_edge > 0:
            return('Circles do not overlap.')
        elif dist_edge > 0:
            return('Circles overlap.')
        else:
            return('The circles are touching')
        #C1C2 = sqrt((x1 - x2)2 + (y1 - y2)2).
        #pass second circle instance as an arguement to compare to self circle

def main():
    print('This module is to create Circle objects. '
        '\nTo Create a circle one must pass 3 arguements: '
        '"x" coord, "y" coord, and radius')
    print('c = Circle(0,0,1)')
    print('d = Circle(0,0,2)')
    c = Circle(0,0,1)
    d = Circle(0,0,2)
    print('.calc_perim() finds the perimiter of the circle.')
    print('c.calc_perim() = ', c.calc_perim())
    print('.calc_area() finds the area of the circle.')
    print('d.calc_area() = ', d.calc_area())
    print('.calc_overlaps() takes a second circle as an arguement and '
        'checks to see if the two circles overlap.')
    print('c.calc_overlaps(d) = ', c.calc_overlaps(d))
    input('Press Enter key to exit...')

if __name__ == '__main__':
    main()
