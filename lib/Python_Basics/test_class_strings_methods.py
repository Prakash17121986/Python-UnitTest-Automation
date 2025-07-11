import unittest

def test_string_isdigit(string_value):
    '''
    The isdigit() method returns True if all the characters are digits, otherwise False.
    '''
    #string_value = "12345"
    #print(f'__doc__: {test_string_isdigit.__doc__}')
    print(f"string_value: {string_value}")
    print(f"isdigit method: {string_value.isdigit()}\n")
    return string_value.isdigit()

def test_string_expandtabs(string_value, tab_size):
    '''
    The expandtabs() method sets the tab size to the specified number of whitespaces.
    '''
    #string_value = "H\te\tl\tl\to"
    #tab_size = 4
    #print(f'__doc__: {test_string_expandtabs.__doc__}')
    string_output = string_value.expandtabs(tab_size)
    print(f"string_value: {string_value}")
    print(f"expandtabs method: {string_output}\n")

def test_string_find(string_value, start, end):
    '''
    The find() method finds the first occurrence of the specified value.
    The find() method returns -1 if the value is not found.
    The find() method is almost the same as the index() method, the only difference is that the index() method raises an exception if the value is not found. 
    '''
    #string_value = "Hello, welcome to my world."
    #start=5
    #end=10
    #print(f'__doc__: {test_string_find.__doc__}')
    string_output = string_value.find("welcome")
    string_output2 = string_value.find("e")
    string_output3 = string_value.find("e", start, end)
    print(f"string_value: {string_value}")
    print(f"find method: {string_output}")
    print(f"string_value: {string_value}")
    print(f"find method: {string_output2}")
    print(f"string_value: {string_value}")
    print(f"find method: {string_output2}\n")
    return string_output

def test_string_format(string_value):
    '''
    The format() method formats the specified value(s) and insert them inside the string's placeholder.
    The placeholder is defined using curly brackets: {}
    The format() method returns the formatted string.
    #"My name is {fname}, I'm {age}".format(fname = "John", age = 36)
    #"My name is {0}, I'm {1}".format("John",36)
    #"My name is {}, I'm {}".format("John",36)
    # F-strings are faster than traditional string formatting methods. F strings are superior in readability and performance
    '''
    #string_value = "For only {price:.2f} dollars!"
    #print(f'__doc__: {test_string_format.__doc__}')
    string_output1 = "My name is {fname}, I'm {age}".format(fname = "John", age = 36)
    string_output2 = "My name is {0}, I'm {1}".format("John",36)
    string_output3 = "My name is {}, I'm {}".format("John",36)
    
    print("string_value: ", "For only {price:.2f} dollars!".format(price = 49))
    print(f"format method using value for key: {string_output1}")
    print(f"string_value: {string_value}")
    print(f"format method using value for index: {string_output2}")
    print(f"string_value: {string_value}")
    print(f"format method using value for empty value: {string_output3}\n")

def test_string_index(string_value):
    '''
    The index() method finds the first occurrence of the specified value.
    The index() method raises an exception if the value is not found.
    The index() method is almost the same as the find() method, the only difference is that the find() method returns -1 if the value is not found.
    If the value is not found, the find() method returns -1, but the index() method will raise an exception:
    txt = "Hello, welcome to my world."
    print(txt.find("q"))
    print(txt.index("q"))
    '''
    #string_value = "Hello, welcome to my world."
    #print(f'__doc__: {test_string_index.__doc__}')
    string_output1 = string_value.index("e")
    string_output2 = string_value.index("e", 5, 10)

    print(f"string_value: {string_value}")
    print(f"index method: {string_output1}, {string_output2}\n")
    return string_output1, string_output2

def test_string_islower(string_value):
    '''
    The islower() method returns True if all the characters are in lower case, otherwise False.
    Numbers, symbols and spaces are not checked, only alphabet characters.
    '''
    #string_value = "hello world!"
    #print(f'__doc__: {test_string_islower.__doc__}')
    string_output = string_value.islower()
    print(f"string_value: {string_value}")
    print(f"islower method: {string_output}\n")
    return string_output

def test_string_isupper(string_value):
    '''
    The isupper() method returns True if all the characters are in upper case, otherwise False.
    Numbers, symbols and spaces are not checked, only alphabet characters.
    '''
    #string_value = "THIS IS NOW!"
    print(f'__doc__: {test_string_isupper.__doc__}')
    string_output = string_value.isupper()
    print(f"string_value: {string_value}")
    print(f"isupper method: {string_output}")
    return string_output

def test_string_swapcase(string_value):
    '''
    The swapcase() method returns a string where all the upper case letters are lower case and vice versa.
    '''
    #string_value = "Hello My Name Is PETER"
    #print(f'__doc__: {test_string_swapcase.__doc__}')
    string_output = string_value.swapcase()
    print(f"string_value: {string_value}")
    print(f"swapcase method: {string_output}")
    return string_output

def test_string_join(string_value="", string_value1={}):
    '''
    The join() method takes all items in an iterable and joins them into one string.
    '''
    #string_value = ("John", "Peter", "Vicky")
    #print(f'__doc__: {test_string_join.__doc__}')
    string_output1 = "#".join(string_value)
    #string_value1 = {"name": "John", "country": "Norway"}
    mySeparator = "TEST"
    string_output2 = mySeparator.join(string_value1)
    print(f"string_value: {string_value}")
    print(f"mySeparator: {mySeparator}")
    print(f"join method: {string_output1}\n")
    print(f"string_value: {string_value1}")
    print(f"join method: {string_output2}\n")
    return string_output1, string_output2

