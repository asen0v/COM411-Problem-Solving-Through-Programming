# Task for len() function

print("Please enter a phrase:")
phrase = input()

bops = 0

while (bops < len(phrase)):
    print("Bop ", end="")
    bops=bops+1

### Working variant but without While Loop
### print("Please enter a phrase:")
### phrase = str(input())
### kolko = len(phrase)
### word = "Bop "
### print(word * kolko)