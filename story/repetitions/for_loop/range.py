# Task for 'for' loop, to determinate brightness for Beep and Bop

print("What level of brightness is required?")
svetlina = int(input())

for count in range(2, svetlina+1, 2):
    print("Adjusting brightness...")
    print("Beep's brightness level:", "*" * count)
    print("Bop's brightness level:", "*" * count)

print("Adjustments complete!")