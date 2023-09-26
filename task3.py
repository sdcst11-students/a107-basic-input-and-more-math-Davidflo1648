#!python3

# Heron's formula is a method of finding the area of a any triangle if you know the lengths of 3 sides.

'''
write a program to calculate the area of a triangle provided the 3 sides are known:
sample:
I will use Heron's formula to find the area of a triangle provided that all 3 sides are known.
You will need to enter the lengths of the 3 sides: a, b and c

Enter the length of side a: 3
Enter the length of side b: 5
Enter the length of side c: 7

Your half perimeter is 7.5
The area of your triangle is 6.495



I will use Heron's formula to find the area of a triangle provided that all 3 sides are known.
You will need to enter the lengths of the 3 sides: a, b and c

Enter the length of side a: 5
Enter the length of side b: 12
Enter the length of side c: 12

Your half perimeter is 14.5
The area of your triangle is 29.342
'''

import math

def calculate_area():
    
    a, b, c = map(float, input("Enter the lengths of the three sides separated by commas: ").split(","))
    print()
    h=(float("Enter your half perimeter: "))
    
    area = math.sqrt(h * (h - a) * (h - b) * (h - c))
    
    print(f"The area of the triangle with sides {a}, {b}, and {c} is {area:.4f} square units.")

calculate_area()
