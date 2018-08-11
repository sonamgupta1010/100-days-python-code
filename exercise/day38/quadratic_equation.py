# Solve the quadratic equation ax**2 + bx + c = 0

import cmath


a = float(input('Enter a: '))
b = float(input('Enter b: '))
c = float(input('Enter c: '))

d = (b**2) - (4*a*c)

# find two solutions
sol1 = (-b-cmath.sqrt(d))/(2*a)
sol2 = (-b+cmath.sqrt(d))/(2*a)

print('The solution are {0} and {1}'.format(sol1,sol2))


#output:
#Enter a: 2
#Enter b: 4
#Enter c: 2
#The solution are (-1+0j) and (-1+0j)

