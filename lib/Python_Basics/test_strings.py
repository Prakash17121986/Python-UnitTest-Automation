import unittest

def test_single_quote_string(string_value = 'Hello, World!'):
    """
    #Strings
    #Strings in python are surrounded by either single quotation marks, or double quotation marks. 
    # 'hello world' is the same as "hello world".
    # You can display a string literal with the print() function:
    """
    print(f'__doc__: {test_single_quote_string.__doc__}')
    print("Single Quoted String:",string_value)

def test_double_quote_string(string_value = "Hello, World!"):
    """
    #Strings in python are surrounded by either single quotation marks, or double quotation marks. 'hello world' is the same as "hello".
    #You can display a string literal with the print() function:
    """
    print(f'__doc__: {test_double_quote_string.__doc__}\n')
    print("Double Quoted String:", string_value)


def test_three_quote_string(string_value = "Hello world"):
    """
    #Quotes Inside Quotes
    #You can use quotes inside a string, as long as they don't match the quotes surrounding the string:
    #Assigning a string to a variable is done with the variable name followed by an equal sign and the string:
    #Multiline Strings - You can assign a multiline string to a variable by using three quotes:
    #You can use three double quotes:
    #Strings are Arrays
    #Like many other popular programming languages, strings in Python are arrays of bytes representing unicode characters.
    #However, Python does not have a character data type, a single character is simply a string with a length of 1.
    #Square brackets can be used to access elements of the string.
    """
    print(f'__doc__: {test_three_quote_string.__doc__}\n')
    
    print(f"Hi, How are you")
    print(f"Someone is there'")
    print(f'Look behind you"')

    print(f"String value: {string_value}")

    text = """Hi,
    hello,
    How are you!    
    Where are you."""

    print(f"Three double Quoted string with text variable : {text}\n")

    #Or three single quotes:
    text = '''Hi,
    hello,
    How are you!    
    Where are you.'''

    print(f"Three single Quoted string with text variable: {text}\n")


def test_string_char_read(string_value = "Hello, World!"):
    """
    #Get the character at position 1 (remember that the first character has the position 0):
    """
    print(f'__doc__: {test_string_char_read.__doc__}')
    string_value = "Hello, World!"
    print(f"string_value: {string_value}")
    print(f"Get the string character at position 0 to 10: {string_value[0:10]}\n") 

def test_string_length(string_value = "Hello, World!"):
    """
    #The len() function returns the length of a string:

    """
    print(f'__doc__: {test_string_length.__doc__}')
    string_value = "Hello, World!" #Assign String to a Variable
    print(f"string_value: {string_value}, length of string_value: {len(string_value)}\n")

def test_string_loop(string_value = "Hello, World!"):
    """
    #Looping Through a String
    #Since strings are arrays, we can loop through the characters in a string, with a for loop.
    #Loop through the letters in the word "banana":
    """
    print(f'__doc__: {test_string_loop.__doc__}')

    #Check String
    #To check if a certain phrase or character is present in a string, we can use the keyword in.
    #Check if "free" is present in the following text:

    #Strings are Arrays
    for indx, value in enumerate(string_value):
        print(f'string_value: {string_value[indx]}\n)')
        print(f'string_value: {value}\n')

    #Loop through the char in the word string_value
    for char in string_value:
        print(f"char; {char}")

def test_check_string(string_value = "Hello, World!"):
    '''
    To check if a certain phrase or character is present in a string, we can use the keyword in.
    Check if "Hello" is present in the following string_value:
    '''
    print(f'__doc__: {test_check_string.__doc__}')
    if "Hello" in string_value:
      print(f"Yes, 'Hello' is present.\n")

def test_check_if_not_in_string(string_value = "Hello, World!"):
    '''
    To check if a certain phrase or character is NOT present in a string, we can use the keyword not in.
    '''
    print(f'__doc__: {test_check_if_not_in_string.__doc__}')
    #Check if NOT
    if "Hi" not in string_value:
        print(f"No, 'Hi' not present.\n")

def test_concatenate_strings(string_value1="hello", string_value2="world"):
    '''
    String Concatenation - To concatenate, or combine, two strings you can use the + operator.
    To add a space between them, add a " "
    '''
    print(f'__doc__: {test_concatenate_strings.__doc__}')
    result = string_value1 + " " + string_value2
    print(f"Concatenation of string_value1 and string_value2: {result}\n")

