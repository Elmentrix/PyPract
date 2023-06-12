# Write a Python program which takes two digits m (row) and n (column) as input and generates a two-dimensional array. 
# The element value in the i-th row and j-th column of the array should be i*j.
# Note :
# i = 0,1.., m-1 
# j = 0,1, n-1.
# Input
# Input number of rows: 3                                                                                       
# Input number of columns: 4  
# Output
# [[0, 0, 0, 0], [0, 1, 2, 3], [0, 2, 4, 6]] 

import random

matrix = []  #this is a variable to hold each row for matrix formation

# user input
print('''
The system is to generate random matrix based on the row size and column size you input''')
row = int(input("Enter row size of the matrix: "))
column = int(input("Enter the column size of the matrix: "))

# generating matrix
for i in range(1, row + 1):
    new_row = [] # this is a variable for holding the column values of each row
    for j in range(1, column + 1):
        num = random.randint(0,100)
        new_row.append(num)
    
    matrix.append(new_row)

print("\n" + "Matrix: ", matrix)
print("Type of Matrix: " + str(row) + " * " + str(column) + "\n")