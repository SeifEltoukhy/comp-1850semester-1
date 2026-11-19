import random

# Read names from a file

with open("names.txt") as infile:
    names = [ line.strip() for line in infile ]

# Ask user to enter a number, then randomly choose that many names
# from the list, avoiding any duplicate choices
amount = int(input("How many names do you want to pick? "))

names = list(dict.fromkeys(names))

if amount > len(names):
    print("Not enough names in the file!")
else:
    chosen_names = random.sample(names, amount)

# Display the chosen names, one per line
for name in chosen_names:
        print(name)