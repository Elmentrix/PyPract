# Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn. Go to the editor
# Sample value of n is 5 
# Expected Result : 615.

user_in = int(input("Enter a number: "))

n1 = int(str(user_in))
n2 = int(str(user_in) + str(user_in))
n3 = int(str(user_in) + str(user_in) + str(user_in))

sum = n1 + n2 + n3
print(sum)