# Write a program to find greatest of four numbers entered by the user.
# Get four numbers from the user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))
num4 = float(input("Enter fourth number: "))

# Compare numbers using conditional statements
if num1 >= num2 and num1 >= num3 and num1 >= num4:
    greatest = num1
elif num2 >= num1 and num2 >= num3 and num2 >= num4:
    greatest = num2
elif num3 >= num1 and num3 >= num2 and num3 >= num4:
    greatest = num3
else:
    greatest = num4

# Display the result
print("The greatest number is:", greatest)

#output
#Enter first number: 12
#Enter second number: 45
#Enter third number: 33
#Enter fourth number: 27
#The greatest number is: 45.0