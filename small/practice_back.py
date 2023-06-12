def backward_draw(n):
    # creating the loop to print the numbers in patterns within range of 1 - 10
    # row loop
    for i in range(n, 0, -1): 

        # column loop   
        for j in range(0, i - 1):  
            print("*", end=' ')

        # ending line after each row
        print("\r")


# Driver Code
n = 10
print("")
backward_draw(n)
print("")