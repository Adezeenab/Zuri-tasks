''' This task is about reading text files in python
as well as count the occurence of words in that text
Example:
count_words("The cake is done. It is a big cake!") 
{"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}
'''

def read_file_content(filename):
    with open(filename, mode="r") as myfile:
        content = myfile.read()
        return content

#Solution 1 for count words
def count_words():
    text = read_file_content("./story.txt")
    mydict = {}
    textList = text.split()
    
    for i in textList:
        if i in mydict.keys():
            mydict[i] += 1
        else:
            mydict[i] = 1

    print(mydict)         
    

read_file_content('story.txt')
count_words()


#################################################
#    2) Import a module in Python               #
#################################################

from collections import Counter

words = read_file_content('story.txt').split()
print(Counter(words))