def test_string_split(string_value):
    '''
    Split a string into a list where each word is a list item:
    Splits the string at the specified separator, and returns a list
    The split() method splits a string into a list.
    string.split(separator, maxsplit)
    You can specify the separator, default separator is any whitespace.
    #setting the maxsplit parameter to 1, will return a list with 2 elements!
    '''
    #string_value = "hello, my name is Peter, I am 26 years old"
    #print(f'__doc__: {test_string_split.__doc__}')
    string_output1 = string_value.split(", ")
    
    string_output2 = string_value.split("#", 1)
    print(f"string_value: {string_value}")
    print(f"split method ',': {string_output1}")
    print(f"string_value: {string_value}")
    print(f"split method '#': {string_output2}")
    return string_output1, string_output2



def test_string_splitlines(string_value):
    '''
    The splitlines() method splits a string into a list. The splitting is done at line breaks.
    Splits the string at line breaks and returns a list
    '''
    #string_value = "Thank you for the music\nWelcome to the jungle"
    #print(f'__doc__: {test_string_isdigit.__doc__}')
    string_output1 = string_value.splitlines()
    string_output2 = string_value.splitlines(True)
    print(f"string_value: {string_value}")
    print(f"splitlines method: {string_output1}\n")

    print(f"string_value: {string_value}")
    print(f"splitlines method: {string_output2}\n")
    return string_output1, string_output2

def test_string_startswith(string_value):
    '''
    Returns true if the string starts with the specified value
    '''
    #string_value = "Hello, welcome to my world."
    #print(f'__doc__: {test_string_startswith.__doc__}')
    string_output1 = string_value.startswith('Hello')
    string_output2 = string_value.startswith("wel", 7, 20)
    print(f"string_value: {string_value}")
    print(f"startswith method: {string_output1}\n")

    print(f"string_value: {string_value}")
    print(f"startswith method: {string_output2}")
    return string_output1, string_output2

def test_string_endswith(string_value):
    '''
    The endswith() method returns True if the string ends with the specified value, otherwise False.
    '''
    #string_value = "Hello, welcome to my world."
    #print(f'__doc__: {test_string_endswith.__doc__}')
    string_output = string_value.endswith(".")
    print(f"string_value: {string_value}")
    print(f"endswith method: {string_output}\n")
    return string_output

def test_string_strip(string_value):
    '''
    The strip() method removes any leading, and trailing whitespaces.
    '''
    #string_value = ",,,,,rrttgg.....banana....rrr"
    print(f'__doc__: {test_string_swapcase.__doc__}')
    string_output = string_value.strip(",.grt")
    print(f"string_value: {string_value}")
    print(f"strip method: {string_output}\n")
    return string_output

def test_string_partition(string_value):
    '''
    The partition() method searches for a specified string, and splits the string into a tuple containing three elements.
    The first element contains the part before the specified string.
    The second element contains the specified string.

    The third element contains the part after the string.
    Search for the word "bananas", and return a tuple with three elements:

    1 - everything before the "match"
    2 - the "match"
    3 - everything after the "match"
    '''
    #string_value = "I could eat bananas all day"
    #print(f'__doc__: {test_string_swapcase.__doc__}')
    string_output = string_value.partition("bananas")
    print(f'string_value: {string_value}')
    print(f'partition method: {string_output}\n')
    return string_output


def test_string_capitalize(string_value):
    '''
    #Upper case the first letter in this sentence:
    #The capitalize() method returns a string where the first character is upper case, and the rest is lower case.
    #The first character is converted to upper case, and the rest are converted to lower case
    '''
    #print(f'__doc__: {test_string_capitalize.__doc__}')

    #string_value = "hello, and welcome to my world."
    string_output = string_value.capitalize()
    print(f'string_value: {string_value}')
    print(f'capitalize method: {string_output}\n')
    return string_output

def test_string_casefold(string_value):
    '''
    #The casefold() method returns a string where all the characters are lower case.
    #This method is similar to the lower() method, but the casefold() method is stronger, more aggressive,
    # meaning that it will convert more characters into lower case, and will find more matches
    # when comparing two strings and both are converted using the casefold() method
    '''
    #print(f'__doc__: {test_string_casefold.__doc__}')
    #string_value  = "Hello, And Welcome To My World!"
    string_ouput = string_value.casefold()
    print(f'string_value: {string_value}')
    print(f'string_value using casefold method: {string_ouput}\n')
    return string_ouput

def test_string_replace(string_value):
    '''
    Given string will repalce with another string using str.replace()
    '''
    #print(f'__doc__: {test_string_replace.__doc__}')
    #string_value = "Hello, And Welcome To My World!"
    string_output = string_value.replace('And', "All")
    print(f'string_value: {string_value}')
    print(f'string_value using replace method: {string_output}\n')
    return string_output



