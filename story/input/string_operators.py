# Task for string operations

print("Please enter the number of lives.")
lives = int(input())
print("Please enter the energy level.")
energy = int(input())
print("Please enter the shield level.")
shield = int(input())
print("Health has been set.")
livsym = "♥"
othsym = "♦"
print("Lives: ", livsym*lives)
print("Energy: ", othsym*energy)
print("Shield: ", othsym*shield)