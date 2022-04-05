#program to calculate the perimeter and area of the hexagon
side=float(input("enter a length of the side:", ))
import math as m
perimeter=6*side
area=((3*m.sqrt(3))/2*(side*side))
print("perimeter of the hexagon:", perimeter)
print("area of the hexagon:",area)