def test_string_slicing(string_value):
    """
    #Python - Slicing Strings
    #You can return a range of characters by using the slice syntax.
    #Specify the start index and the end index, separated by a colon, to return a part of the string.
    #Get the characters from position 2 to position 5 (not included)
    """
    #print(f'__doc__: {test_string_slicing.__doc__}')
    #string_value = "Hello, World!"
    print(f'string_value: {string_value}')
    string_output1 = string_value[0:5]
    string_output2 = string_value[-4:-1]
    print(f'string_output1: string_value[0:5]: {string_output1}')
    print(f'string_output2: string_value[-4:-1]:v{string_output1}')
    print(f'positive slicing method')
    print(f'string_value[2:5]: {string_value[2:5]}') # Positive indexing
    print(f'string_value[:5]: {string_value[:5]}') # Positive indexing
    print(f'string_value[:2]: {string_value[:2]}\n') # Positive indexing

    print(f'negative slicing method')
    print(f'string_value[-5:-2],{string_value[-5:-2]}\n') # Negative indexing
    return string_output1,string_output2

def test_string_encode_function(string_value):
    '''
    #UTF-8 encode the string:
    #The encode() method encodes the string, using the specified encoding. If no encoding is specified, UTF-8 will be used.
    '''
    #print(f'__doc__: {test_string_encode_function.__doc__}')
    #These examples uses ascii encoding, and a character that cannot be encoded, showing the result with different errors:
    string_value = "My name is Ståle"
    string_output = string_value.encode()
    print(f'string_value: {string_value}')
    print(f'string_value using encode method: {string_output}')

    print(f'string_value: {string_value}')
    print(f'string_value using enocde backslashreplace method: {string_value.encode(encoding="ascii",errors="backslashreplace")}\n')
    
    print(f'string_value: {string_value}')
    print(f'string_value using encode ascii method: {string_value.encode(encoding="ascii",errors="ignore")}\n')
    
    print(f'string_value: {string_value}')
    print(f'string_value using encode namereplace method: {string_value.encode(encoding="ascii",errors="namereplace")}\n')
    
    print(f'string_value: {string_value}')
    print(f'string_value using encode replace method: {string_value.encode(encoding="ascii",errors="replace")}\n')
    
    print(f'string_value: {string_value}')
    print(f'string_value using encode xmlcharrefreplace method: {string_value.encode(encoding="ascii",errors="xmlcharrefreplace")}\n')

    return string_output


def test_string_count(string_value):
    '''
    #The count() method returns the number of times a specified value appears in the string.
    #string.count(value, start, end)
    #Search from position 10 to 24:
    Return the number of times the value "apple" appears in the string:
    '''
    #print(f'__doc__: {test_string_count.__doc__}')
    #string_value = "I love apples, apple are my favorite fruit"
    string_count = string_value.count("apple")
    print(f'string_value: {string_value}')
    print(f"center method: {string_count}\n")

    string_value = "I love apples, apple are my favorite fruit"
    string_output = string_value.count("apple", 10, 24)
    print(f"string_value: {string_value}")
    print(f"count method: {string_output}\n")

    return string_count, string_output

def test_string_center(string_value):
    '''
    #The center() method will center align the string, using a specified character (space is default) as the fill character.
    #string.center(length, character)
    #length	Required. The length of the returned string
    #character	Optional. The character to fill the missing space on each side. Default is " " (space)
    '''
    #print(f'__doc__: {test_string_center.__doc__}')
    #string_value = "banana"
    string_output = string_value.center(20)
    print(f"string_value: {string_value}\n")
    print(f"center method: {string_output}\n")

    #Using the letter "O" as the padding character:
    string_value1 = "banana"
    string_output1 = string_value1.center(20, "O")
    print(f"string_value1: {string_value1}")
    print(f"Cenetr Method: {string_output1}\n")

    return string_output, string_output1

def test_string_isidentifier(string_value):
    '''
    The isidentifier() method returns True if the string is a valid identifier, otherwise False.
    A string is considered a valid identifier if it only contains alphanumeric letters (a-z) and (0-9), or underscores (_). A valid identifier cannot start with a number, or contain any spaces.
    '''
    #string_value = "I love apples, apple are my favorite fruit"
    #print(f'__doc__: {test_string_isidentifier.__doc__}')
    string_output = string_value.isidentifier()
    print(f"string_value: {string_value}")
    print(f"isidentifier method: {string_output}\n")
    return string_output

def test_string_maketrans_translate(string_value):
    '''
    Create a mapping table, and use it in the translate() method to replace any "S" characters with a "P" character:
    The maketrans() method returns a mapping table that can be used with the translate() method to replace specified characters.
    Use the maketrans() method to create a mapping table.
    '''
    #string_value = "Hello Sam!"
    #print(f'__doc__: {test_string_maketrans_translate.__doc__}')
    mytable= string_value.maketrans("S", "P") #  ascii codes to replace 83 (S) with 80 (P)
    print(f"string_value: {string_value}, string_value using maketrans method: {mytable}")
    string_output = string_value.translate(mytable)
    print(f"string_value: {string_value}")
    print(f"translate method: {string_output}\n")
    return string_output

def test_string_title(string_value):
    '''
    Make the first letter in each word upper case
    The title() method returns a string where the first character in every word is upper case. Like a header, or a title.
    If the word contains a number or a symbol, the first letter after that will be converted to upper case.
    txt = "hello b2b2b2 and 3g3g3g"
    x = txt.title()
    print(x)
    Hello B2B2B2 And 3G3G3G
    '''
    #string_value = "Welcome to my 2nd world"
    #print(f'__doc__: {test_string_title.__doc__}')
    string_output = string_value.title()
    print(f"string_value: {string_value}")
    print(f"title method: {string_output}\n")
    return string_output

