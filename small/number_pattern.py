# Write a Python program to construct the following pattern, using a nested loop number.
# 1
# 22
# 333
# 4444
# 55555
# 666666
# 7777777
# 88888888
# 999999999


# Function for the pattern
def pattern(n):
    # creating the loop to print the numbers in patterns within range of 1 - 10
    # row loop
    for i in range(1, n):

        # nested loop or column loop
        for j in range(1, i+1):
            # printing stars
            print(i, end=" ")

        # ending line after each row
        print("\r")


# Driver Code
n = 10
pattern(n)
print("")
