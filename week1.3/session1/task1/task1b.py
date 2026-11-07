# Week 1.3, Session 1: Task 1b

fruit = ['apple','pear','banana','orange']

# loop through the list
while fruit:
	print(fruit.pop())


# Why does this work?
# The while loop runs while the list is not empty.
# pop() removes the last item each time.
# When the list is empty, the loop stops.

# What features of Python does it rely on?
