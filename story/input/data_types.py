# Task to define the body-mass index (bmi) of the person

print("What is your name?")
name = input()
print("How old are you (in years)?")
age = str(input())
print("How tall are you (in meters)?")
tall = float(input())
print("How much do you weight (in kilograms)?")
weight = float(input())
bmii = "{bmi:.2f}"
print(name, " you are ", age, " years old and your bmi is ", bmii.format(bmi = weight/(tall**2)))