def test_string_zfill(string_value):
    '''
    Fill the string with zeros until it is 10 characters long:
    The zfill() method adds zeros (0) at the beginning of the string, until it reaches the specified length.
    If the value of the len parameter is less than the length of the string, no filling is done.
    '''
    #string_value = "12345"
    #print(f'__doc__: {test_string_zfill.__doc__}')
    string_output = string_value.zfill(10)
    print(f"string_value: {string_value}")
    print(f"zfill method: {string_output}\n")
    return string_output

def test_string_alpha(string_value):
    '''
    The isalnum() method returns True if all the characters are alphanumeric, meaning alphabet letter (a-z) and numbers (0-9).
    Example of characters that are not alphanumeric: (space)!#%&? etc.
    '''
    #string_value = "Company12"
    #print(f'__doc__: {test_string_alpha.__doc__}')
    string_output = string_value.isalnum()
    print(f"string_value: {string_value}")
    print(f"alpha method: {string_output}\n")
    return string_output

def test_string_isalpha(string_value):
    '''
    The isalpha() method returns True if all the characters are alphabet letters (a-z).
    Example of characters that are not alphabet letters: (space)!#%&? etc.
    '''
    #string_value = "CompanyX"
    #print(f'__doc__: {test_string_isalpha.__doc__}')
    string_output = string_value.isalpha()
    print(f"string_value: {string_value}")
    print(f"isalpha method: {string_output}\n")
    return string_output

def test_string_isascii(string_value):
    '''
    The isascii() method returns True if all the characters are ascii characters  (a-z).
    '''
    #string_value = "Company123"
    #print(f'__doc__: {test_string_isascii.__doc__}')
    string_output = string_value.isascii()
    print(f"string_value: {string_value}")
    print(f"isascii method: {string_output}\n")
    return string_output

def test_string_isdecimal(string_value):
    '''
    The isdecimal() method returns True if all the characters are decimals (0-9).
    This method can also be used on unicode objects
    '''
    #string_value = "123"
    #print(f'__doc__: {test_string_isdecimal.__doc__}')
    string_output = string_value.isdecimal()
    print(f"string_value: {string_value}")
    print(f"isdecimal method: {string_output}\n")
    return string_output

def test_string_isnumeric(string_value):
    '''
    The isnumeric() method returns True if all the characters are numeric (0-9), otherwise False.
    Exponents, like ² and ¾ are also considered to be numeric values.
    "-1" and "1.5" are NOT considered numeric values, because all the characters in the string must be numeric, and the - and the . are not.
    '''
    #string_value = "565543"
    #print(f'__doc__: {test_string_isnumeric.__doc__}')
    string_output = string_value.isnumeric()
    print(f"string_value: {string_value}")
    print(f"isnumeric method: {string_output}\n")
    return string_output

def test_string_isprintable(string_value):
    '''
    The isprintable() method returns True if all the characters are printable, otherwise False.
    Example of none printable character can be carriage return and line feed.
    '''
 
    #string_value = "Hello!\nAre you #1?"
    #print(f'__doc__: {test_string_isprintable.__doc__}')
    string_output = string_value.isprintable()
    print(f"string_value: {string_value}")
    print(f"isprintable method: {string_output}\n")
    return string_output

def test_string_isspace(string_value):
    '''
    The isspace() method returns True if all the characters in a string are whitespaces, otherwise False.
    '''
    #string_value = "  "
    #print(f'__doc__: {test_string_isspace.__doc__}')
    string_output = string_value.isspace()
    print(f"string_value: {string_value}")
    print(f"isspace method: {string_output}\n")
    return string_output

def test_string_istitle(string_value):
    '''
    The istitle() method returns True if all words in a text start with a upper case letter, AND the rest of the word are lower case letters, otherwise False.
    Symbols and numbers are ignored.
    '''
    #string_value = "Hello, And Welcome To My World!"
    #print(f'__doc__: {test_string_istitle.__doc__}')
    string_output = string_value.istitle()
    print(f"string_value: {string_value}")
    print(f"istitle method: {string_output}\n")
    return string_output
    

def test_string_ljust(string_value,length):
    '''
    The ljust() method will left align the string, using a specified character (space is default) as the fill character.
    string.ljust(length, character)
    length -	Required. The length of the returned string
    character - Optional. A character to fill the missing space (to the left of the string). Default is " " (space).
    '''
    #txt = "banana"
    #x = txt.ljust(20)

    #string_value = "Hello, And Welcome To My World!"
    #print(f'__doc__: {test_string_ljust.__doc__}')
    string_output = string_value.ljust(length)
    print(f"string_value: {string_value}")
    print(f"ljust method: {string_output}\n")
    return string_output

def test_string_rjust(string_value,length):
    '''
    The rjust() method will right align the string, using a specified character (space is default) as the fill character.
    string.rjust(length, character)
    '''
    #txt = "banana"
    #x = txt.ljust(20)

    #string_value = "Hello, And Welcome To My World!"
    #print(f'__doc__: {test_string_rjust.__doc__}')
    string_output = string_value.rjust(length)
    print(f"string_value: {string_value}")
    print(f"rjust method: {string_output}\n")
    return string_output

