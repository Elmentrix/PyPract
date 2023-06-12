#  Write a Python program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700.

# This problem does not require taking any input. Hence, direct application of loop

ranger = []
result = []

for value in range(1500, 2700):
    ranger.append(value)

    # checking for condition
    if (value % 7 == 0) and (value % 5 == 0):
        result.append(value)

print("\n Number from 1500 - 2700: " , ranger)
print("Numbers Divisible by 7 and is a Multiple of 5: " , result , "\n")