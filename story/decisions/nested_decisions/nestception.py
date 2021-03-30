# Task multiple nested decisions

print("Where should I look?")
loc = input()

#in the bedroom
if (loc == "in the bedroom"):
    print("Where in the bedroom should I look?")
    bedwhere = input()
    if (bedwhere == "under the bed"):
        print("Found some shoes but no battery")
    else:
        print("Found some mess but no battery!")
#in the bathroom
elif (loc == "in the bathroom"):
        print("Where in the bathroom should I look?")
        bathwhere = input()
        if (bathwhere == "in the bathtub"):
            print("Found a rubber duck, but no battery")
        else:
            print("Found a wet surface but no battery")
#in the lab
elif (loc == "in the lab"):
        print("Where in the lab should I look?")
        labwhere = input()
        if (labwhere == "on the table"):
            print("Yes! Found my battery!")
        else:
            print("Found some tools, but no battery")
else:
    print("I don't know where that is, but I'll keep looking!")