def test_string_lstrip(string_value):

    '''
    The lstrip() method removes any leading characters (space is the default leading character to remove)
    '''
    # txt = "     banana     "
    # x = txt.lstrip()
    # print("of all fruits", x, "is my favorite")
    # txt = ",,,,,ssaaww.....banana"
    # x = txt.lstrip(",.asw")
    # print(x)

    #string_value = "Hello, And Welcome To My World!"
    #print(f'__doc__: {test_string_isalpha.__doc__}')
    string_output = string_value.lstrip()
    print(f"string_value: {string_value}")
    print(f"lstrip method: {string_output}\n")
    return string_output

def test_string_rfind(string_value, value):

    '''
    The rfind() method finds the last occurrence of the specified value.
    The rfind() method returns -1 if the value is not found.
    The rfind() method is almost the same as the rindex() method. See example below.
    string.rfind(value, start, end)
    value - Required. The value to search for
    start - Optional. Where to start the search. Default is 0
    end - Optional. Where to end the search. Default is to the end of the string
    '''
    # txt = "Mi casa, su casa."
    # x = txt.rfind("casa")
    # print(x)

    # txt = "Hello, welcome to my world."
    # x = txt.rfind("e")
    # print(x)

    # txt = "Hello, welcome to my world."
    # x = txt.rfind("e", 5, 10)
    # print(x)

    # txt = "Hello, welcome to my world."
    #If the value is not found, the rfind() method returns -1, but the rindex() method will raise an exception:
    # print(txt.rfind("q"))
    # print(txt.rindex("q"))
    

    #string_value = "Hello, And Welcome To My World!"
    #print(f'__doc__: {test_string_isalpha.__doc__}')
    string_output = string_value.rfind(value)
    print(f"string_value: {string_value}")
    print(f"rfind method: {string_output}\n")
    return string_output


def test_string_rindex(string_value,value):
    '''
    The rindex() method finds the last occurrence of the specified value.
    The rindex() method raises an exception if the value is not found.
    The rindex() method is almost the same as the rfind() method.
    string.rindex(value, start, end)
    value - Required. The value to search for
    start - Optional. Where to start the search. Default is 0
    end - Optional. Where to end the search. Default is to the end of the string
    '''
    # txt = "Hello, welcome to my world."
    # x = txt.rindex("e")
    # print(x)

    # txt = "Hello, welcome to my world."
    # x = txt.rindex("e", 5, 10)
    # print(x)
    
    #string_value = "Hello, And Welcome To My World!"
    #print(f'__doc__: {test_string_rindex.__doc__}')
    string_output = string_value.rindex(value)
    print(f"string_value: {string_value}")
    print(f"rindex method: {string_output}\n")
    return string_output


def test_string_rpartition(string_value, value):
    '''
    The rpartition() method searches for the last occurrence of a specified string, and splits the string into a tuple containing three elements.
    The first element contains the part before the specified string.
    The second element contains the specified string.
    The third element contains the part after the string.
    string.rpartition(value)
    value - Required. The string to search for
    '''
    # txt = "I could eat bananas all day, bananas are my favorite fruit"
    # x = txt.rpartition("apples")
    # print(x)
    
    #string_value = "Hello, And Welcome To My World!"
    #print(f'__doc__: {test_string_rpartition.__doc__}')
    string_output = string_value.rpartition(value)
    print(f"string_value: {string_value}")
    print(f"rpartition method: {string_output}\n")
    return string_output

def test_string_rsplit(string_value, value):
    '''
    The rsplit() method splits a string into a list, starting from the right.
    If no "max" is specified, this method will return the same as the split() method.
    seperator - Optional. Specifies the separator to use when splitting the string. By default any whitespace is a separator
    maxaplit - Optional. Specifies how many splits to do. Default value is -1, which is "all occurrences"
    '''

    #txt = "apple, banana, cherry"
    #Split the string into a list with maximum 2 items
    # setting the maxsplit parameter to 1, will return a list with 2 elements!
    # x = txt.rsplit(", ", 1)
    # print(x)

    #string_value = "Hello, And Welcome To My World!"
    #print(f'__doc__: {test_string_rsplit.__doc__}')
    string_output = string_value.rsplit(value)
    print(f"string_value: {string_value}")
    print(f"rsplit method: {string_output}\n")
    return string_output
    

def test_string_rstrip(string_value):
    '''
    The rstrip() method removes any trailing characters (characters at the end a string), space is the default trailing character to remove.
    string.rstrip(characters)
    characters - 	Optional. A set of characters to remove as trailing characters
    '''
    # Remove the trailing characters if they are commas, periods, s, q, or w:
    # txt = "banana,,,,,ssqqqww....."
    # x = txt.rstrip(",.qsw")
    # print(x)

    #string_value = "Hello, And Welcome To My World!"
    #print(f'__doc__: {test_string_rstrip.__doc__}')
    string_output = string_value.rstrip(',')
    print(f"string_value: {string_value}")
    print(f"rstrip method: {string_output}\n")
    return string_output

   
