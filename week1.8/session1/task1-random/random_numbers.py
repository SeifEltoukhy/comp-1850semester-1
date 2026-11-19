import random

# Get user to input how many random numbers they want
amount = int(input("How many random numbers do you want? "))

# Generate this many random numbers
numbers = []

for i in range(amount):
    number = random.randint(1, 100)
    numbers.append(number)
# Write the random numbers to a file named random.txt, one number per line
with open("random.txt", "w") as file:
    for number in numbers:
        file.write(str(number) + "\n")