def test_string_format():
    '''
    we can combine strings and numbers by using f-strings or the format() method
    f-string -f in front of the string literal, and add curly brackets {} as placeholders for variables and other operations.
    
    Placeholders and Modifiers
    A placeholder can contain variables, operations, functions, and modifiers to format the value.
    A modifier is included by adding a colon : followed by a legal formatting type, like .2f which means fixed point number with 2 decimals
    '''
    print(f'__doc__: {test_string_format.__doc__}')
    #age = 36
    #string_value = "My name is John, I am " + age #we cannot combine strings and numbers 

    age = 36
    string_value = f"My name is John, I am {age}"
    print(f"format the string: {string_value}")

    price = 59
    string_value = f"The price is {price} dollars" # Add a placeholder for the price variable
    print(f"format the string - Add a placeholder for the price variable: {string_value}")
    
    string_value = f"The price is {20 * 59} dollars"
    print(f"format the string - Add a placeholder for the price variable and do math operation: {string_value}\n")

def test_escape_character_in_strings(string_value="hello"):
    '''
    An escape character is a backslash \ followed by the character you want to insert.
    '''
    print(f'__doc__: {test_escape_character_in_strings.__doc__}')

    #string_value = "We are the so-called "Vikings" from the north." #Not allowed to add "Vikings" in string

    string_value = "We are the so-called \"Vikings\" from the north."
    print(f"include a string value using \": {string_value}\n")

def test_slicing(string_value="hello"):
    '''
    You can return a range of characters by using the slice syntax.
    Specify the start index and the end index, separated by a colon, to return a part of the string.
    '''
    print(f'__doc__: {test_slicing.__doc__}')
    #Get the characters from position 0 to position 4 using positive index number
    print(f"string slicing [0:len(string_value): step]: {string_value[:]}")

    #Get the characters from position 0 to position 4 using positive index number
    print(f"string slicing [0:len(string_value): step]: {string_value[0:4]}")

    #Get the characters from position 0 to position 4 using negative index number
    print(f"string negative slicing [0:len(string_value): step]: {string_value[-4:-1]}")

    #Get the characters from position 0 to position 4 using positive step index number
    print(f"string slicing [0:len(string_value): step]: {string_value[0:4:2]}")

    #Get the characters from position 0 to position 4 using negative step index number
    print(f"string negative slicing [0:len(string_value): step]: {string_value[-4:-1:-1]}\n")

def test_modify_strings(string_value="hello world "):
    '''
    Python has a set of built-in methods that you can use on strings.
    The upper() method returns the string in upper case
    The lower() method returns the string in lower case
    The strip() method removes any whitespace from the beginning or the end
    Whitespace is the space before and/or after the actual text
    The replace() method replaces a string with another string:
    '''
    print(f'__doc__: {test_modify_strings.__doc__}')
    print(f"class method: string upper: {string_value.upper()}")
    print(f"class method: string lower: {string_value.lower()}")
    print(f"class method: string strip: {string_value.strip()}")
    print(f"class method: string split: {string_value.split()}")
    print(f"class method: string split: {string_value.replace('hello', 'Hi Hello')}")

if __name__ =='__main__':
    test_single_quote_string(string_value = 'Hello, World!')
    test_double_quote_string(string_value = "Hello, World!")
    test_three_quote_string(string_value = "Hello world")
    test_string_char_read(string_value = "Hello, World!")
    test_string_length(string_value = "Hello, World!")
    test_string_loop(string_value = "Hello, World!")
    test_check_string(string_value = "Hello, World!")
    test_check_if_not_in_string(string_value = "Hello, World!")
    test_concatenate_strings(string_value1="hello", string_value2="world")
    test_string_format()
    test_escape_character_in_strings(string_value="hello")
    test_slicing(string_value="hello")
    test_modify_strings(string_value="hello world ")
    unittest.main()


# --------------------------------Program output-----------------------------------------------
# PS C:\Users\Anamika\Python_codes\myenv\tests\Python_Basics> python .\test_strings.py
# __doc__: 
#     #Strings
#     #Strings in python are surrounded by either single quotation marks, or double quotation marks. 
#     # 'hello world' is the same as "hello world".
#     # You can display a string literal with the print() function:
    
# Single Quoted String: Hello, World!
# __doc__:
#     #Strings in python are surrounded by either single quotation marks, or double quotation marks. 'hello world' is the same as "hello".
#     #You can display a string literal with the print() function:


