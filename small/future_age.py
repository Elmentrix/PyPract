# Create a program that asks the user to enter their name and their age.
# Print out a message addressed to them that tells them the year that they will turn 100 years old.

from datetime import date

# first take input from user
name = input("\n Enter your name: ")
age = int(input("Enter your current age: "))
print("")

# getting current date and slicing the year out of the date
today = str(date.today())
current_year = int(today[:4])

# subtracting the current age from the 100 years to get remaining age
more_to_100 = 100 - age

# adding the years left to get to 100 to get the future year
future = current_year + more_to_100

# printing a letter out based on the input and process
print("""
Hello {name}. From the information you provided, you are currently {age} years old
as of today, {date}. Your will be 100 years old in {more_to_100} years time in the year {future}. 
\n
Thank you and stay blessed.
""".format(name = name, age = age, date = today, more_to_100 = more_to_100, future = future))
