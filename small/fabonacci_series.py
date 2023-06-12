# Write a Python program to get the Fibonacci series between 0 to 50 

def fabo(b, n):
    # initialize the first two numbers of the series
    a = 0
    fab = []

    # loop through the numbers until the series reaches 50
    while b <= n:
        # print(b, end=' ')
        fab.append(b)
        a, b = b, a + b
    print("Fabonacci Sequence: " + str(fab))

def inp():
    arr = list(map(str, input("Enter the range you want to use using colon(:) to separate from lower to higher range: ").strip().split(":")))
    return arr

arr = inp()
size = len(arr)
n = int(arr[-1])
b = int(arr[0])

# checking if input is correct
if (size == 2):
    print("\n" + "Range: " + str(arr))
    fabo(b, n)
    print("")
else:
    print("Range is in accurate, please retype range.")
    
