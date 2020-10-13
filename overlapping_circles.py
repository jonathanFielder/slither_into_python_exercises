#user inputs radius and x y plot for 2 circle
#tests if the circles overlap, their center point distances, and how far they overlap or how far the are from touching

import math
def overlapping_circles():
    c1x = float(input('Enter x for circle 1: '))
    c1y = float(input('Enter y for circle 1: '))
    c1r = float(input('Enter radius for circle 1: '))

    c2x = float(input('Enter x for circle 2: '))
    c2y = float(input('Enter y for circle 2: '))
    c2r = float(input('Enter radius for circle 2: '))

    dist_cent = math.sqrt(((c1x - c2x)**2) + ((c1y - c2y)**2))
    comb_rad = c1r + c2r
    rad_dif = (c1r - c2r)
    if rad_dif < 0:
        rad_dif = rad_dif * -1
    dist_edge = (dist_cent - comb_rad)

    
    if dist_cent == 0:
        print ('These circles are perfectly centered together.')
        if rad_dif == 0:
            print('The edges are aligned.')
        else:
            print ('The edges are ' + str(rad_dif) + ' units apart.')
    elif dist_cent != 0:
        print('Distance from center of each circle is: ' + str(dist_cent))
        if dist_edge > 0:
            print('These circles are not overlapping')
            print('Minimum distance between circles is: ' + str(dist_edge) + ' units.')
        elif dist_edge < 0:
            print('These circles are overlapping by a maximum ditance of ' + str(dist_edge * -1) + ' units.')
           
        else:
            print('The circles are perfectly touching on the edge')

while True:

    overlapping_circles()    
