import unittest

def test_indentation():
    """
    Python Indentation - Indentation refers to the spaces at the beginning of a code line.
    Where in other programming languages the indentation in code is for readability only, the indentation in Python is very important.
    Python uses indentation to indicate a block of code.
    Python will give you an error if you skip the indentation:
    Indentation refers to the spaces at the beginning of a code line.
    """

    # Execute Python Syntax - As we learned in the previous page, Python syntax can be executed by writing directly in the Command Line:
    # print("Hello, World!")
    # Hello, World! Or by creating a python file on the server, using the .py file extension, and running it in the Command Line:
    # python myfile.py
    # Example
    # Syntax Error:
    # if 5 > 2:
    #     print("Five is greater than two!")
    # The number of spaces is up to you as a programmer, the most common use is four, but it has to be at least one.
    # Example
    # if 5 > 2:
    #     print("Five is greater than two!")
    # if 5 > 2:
    #     print("Five is greater than two!")
    # You have to use the same number of spaces in the same block of code, otherwise Python will give you an error:
    # Example
    # Syntax Error:
    # if 5 > 2:
    #     print("Five is greater than two!")
    #     print("Five is greater than two!")
    # Hello, World!
    # Five is greater than two!
    print(f'__doc__: {test_indentation.__doc__}')

    print("Hello, World!")
    if 5 > 2:
        print(f"Five is greater than two: 5 > 2!\n")

if __name__ == '__main__':
    test_indentation()
    unittest.main()

# ------------------------------Program Output----------------------------------------
# PS C:\Users\Anamika\Python_codes\myenv\tests\Python_Basics> python .\test_Indendations.py
# __doc__: 
#     Python Indentation - Indentation refers to the spaces at the beginning of a code line.
#     Where in other programming languages the indentation in code is for readability only, the indentation in Python is very important.
#     Python uses indentation to indicate a block of code.
#     Python will give you an error if you skip the indentation:
#     Indentation refers to the spaces at the beginning of a code line.

# Hello, World!
# Five is greater than two: 5 > 2!


# ----------------------------------------------------------------------
# Ran 0 tests in 0.000s

# OK
# PS C:\Users\Anamika\Python_codes\myenv\tests\Python_Basics> 