num_list = []
tbl_list = ['Radius','Area','Volume']
entry_list = ['Enter starting radius: ','Enter radius incrementer: ','Enter amount to print: ']
a = 0
while a < 3:
    try:
        num_list.append(float(input(entry_list[a])))
        a += 1
    except:
        print('invalid entry! Must be a number.')
        a = 0
    #print(num_list)#testing
rad = num_list[0]
rad_inc = num_list[1]
rad_end = int(num_list[2]//1)
radius_list = []
area_list = []
volume_list = []
pi = 3.14159265359
for a in range(0,rad_end):
    radius_list.append(rad)
    area_list.append(4*pi*(rad**2))
    volume_list.append((4/3)*(pi*(rad**3)))
    rad+=rad_inc
    












for a in range(0,3):
    print('{:>15}'.format(tbl_list[a]),end='')
print()
print('{:>15}'.format('-'*10)*3)

for a in range(0,rad_end):
    print('{:>15.9}{:>15.2f}{:>15.2f}'.format(radius_list[a],area_list[a],volume_list[a]))

