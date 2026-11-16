# Week 1.3, Session 2: Word Counter

# We want to read in a text file, and calculate how many words are in it. 
# You can use any of the .txt files to test this - or even make your own.

# open and read the file

# calculate the number of words
# hint: you could use .split() to break up by spaces
# hint: watch out for empty lines that might give you empty strings

# display the wordcount

# Here are the word counts you should get:
# story.txt - 290
# story2.txt - 326
# glasses.txt - 210
text="Hi my name is seif i want to play fifa , futchamps blad blad blad blahhh . cristiano ronaldo sewyyy . "
word=text.split()
word_count={}
for word in word:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1
print(word_count)


with open("week1.3/session2/task2/1_word_counter/story.txt", "r") as file:
    text = file.read()
words = text.split()
word_count = len(words)
print("Total number of words:", word_count)