if __name__ == '__main__':
    
    test_string_isdigit("12345")
    test_string_expandtabs("H\te\tl\tl\to", 4)
    test_string_find("Hello, welcome to my world.", 5, 10)
    test_string_format("For only {price:.2f} dollars!")
    test_string_index("Hello, welcome to my world.")
    test_string_islower("hello world!")
    test_string_isupper("hello world!")
    test_string_swapcase("Hello My Name Is PETER")
    test_string_join(("John", "Peter", "Vicky"), {"name": "John", "country": "Norway"})
    test_string_split("hello, my name is Peter, I am 26 years old")
    test_string_splitlines("Thank you for the music\nWelcome to the jungle")
    test_string_startswith("Hello, welcome to my world.")
    test_string_endswith("Hello, welcome to my world.")
    test_string_strip(",,,,,rrttgg.....banana....rrr")
    test_string_partition("I could eat bananas all day")
    test_string_capitalize("hello, and welcome to my world.")
    test_string_casefold("Hello, And Welcome To My World!")
    test_string_replace("Hello, And Welcome To My World!")
    test_string_slicing("Hello, World!")
    test_string_encode_function("My name is Ståle")
    test_string_count("I love apples, apple are my favorite fruit")
    test_string_center("banana")
    test_string_isidentifier("I love apples, apple are my favorite fruit")
    test_string_maketrans_translate("Hello Sam!")
    test_string_title("Welcome to my 2nd world")
    test_string_zfill("12345")
    test_string_alpha("Company12")
    test_string_isalpha("CompanyX")
    test_string_isascii("Company123")
    test_string_isdecimal("123")
    test_string_isnumeric("565543")
    test_string_isprintable("Hello!\nAre you #1?")
    test_string_isspace("  ")
    test_string_istitle("Hello, And Welcome To My World!")
    test_string_ljust("Hello, And Welcome To My World!",20)
    test_string_rjust("Hello, And Welcome To My World!",20)
    test_string_lstrip("Hello, And Welcome To My World!")
    test_string_rfind("Hello, And Welcome To My World!", 'Welcome')
    test_string_rindex("Hello, And Welcome To My World!", 'Welcome')
    test_string_rpartition("Hello, And Welcome To My World!",'Welcome')
    test_string_rsplit("Hello, And Welcome To My World!",'Welcome')
    test_string_rstrip("Hello, And Welcome To My World!")
    unittest.main()

# -------------------------Program Output----------------------------------------


# PS C:\Users\Anamika\Python_codes\myenv\tests\Python_Basics> python .\test_class_strings_methods.py
# __doc__: 
#     The isdigit() method returns True if all the characters are digits, otherwise False.
    
# string_value: 12345
# isdigit method: True

# __doc__:
#     The expandtabs() method sets the tab size to the specified number of whitespaces.

# string_value: H e       l       l       o
# expandtabs method: H   e   l   l   o

# __doc__:
#     The find() method finds the first occurrence of the specified value.
#     The find() method returns -1 if the value is not found.
#     The find() method is almost the same as the index() method, the only difference is that the index() method raises an exception if the value is not found.

# string_value: Hello, welcome to my world.
# find method: 7
# string_value: Hello, welcome to my world.
# find method: 1
# string_value: Hello, welcome to my world.
# find method: 1

# __doc__:
#     The format() method formats the specified value(s) and insert them inside the string's placeholder.
#     The placeholder is defined using curly brackets: {}
#     The format() method returns the formatted string.
#     #"My name is {fname}, I'm {age}".format(fname = "John", age = 36)
#     #"My name is {0}, I'm {1}".format("John",36)
#     #"My name is {}, I'm {}".format("John",36)
#     # F-strings are faster than traditional string formatting methods. F strings are superior in readability and performance

# string_value:  For only 49.00 dollars!
# format method using value for key: My name is John, I'm 36
# string_value: For only {price:.2f} dollars!
# format method using value for index: My name is John, I'm 36
# string_value: For only {price:.2f} dollars!
# format method using value for empty value: My name is John, I'm 36

# __doc__:
#     The index() method finds the first occurrence of the specified value.
#     The index() method raises an exception if the value is not found.
#     The index() method is almost the same as the find() method, the only difference is that the find() method returns -1 if the value is not found.
#     If the value is not found, the find() method returns -1, but the index() method will raise an exception:
#     txt = "Hello, welcome to my world."
#     print(txt.find("q"))
#     print(txt.index("q"))

# string_value: Hello, welcome to my world.
# index method: 1, 8

# __doc__:
#     The islower() method returns True if all the characters are in lower case, otherwise False.
#     Numbers, symbols and spaces are not checked, only alphabet characters.

# string_value: hello world!
# islower method: True

# __doc__:
#     The isupper() method returns True if all the characters are in upper case, otherwise False.
#     Numbers, symbols and spaces are not checked, only alphabet characters.

# string_value: hello world!
# isupper method: False
# __doc__:
#     The swapcase() method returns a string where all the upper case letters are lower case and vice versa.

# string_value: Hello My Name Is PETER
# swapcase method: hELLO mY nAME iS peter
# __doc__:
#     The join() method takes all items in an iterable and joins them into one string.

# string_value: ('John', 'Peter', 'Vicky')
# mySeparator: TEST
# join method: John#Peter#Vicky

# string_value: {'name': 'John', 'country': 'Norway'}
# join method: nameTESTcountry

