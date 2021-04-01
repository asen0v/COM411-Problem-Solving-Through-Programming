# Task about for loop for countdown
print("How far are we from the cave?")
kolko = int(input())

print()

for count in range(kolko, 0, -1):
    print(count, "steps remaining.")
print("We have reached the cave!")



# The code is working as well, but not that long
#print("How far are we from the cave?")
#kolko = int(input())
#ostavat = 0
#for steps in range(kolko):
#    steps = steps + 1
#    ostavat = kolko+1 - steps
#    print(ostavat, "steps remaining")

#print("We have reached the cave!")