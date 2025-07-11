import unittest
from collections import Counter
import re
import os

def test_word_unique_count_in_string(file_path="", uniques=[], counts=[]):
    cwd = os.getcwd()
    file_path = cwd+"\simpletext.txt"
    fp = open(file_path, "w+") 
    
    word = """It was the best of times, it was the worst of times,
    it was the age of wisdom,
    it was the age of foolishness,
    it was the epoch of belief,
    it was the epoch of incredulity,
    it was the season of Light,
    it was the season of Darkness,
    it was the spring of hope,
    it was the winter of despair,
    we had everything before us,
    we had nothing before us,
    we were all going direct to Heaven,
    we were all going direct the other way--
    in short, the period was so far like the present period, that some of
    its noisiest authorities insisted on its being received, for good or for
    evil, in the superlative degree of comparison only."""

    fp.write(word)
    fp.close()

    words = open(file_path).read().lower().split()

    # Get the set of unique words.
    uniques = []
    for word in words:
        if word not in uniques:
            uniques.append(word)
    print(f'unique word in given file: {uniques}',end="\n")
    # Make a list of (count, unique) tuples.
    counts = []
    for unique in uniques:
        count = 0              # Initialize the count to zero.
        for word in words:     # Iterate over the words.
            if word == unique:   # Is this word equal to the current unique?
                count += 1         # If so, increment the count
        counts.append((count, unique))

    counts.sort()            # Sorting the list puts the lowest counts first.
    counts.reverse()         # Reverse it, putting the highest counts first.
    # Print the ten words with the highest counts.
    for i in range(min(10, len(counts))):
        count, word = counts[i]
        #print('%s %d' % (word, count))
    #print(f'Word count in given file: word: {word}, counts: {counts}',end="\n")
    
    
          

    with open(file_path, 'r') as file:
        text = file.read()
    words = re.findall(r'\b\w+\b', text) # Extract all words using regex
    print(f'word count for given string using re method: words: {words}, count: {len(words)}',end="\n")
    return words, len(words)

# Python Program to Count the Frequency using split and dict of Each Word in a String using Dictionary
def test_word_freq_dictmethod(user_str="", l=[], d ={}):
    # Count the frequency of words
    #user_str = input("Enter the string:")
    l = user_str.split()
    d = {}
    for key in l:
        if key not in d.keys():
            d[key] = 0
        d[key] = d[key]+1
    print(f'word count for given string: {key}, counts: {d[key]}',end="\n")

# Python Program to Count the Frequency using for loop method of Each Word in a String using Dictionary
def test_word_freq_forloop(user_str="", l=[], d ={}):
    # Count the frequency of words
    #user_str = input("Enter the string:")
    l = user_str.split()
    d = {}
    for key in l:
        d[key] = d.get(key,0)+1 # counter[word] = counter.get(word, 0) + 1.
    print(f'word count for given string using string split method and for loop: {key}, counts: {d[key]}',end="\n")

    # Define a function named word_count that takes one argument, 'str'.
def test_word_count(user_str):
    # Create an empty dictionary named 'counts' to store word frequencies.
    # dict method - using keys to check the word frequency is incremented or not
    # https://blog.finxter.com/how-to-count-the-number-of-words-in-a-string-in-python/
    counts = dict()
    
    # Split the input string 'str' into a list of words using spaces as separators and store it in the 'words' list.
    words = user_str.split()

    # Iterate through each word in the 'words' list.
    for word in words:
        # Check if the word is already in the 'counts' dictionary.
        if word in counts:
            # If the word is already in the dictionary, increment its frequency by 1.
            counts[word] += 1
        else:
            # If the word is not in the dictionary, add it to the dictionary with a frequency of 1.
            counts[word] = 1
    print(f'word count for given string using string split method and dict method: {word}, counts: {counts}',end="\n")
          
    # Return the 'counts' dictionary, which contains word frequencies.
    return counts

