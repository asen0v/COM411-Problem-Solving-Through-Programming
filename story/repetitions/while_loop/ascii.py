# Task for creating a program to display ASCII chars for the robot

print("How many bars should be charged?")
barstobe = int(input())

bars = 0

while (bars < barstobe):
    bars = bars + 1
    print("Charging:", "█" * bars)
print("The battery is fully charged.")

