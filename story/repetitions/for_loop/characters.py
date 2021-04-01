# Task for determinate the characters through loop

print("What strange markings do you see?")
text = input()

print("Indetifying...")
for count in range(0, len(text), 1):
    print("index ", count, ":", text[count])

print("Done.")