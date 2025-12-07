"""
When all the lenght of the sides of the the traingkes is know : q,b,c
Formula is
First find semi perimeter s= (a+b+c)/2
Area= square root of (s*(s-a)*(s-b)*(s-c))
"""

a= float(input("Enter first side: "))
b= float(input("Enter second side: "))
c= float(input("Enter third side: "))
s= (a+b+c)/2
print(s)
area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
print("The area of Triangle with the given side is", round(area,2))