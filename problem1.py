# write a program to find the greatest of four numbers entered by the user.
a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
c=int(input("Enter third number:"))
d=int(input("Enter fourth number:"))

if (a>b and a>c and a>d):
    print("Greatest number is a:",a)
if (b>a and b>c and b>d):
    print("Greatest number is b:",b)
if (c>a and c>b and c>d):
    print("Greatest number is c:",c)
if (d>a and d>b and d>c):
    print("Greatest number is d",d)