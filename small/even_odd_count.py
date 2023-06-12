# Count the number of even and odd numbers from a series of numbers
# Input 
# numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9) # Declaring the tuple
# Output
# Number of even numbers : 4                                                                                    
# Number of odd numbers : 5 

# function for separations and display
def counter(arr):
    even = [value for value in arr if value%2 == 0]
    odd = [value for value in arr if value%2 != 0]

    return odd, even

def display(od, ev, user_input):
    print("\n" + "User Input: " + str(user_input) + "\t Total Number: " + str(len(user_input)))
    print("Even Numbers: " + str(ev) + "\t\t Total Even Numbers: " + str(len(ev)))
    print("Odd Numbers: " + str(od) + "\t\t Total Odd Numbers: " + str(len(od)) + "\n")


# taking input from user
user_input = tuple(map(int, input("Enter the numbers separating each with a space: ").strip().split()))
od, ev = counter(user_input)
display(od, ev, user_input)
