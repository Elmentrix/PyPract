# Write a Python program to check a triangle is valid or not.

# taking inputs from user
a = float(input("Enter first size of the triangle: ").strip()) # takes out any whitespaces in the input
b = float(input("Enter first size of the triangle: ").strip())
c = float(input("Enter first size of the triangle: ").strip())
print("")

# checking through for the validity of the triangle
if (a + b >= c) and (a + c >= b) and (b + c >= a):
    print("Triangle is valid")
else:
    print("Triangle is not valid")
print("")

user = 1        
