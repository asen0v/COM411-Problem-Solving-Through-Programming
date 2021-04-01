# Task for summing user numbers

print("How many numbers should I sum up?")
numbers = int(input())
koe = 0

print()

suma = 0

while (koe < numbers):
    print("Please enter number ", koe+1, "of ", numbers)
    chislo = int(input())
    suma = suma + chislo
    koe = koe + 1

print("The sum of the numbers is: ", suma)