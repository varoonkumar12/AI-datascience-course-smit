import math
def func_Circle(radius):
    area= math.pi*(radius**2)
    circumference= 2*math.pi*radius
    return area,circumference

r= float(input("Enter value of radius:"))
area,circumference=func_Circle(r)

print(" Area of circle is  ",area)
print("Circumference of circle is ",circumference)
