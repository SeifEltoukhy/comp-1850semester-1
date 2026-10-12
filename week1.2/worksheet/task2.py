# Worksheet 1.2: Task 2 Solution
import sys

from util import read_numbers
numbers = read_numbers()
if numbers ==[]:
    sys.exit("Error: no numbers provided")

else:
    numbers.sort()
    print ("Minimum =", min(numbers))
    print("Maximum =", max(numbers))
    print ("Mean =", (sum(numbers)) / (len(numbers)))
    mid=len(numbers)//2
if len(numbers) % 2 == 1:
    median = numbers[mid]
else:
    median = (numbers[mid - 1] + numbers[mid]) / 2
    print("Median =", median)
    



