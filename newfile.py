In [1]:
#write a python program to design simple calculator
#addition of two numbers
a=int(input('Enter a value'))
b=int(input('Enter b value'))
print('the addition of two numbers is', a+b)
Enter a value10
Enter b value15
the addition of two numbers is 25
In [2]:
#subtraction of two numbers
a=int(input('Enter a value'))
b=int(input('Enter b value'))
print('the subtraction of two numbers is', a-b)
Enter a value50
Enter b value25
the subtraction of two numbers is 25
In [3]:
#multiplication of two numbers
a=int(input('Enter a value'))
b=int(input('Enter b value'))
print('the multiplication of two numbers is', a*b)
Enter a value2
Enter b value3
the multiplication of two numbers is 6
In [5]:
#Division of two numbers
a=int(input('Enter a value'))
b=int(input('Enter b value'))
print('the division of two numbers is', a/b)
Enter a value20
Enter b value10
the division of two numbers is 2
In [6]:
#reminder of two numbers
a=int(input('Enter a value'))
b=int(input('Enter b value'))
print('the reminder of two numbers is', a%b)
Enter a value22
Enter b value12
the reminder of two numbers is 10
In [8]:
#exponent
a=int(input('enter the number'))
b=int(input('enter the power of that number'))
print('the addition of two numbers is', a**b)
enter the number2
enter the power of that number5
the addition of two numbers is 32
In [9]:
#floor division
a=int(input('Enter a value'))
b=int(input('Enter b value'))
print('the floor division of two numbers is', a//b)
Enter a value22
Enter b value12
the floor division of two numbers is 1
In [11]:
#write a phython program to calculate simple interest
p=float(input('Enter the principal value'))
r=float(input('Enter the rate of interest'))
t=int(input('Enter the time period'))
s=float((p*r*t)/100)
print('The simple interest is' ,s)
Enter the principal value12
Enter the rate of interest10
Enter the time period5
The simple interest is 6.0
In [15]:
#write a program to calculate area of circle
pi=3.14
r=float(input('Enter the radius of circle'))
print('Area of circle is', pi*r*r )
Enter the radius of circle6
Area of circle is 113.03999999999999
In [19]:
#write a program to calculate area of triangle
a=float(input('Enter first side'))  
b=float(input('Enter second side'))  
c=float(input('Enter third side'))
s=float(a + b + c) / 2
Area=(s*(s-a)*(s-b)*(s-c))** 0.5
print('The area of the triangle is', Area)
Enter first side5
Enter second side6
Enter third side7
The area of the triangle is 14.696938456699069
In [23]:
#write a program to temp in Celsius to Fahrenheit
c=float(input('The temp in Celsius'))
f=(celsius*1.8)+32
print('the temp in fahrenheit is' ,fahrenheit)
The temp in Celsius37.5
the temp in fahrenheit is 99.5
In [24]:
#write a program to calculate area of rectangle
w=float(input('Please Enter the Width of a Rectangle'))
h=float(input('Please Enter the Height of a Rectangle'))
print(" Area of a Rectangle is" ,w*h)