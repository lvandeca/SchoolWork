'''
CIS 210: Concordance

Author Luke Vandecasteele

Credits: Class notes, textbook

This function determines the concordance
of words in a file and then
displays the results
'''

from documents import getLines

# List of English Punctuation Symbols
# Reference : Took maximum puntuations symbols possible from https://en.wikipedia.org/wiki/Punctuation_of_English
# NOTE: Apostrophe is excluded from the list as having it or not having it will give always distinct words.
punctuations = ["[", "]", "(", ")", "{", "}", "<", ">", \
         ":", ";", ",", "`", "'", "\"", "-", ".", \
         "|", "\\", "?", "/", "!", "-", "_", "@", \
         "\#", "$", "%", "^", "&", "*", "+", "~", "=" ]

def stripPunctuation(data):
    """ Strip Punctuations from the given string. """
    for punctuation in punctuations:
        data = data.replace(punctuation, " ")
    return data

def display(wordsDictionary):
    """ Display sorted dictionary of words and their frequencies. """
    noOfWords = 0
    print("-" * 42)
    print("| %20s | %15s |" % ("WORDS".center(20), "FREQUENCY".center(15)))
    print("-" * 42)
    for word in list(sorted(wordsDictionary.keys())):
        noOfWords += 1
        print("| %-20s | %15s |" % (word, str(wordsDictionary.get(word)).center(15)))
        # Halt every 20 words (configurable)
        if (noOfWords != 0 and noOfWords % 20 == 0):
            print("\n" * 2)
            input("PRESS ENTER TO CONTINUE ... ")
            print("\n" * 5)
            print("-" * 42)
            print("| %20s | %15s |" % ("WORDS".center(20), "FREQUENCY".center(15)))
            print("-" * 42)
    print("-" * 42)
    print("\n" * 2)

def prepareDictionary(words):
    """ Prepare dictionary of words and count their occurences. """
    wordsDictionary = {}
    for word in words:
        # Handle subsequent Occurences
        if (wordsDictionary.get(word.lower(), None) != None):
            # Search and add words by checking their lowercase version
            wordsDictionary[word.lower()] = wordsDictionary.get(word.lower()) + 1
        # Handle first Occurence
        else:
            wordsDictionary[word.lower()] = 1
    return wordsDictionary

def main():
    """ Main method """
    print("\n" * 10)
    print("Given a file name, program will find unique words and their occurences!", end="\n\n");
    input("Press ENTER to start execution ... \n");

    # To store all the words and their frequencies
    wordsDictionary = {}
    lines = ""
    # Get valid input file
    while (len(lines) == 0):
        fileName = input("Enter the file name (RELATIVE ONLY and NOT ABSOLUTE): ")
        print("\n\n" * 1)
        lines = getLines(fileName)
    # Get all words by removing all puntuations
    words = stripPunctuation(lines).split()
    # Prepare the words dictionary
    wordsDictionary = prepareDictionary(words)
    # Display words dictionary
    display(wordsDictionary)

"""
    Starting point
"""
main()
                            
        
