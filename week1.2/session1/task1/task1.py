# Week 1.2, Session 1: Task 1

# Create a shopping list

shopping = ["eggs", "milk", "flour", "carrots"]
print(shopping)

# We forgot something, so add it to list

shopping.append("bananas")
print(shopping)

# We bought something, so remove it from list

shopping.remove("eggs")
print(shopping)

# Replace bananas with grapes
shopping.remove("bananas")
shopping.append("grapes")
print(shopping)

# a better way for repplacing insted of doing what i did up shopping[3]="grapes"

# Add yoghurt, just after milk
shopping.insert(1,"yoghurt")
print(shopping)


Grade=int(input("Enter Your Grade "))
if Grade ==39 or Grade <39 :
    print("you failed ")  
elif Grade >=40 and Grade<= 69:
    print("you have passed")  
