#  Write a Python program to construct the following pattern, using a nested for loop.
# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *


# Functions for the pattern
# forward pattern
def forward_draw(n):
    # creating the loop to print the numbers in patterns within range of 1 - 10
    # row loop
    for i in range(1, n):

        # nested loop or column loop
        for j in range(1, i+1):
            # printing stars
            print("*", end=" ")

        # ending line after each row
        print("\r")


# backward_pattern
def backward_draw(n):
    # creating the loop to print the numbers in patterns within range of 1 - 10
    # row loop
    for i in range(n, 1, -1): 

        # column loop   
        for j in range(1, i - 1):  
            print("*", end=' ')

        # ending line after each row
        print("\r")


# Driver Code
n = int(input("Enter the number to draw the pattern: ").strip())
print("")
forward_draw(n)
backward_draw(n)
print("")
