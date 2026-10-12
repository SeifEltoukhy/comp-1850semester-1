# Worksheet 1.2: Task 1 Solution
import sys
try:
    grade1 =int(input("Enter your grade "))
except:
    sys.exit("Error: Grade must be an integer between 0 and 100")
if grade1 >= 0 and grade1 <= 39 :
    print(grade1,("is a Fail"))
elif grade1 >= 40 and grade1 <= 69 :
    print(grade1,("is a Pass"))
elif grade1 >= 70 and grade1 <= 100 :
     print(grade1,("is a Distinction"))
else:
    sys.exit("Error: Grade must be an integer between 0 and 100")