def test_word_count_using_re_method(user_str):
    # count the number of words in given string using re module and len() func
    print("find all the word in given string using re method", re.findall("\w+", user_str),end="\n")
    print("Length of word in given string using re ,method", len(re.findall("\w+", user_str)),end="\n")

def test_word_count_str_method(user_str, word=0):
    '''
    spaces = user_str.count(' ')
    tabs = user_str.count('\t')
    newlines = sentence.count('\n')
    word = 0
    word = spaces+tabs+newlines+1
    word = sum(1 for special_character in str if special_character in ' \t\s')
    print(word+1)

    You can count the number of words in string using one of the following options:
    Method 1: Using split() and len()
    Method 2: Using regex
    Method 3: Using a For Loop
    Method 4: Using count
    Method 5: Using sum

    '''
    # count the number of words in given string
    word = 0
    print(len(user_str.split())) # split method to count the words
    print("Length of word in given string", len(re.findall("\w+", user_str))) # regex method
    # for loop method to find the count of words
    for i in user_str:
        if i == " " or i == "\t" or i == "\n":
            word+=1
    if len(user_str) > 0:
        print("Number of words:", word)
    else:
        print("Number of words: 0")

    if user_str == " ":
        print(0)
    else:
        print(word+1)

    word = sum(1 for special_character in user_str if special_character in ' \t\s')
    print(f'word count for given string with tabs, new line, empty space using string split method and for loop: {word}',end="\n")

def test_word_cnt(text=""):
    text = "some words that are mostly different but are not all different not at all"
    words = text.split()
    resulting_count = Counter(words)
    print(f'word count for given string using string split method and Counter method: {words}, counts: {resulting_count}',end="\n")

# Python Program to Count the Frequency of Each Word in a String using Dictionary
def test_word_freq_split_method(user_str="", l=[], word_freq= []):
    '''
    Problem Solution
    1. Enter a string and store it in a variable.
    2. Declare a list variable and initialize it to an empty list.
    3. Split the string into words and store it in the list.
    4. Count the frequency of each word and store it in another list.
    5. Using the zip() function, merge the lists containing the words and the word counts into a dictionary.
    3. Print the final dictionary.
    4. Exit.

    Program Explanation
    1. User must enter a string and store it in a variable.
    2. A list variable is declared and initialized to an empty list.
    3. The string is split into words using a space as the reference and stored in the list.
    4. The frequency of each word in the list is counted using list comprehension and the count() function.
    5. The final dictionary is created using the zip() function and is printed.
    '''
    # Count the frequency of words
    #user_str = input("Enter the string:")
    l = user_str.split()
    word_freq = [l.count(i) for i in l]
    print(f'word count for given string using zip method: word: {l}, count: {dict(zip(l, word_freq))}', end="\n")

def test_word_counter_using_dictionary(user_str, d={}):
    user_str = input("Enter the string:")
    d = {}
    for element in user_str:
        if element in d:
            d[element] += 1
        else:
            d[element] = 1

    print(f'word count for given string using zip method: {d}',end="\n")
    return d
 

if __name__ == '__main__':
    test_word_unique_count_in_string(file_path="", uniques=[], counts=[])
    test_word_freq_dictmethod(user_str="It was the best of times, it was the worst of times", l=[], d ={})
    test_word_freq_forloop(user_str="It was the best of times, it was the worst of times", l=[], d ={})
    test_word_count_using_re_method(user_str="It was the best of times, it was the worst of times")
    test_word_count(user_str="It was the best of times, it was the worst of times")
    test_word_count_str_method(user_str="It was the best of times, it was the worst of times", word=0)
    test_word_cnt(text="")
    test_word_freq_split_method(user_str="It was the best of times, it was the worst of times", l=[], word_freq= [])
    test_word_counter_using_dictionary(user_str="It was the best of times, it was the worst of times", d={})
    unittest.main()

  