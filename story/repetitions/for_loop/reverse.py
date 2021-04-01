# Task for revealing reverse words

print("What phrase do you see?")
text = input()

print("Reversing...")
print("Your phrase is: ", end="")
for count in range(len(text) - 1, -1, -1):
    print(text[count], end="")