# Double Quoted String: Hello, World!
# __doc__:
#     #Quotes Inside Quotes
#     #You can use quotes inside a string, as long as they don't match the quotes surrounding the string:
#     #Assigning a string to a variable is done with the variable name followed by an equal sign and the string:
#     #Multiline Strings - You can assign a multiline string to a variable by using three quotes:
#     #You can use three double quotes:
#     #Strings are Arrays
#     #Like many other popular programming languages, strings in Python are arrays of bytes representing unicode characters.
#     #However, Python does not have a character data type, a single character is simply a string with a length of 1.
#     #Square brackets can be used to access elements of the string.


# Hi, How are you
# Someone is there'
# Look behind you"
# String value: Hello world
# Three double Quoted string with text variable : Hi,
#     hello,
#     How are you!
#     Where are you.

# Three single Quoted string with text variable: Hi,
#     hello,
#     How are you!
#     Where are you.

# __doc__:
#     #Get the character at position 1 (remember that the first character has the position 0):

# string_value: Hello, World!
# Get the string character at position 0 to 10: Hello, Wor

# __doc__:
#     #The len() function returns the length of a string:


# string_value: Hello, World!, length of string_value: 13

# __doc__:
#     #Looping Through a String
#     #Since strings are arrays, we can loop through the characters in a string, with a for loop.
#     #Loop through the letters in the word "banana":

# string_value: H
# )
# string_value: H

# string_value: e
# )
# string_value: e

# string_value: l
# )
# string_value: l

# string_value: l
# )
# string_value: l

# string_value: o
# )
# string_value: o

# string_value: ,
# )
# string_value: ,

# string_value:
# )
# string_value:

# string_value: W
# )
# string_value: W

# string_value: o
# )
# string_value: o

# string_value: r
# )
# string_value: r

# string_value: l
# )
# string_value: l

# string_value: d
# )
# string_value: d

# string_value: !
# )
# string_value: !

# char; H
# char; e
# char; l
# char; l
# char; o
# char; ,
# char;
# char; W
# char; o
# char; r
# char; l
# char; d
# char; !
# __doc__:
#     To check if a certain phrase or character is present in a string, we can use the keyword in.
#     Check if "Hello" is present in the following string_value:

# Yes, 'Hello' is present.

# __doc__:
#     To check if a certain phrase or character is NOT present in a string, we can use the keyword not in.

# No, 'Hi' not present.

# __doc__:
#     String Concatenation - To concatenate, or combine, two strings you can use the + operator.
#     To add a space between them, add a " "

# Concatenation of string_value1 and string_value2: hello world

# __doc__:
#     we can combine strings and numbers by using f-strings or the format() method
#     f-string -f in front of the string literal, and add curly brackets {} as placeholders for variables and other operations.        

#     Placeholders and Modifiers
#     A placeholder can contain variables, operations, functions, and modifiers to format the value.
#     A modifier is included by adding a colon : followed by a legal formatting type, like .2f which means fixed point number with 2 decimals

# format the string: My name is John, I am 36
# format the string - Add a placeholder for the price variable: The price is 59 dollars
# format the string - Add a placeholder for the price variable and do math operation: The price is 1180 dollars

# __doc__:
#     An escape character is a backslash \ followed by the character you want to insert.

# include a string value using ": We are the so-called "Vikings" from the north.

# __doc__:
#     You can return a range of characters by using the slice syntax.
#     Specify the start index and the end index, separated by a colon, to return a part of the string.

# string slicing [0:len(string_value): step]: hello
# string slicing [0:len(string_value): step]: hell
# string negative slicing [0:len(string_value): step]: ell
# string slicing [0:len(string_value): step]: hl
# string negative slicing [0:len(string_value): step]:

# __doc__:
#     Python has a set of built-in methods that you can use on strings.
#     The upper() method returns the string in upper case
#     The lower() method returns the string in lower case
#     The strip() method removes any whitespace from the beginning or the end
#     Whitespace is the space before and/or after the actual text
#     The replace() method replaces a string with another string:

# class method: string upper: HELLO WORLD
# class method: string lower: hello world
# class method: string strip: hello world
# class method: string split: ['hello', 'world']
# class method: string split: Hi Hello world

# ----------------------------------------------------------------------
# Ran 0 tests in 0.000s

# OK
# PS C:\Users\Anamika\Python_codes\myenv\tests\Python_Basics> 

