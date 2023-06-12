# Write a Python program that accepts a string and calculate the number of digits and letters
# Sample Data : "Python 3.2"
# Expected Output :
# Letters 6 
# Digits 2


# User input
user = input("Enter any alpanumeric text of choice: ").replace(" ", "").strip()

# checking through the user inputs
apha = [alpha for alpha in user if alpha.isalpha()]
num = [nam for nam in user if nam.isdigit()]
# sym = [sim for sim in user if sim.s]

# output
print("")
print("User Input: " + user + " Total User Input: " + str(len(user)))
print("Aphabets in Inputs: " + ' '.join(map(str, apha)) + "\t Total Alphabets: " + str(len(apha)))
print("Numbers in Input: " + ' '.join(map(str, num)) + "\t Total Numbers: " + str(len(num)))
# print("Symbols in Input: " + sym + " Total Symbols: " + str(len(sym)))
print("")