# Python program to find Area of a circle using inbuild library

import math
def area(r):
    area = math.pi* pow(r,2)
    return print('Area of circle is:' ,area)
n = int(input("Enter radius of circle : "))
area(n)