# __doc__:
#     Split a string into a list where each word is a list item:
#     Splits the string at the specified separator, and returns a list
#     The split() method splits a string into a list.
#     string.split(separator, maxsplit)
#     You can specify the separator, default separator is any whitespace.
#     #setting the maxsplit parameter to 1, will return a list with 2 elements!

# string_value: hello, my name is Peter, I am 26 years old
# split method ',': ['hello', 'my name is Peter', 'I am 26 years old']
# string_value: hello, my name is Peter, I am 26 years old
# split method '#': ['hello, my name is Peter, I am 26 years old']
# __doc__:
#     The isdigit() method returns True if all the characters are digits, otherwise False.

# string_value: Thank you for the music
# Welcome to the jungle
# splitlines method: ['Thank you for the music', 'Welcome to the jungle']

# string_value: Thank you for the music
# Welcome to the jungle
# splitlines method: ['Thank you for the music\n', 'Welcome to the jungle']

# __doc__:
#     Returns true if the string starts with the specified value

# string_value: Hello, welcome to my world.
# startswith method: True

# string_value: Hello, welcome to my world.
# startswith method: True
# __doc__:
#     The endswith() method returns True if the string ends with the specified value, otherwise False.

# string_value: Hello, welcome to my world.
# endswith method: True

# __doc__:
#     The swapcase() method returns a string where all the upper case letters are lower case and vice versa.

# string_value: ,,,,,rrttgg.....banana....rrr
# strip method: banana

# __doc__:
#     The swapcase() method returns a string where all the upper case letters are lower case and vice versa.

# string_value: I could eat bananas all day
# partition method: ('I could eat ', 'bananas', ' all day')

# __doc__:
#     #Upper case the first letter in this sentence:
#     #The capitalize() method returns a string where the first character is upper case, and the rest is lower case.
#     #The first character is converted to upper case, and the rest are converted to lower case

# string_value: hello, and welcome to my world.
# capitalize method: Hello, and welcome to my world.

# __doc__:
#     #The casefold() method returns a string where all the characters are lower case.
#     #This method is similar to the lower() method, but the casefold() method is stronger, more aggressive,
#     # meaning that it will convert more characters into lower case, and will find more matches
#     # when comparing two strings and both are converted using the casefold() method

# string_value: Hello, And Welcome To My World!
# string_value using casefold method: hello, and welcome to my world!

# __doc__:
#     Given string will repalce with another string using str.replace()

# string_value: Hello, And Welcome To My World!
# string_value using replace method: Hello, All Welcome To My World!

# __doc__:
#     #Python - Slicing Strings
#     #You can return a range of characters by using the slice syntax.
#     #Specify the start index and the end index, separated by a colon, to return a part of the string.
#     #Get the characters from position 2 to position 5 (not included)

# string_value: Hello, World!
# string_output1: string_value[0:5]: Hello
# string_output2: string_value[-4:-1]:vHello
# positive slicing method
# string_value[2:5]: llo
# string_value[:5]: Hello
# string_value[:2]: He

# negative slicing method
# string_value[-5:-2],orl

# __doc__:
#     #UTF-8 encode the string:
#     #The encode() method encodes the string, using the specified encoding. If no encoding is specified, UTF-8 will be used.

# string_value: My name is Ståle
# string_value using encode method: b'My name is St\xc3\xa5le'
# string_value: My name is Ståle
# string_value using enocde backslashreplace method: b'My name is St\\xe5le'

# string_value: My name is Ståle
# string_value using encode ascii method: b'My name is Stle'

# string_value: My name is Ståle
# string_value using encode namereplace method: b'My name is St\\N{LATIN SMALL LETTER A WITH RING ABOVE}le'

# string_value: My name is Ståle
# string_value using encode replace method: b'My name is St?le'

# string_value: My name is Ståle
# string_value using encode xmlcharrefreplace method: b'My name is St&#229;le'

# __doc__:
#     #The count() method returns the number of times a specified value appears in the string.
#     #string.count(value, start, end)
#     #Search from position 10 to 24:
#     Return the number of times the value "apple" appears in the string:

# string_value: I love apples, apple are my favorite fruit
# center method: 2

# string_value: I love apples, apple are my favorite fruit
# count method: 1

# __doc__:
#     #The center() method will center align the string, using a specified character (space is default) as the fill character.
#     #string.center(length, character)
#     #length     Required. The length of the returned string
#     #character  Optional. The character to fill the missing space on each side. Default is " " (space)

# string_value: banana

# center method:        banana

# string_value1: banana
# Cenetr Method: OOOOOOObananaOOOOOOO

# __doc__:
#     The isidentifier() method returns True if the string is a valid identifier, otherwise False.
#     A string is considered a valid identifier if it only contains alphanumeric letters (a-z) and (0-9), or underscores (_). A valid identifier cannot start with a number, or contain any spaces.

# string_value: I love apples, apple are my favorite fruit
# isidentifier method: False

# __doc__:
#     Create a mapping table, and use it in the translate() method to replace any "S" characters with a "P" character:
#     The maketrans() method returns a mapping table that can be used with the translate() method to replace specified characters.     
#     Use the maketrans() method to create a mapping table.

# string_value: Hello Sam!, string_value using maketrans method: {83: 80}
# string_value: Hello Sam!
# translate method: Hello Pam!

