# simple app to perform arithmetic calculations based on user input

# function to perform calculations based on user input
def calculate(inp1, inp2, op):
    if (op == "+"):
        result = inp1 + inp2
    elif(op == "-"):
        result = inp1 - inp2
    elif(op == "/"):
        result = inp1 / inp2
    elif(op == "*"):
        result = inp1 * inp2
    elif(op == "^"):
        result = inp1 ** inp2
    elif(op == "mod"):
        result = inp1 % inp2
    return result

# user inputs:
inp1 = float(input("Enter the first number: "))
op = input("Operator to apply (+, -, /, *, ^, mod): ")
inp2 = float(input("Enter the second number: "))

# fetch processed data from calculate function into result
result = calculate(inp1, inp2, op)

# displaying user result basd on process
print(str(inp1) + " " + " " + str(op) + " "  + " " + str(inp2) + " = " + str(result))

