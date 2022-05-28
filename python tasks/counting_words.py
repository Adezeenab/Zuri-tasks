# This script is to determine the number of words in a text
txt = input("Please enter a text:") # Receive user's input
print("You have entered:\n", txt) # Prints what the user what was entered.

# Getting word count in the text
txt_array = txt.split() # separates each word in the string into an array
word_count = len(txt_array) # gets the number of strings in the list
print("The number of words in the text is:", word_count)
