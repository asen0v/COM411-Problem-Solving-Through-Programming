# Task for calculating the sum of the first 100 numbers

print("Calculating the sum of the first 100 numbers...")

number = 0
total = 0
while (number < 101):
    total = total + number
    number = number + 1

print("...Done! The answer is", total)