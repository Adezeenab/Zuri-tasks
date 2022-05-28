def find_anagram(word, anagram):
    if sorted(word) == sorted(anagram):
        return True
    else:
        return False

#Test if the findAnagram function works
if "__main__" == __name__:
    """
    Use a print function her so that the output will
    be displayed on the terminal since the return 
    keyword was used in the function
    """
word = input("Please input a word:")
anagram = input("Please enter another word:")
print(find_anagram(word, anagram))