# __doc__:
#     Make the first letter in each word upper case
#     The title() method returns a string where the first character in every word is upper case. Like a header, or a title.
#     If the word contains a number or a symbol, the first letter after that will be converted to upper case.
#     txt = "hello b2b2b2 and 3g3g3g"
#     x = txt.title()
#     print(x)
#     Hello B2B2B2 And 3G3G3G

# string_value: Welcome to my 2nd world
# title method: Welcome To My 2Nd World

# __doc__:
#     Fill the string with zeros until it is 10 characters long:
#     The zfill() method adds zeros (0) at the beginning of the string, until it reaches the specified length.
#     If the value of the len parameter is less than the length of the string, no filling is done.

# string_value: 12345
# zfill method: 0000012345

# __doc__:
#     The isalnum() method returns True if all the characters are alphanumeric, meaning alphabet letter (a-z) and numbers (0-9).       
#     Example of characters that are not alphanumeric: (space)!#%&? etc.

# string_value: Company12
# alpha method: True

# __doc__:
#     The isalpha() method returns True if all the characters are alphabet letters (a-z).
#     Example of characters that are not alphabet letters: (space)!#%&? etc.

# string_value: CompanyX
# isalpha method: True

# __doc__:
#     The isascii() method returns True if all the characters are ascii characters  (a-z).

# string_value: Company123
# isascii method: True

# __doc__:
#     The isdecimal() method returns True if all the characters are decimals (0-9).
#     This method can also be used on unicode objects

# string_value: 123
# isdecimal method: True

# __doc__:
#     The isnumeric() method returns True if all the characters are numeric (0-9), otherwise False.
#     Exponents, like ² and ¾ are also considered to be numeric values.
#     "-1" and "1.5" are NOT considered numeric values, because all the characters in the string must be numeric, and the - and the . are not.

# string_value: 565543
# isnumeric method: True

# __doc__:
#     The isprintable() method returns True if all the characters are printable, otherwise False.
#     Example of none printable character can be carriage return and line feed.

# string_value: Hello!
# Are you #1?
# isprintable method: False

# __doc__:
#     The isspace() method returns True if all the characters in a string are whitespaces, otherwise False.

# string_value:
# isspace method: True

# __doc__:
#     The istitle() method returns True if all words in a text start with a upper case letter, AND the rest of the word are lower case letters, otherwise False.
#     Symbols and numbers are ignored.

# string_value: Hello, And Welcome To My World!
# istitle method: True

# __doc__:
#     The ljust() method will left align the string, using a specified character (space is default) as the fill character.
#     string.ljust(length, character)
#     length -    Required. The length of the returned string
#     character - Optional. A character to fill the missing space (to the left of the string). Default is " " (space).

# string_value: Hello, And Welcome To My World!
# ljust method: Hello, And Welcome To My World!

# __doc__:
#     The rjust() method will right align the string, using a specified character (space is default) as the fill character.
#     string.rjust(length, character)

# string_value: Hello, And Welcome To My World!
# rjust method: Hello, And Welcome To My World!

# __doc__:
#     The isalpha() method returns True if all the characters are alphabet letters (a-z).
#     Example of characters that are not alphabet letters: (space)!#%&? etc.

# string_value: Hello, And Welcome To My World!
# lstrip method: Hello, And Welcome To My World!

# __doc__:
#     The isalpha() method returns True if all the characters are alphabet letters (a-z).
#     Example of characters that are not alphabet letters: (space)!#%&? etc.

# string_value: Hello, And Welcome To My World!
# rfind method: 11

# __doc__:
#     The rindex() method finds the last occurrence of the specified value.
#     The rindex() method raises an exception if the value is not found.
#     The rindex() method is almost the same as the rfind() method.
#     string.rindex(value, start, end)
#     value - Required. The value to search for
#     start - Optional. Where to start the search. Default is 0
#     end - Optional. Where to end the search. Default is to the end of the string

# string_value: Hello, And Welcome To My World!
# rindex method: 11

# __doc__:
#     The rpartition() method searches for the last occurrence of a specified string, and splits the string into a tuple containing three elements.
#     The first element contains the part before the specified string.
#     The second element contains the specified string.
#     The third element contains the part after the string.
#     string.rpartition(value)
#     value - Required. The string to search for

# string_value: Hello, And Welcome To My World!
# rpartition method: ('Hello, And ', 'Welcome', ' To My World!')

# __doc__:
#     The rsplit() method splits a string into a list, starting from the right.
#     If no "max" is specified, this method will return the same as the split() method.
#     seperator - Optional. Specifies the separator to use when splitting the string. By default any whitespace is a separator
#     maxaplit - Optional. Specifies how many splits to do. Default value is -1, which is "all occurrences"

# string_value: Hello, And Welcome To My World!
# rsplit method: ['Hello, And ', ' To My World!']

# __doc__:
#     The rstrip() method removes any trailing characters (characters at the end a string), space is the default trailing character to remove.
#     string.rstrip(characters)
#     characters -        Optional. A set of characters to remove as trailing characters

# string_value: Hello, And Welcome To My World!
# rstrip method: Hello, And Welcome To My World!


# ----------------------------------------------------------------------
# Ran 0 tests in 0.000s

# OK
# PS C:\Users\Anamika\Python_codes\myenv\tests\Python_Basics> 