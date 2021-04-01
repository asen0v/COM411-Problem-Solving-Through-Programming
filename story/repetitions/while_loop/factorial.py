# Task for finding the factorial of a number

print("Please enter a number:")
num = int(input())
count = 0
totall = 1

while ( count < num ):
    count = count + 1
    totall = totall * count

print("The factorial is ", totall)