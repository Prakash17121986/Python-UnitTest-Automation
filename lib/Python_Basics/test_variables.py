import unittest

def test_variablenames():
    '''
    Variable Names - Legal variable names:
    A variable can have a short name (like x and y) or a more descriptive name (age, carname, total_volume). Rules for Python variables:
    A variable name must start with a letter or the underscore character
    A variable name cannot start with a number
    A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
    Variable names are case-sensitive (age, Age and AGE are three different variables)
    A variable name cannot be any of the Python keywords.

    Example
    Illegal variable names:
    2myvar = "John"
    my-var = "John"
    my var = "John
    '''
    myvar = "John"
    my_var = "John"
    _my_var = "John"
    myVar = "John"
    MYVAR = "John"
    myvar2 = "John"
    print(f'myvar: {myvar}')
    print(f'my_var: {myvar}')
    print(f'_my_var: {myvar}')
    print(f'MYVAR: {MYVAR}')
    print(f'myvar2: {myvar2}')



# Creating Variables

def test_createvariables():

    x1 = str(3)    # x will be '3'
    y1 = int(3)    # y will be 3
    z1 = float(3)  # z will be 3.0
    x2 = 5
    y3 = "John"

    #Get the Type
    #You can get the data type of each variable with the type() function.
    print(f'x1: {x1}, type: {type(x1)}')
    print(f'y1: {y1},type: {type(y1)}')
    print(f'z1: {z1},type: {type(z1)}')
    print(f'x2: {x2},type: {type(x2)}')
    print(f'y3: {y3},type: {type(y3)}')

    #Single or Double Quotes?
    #String variables can be declared either by using single or double quotes:
    x3 = "John"
    print(f'x3 variable in double quotes, x3: {x3},type: {type(x3)}')
    # is the same as
    y4 = 'John'
    print(f'y3 variable in single quotes, y3: {y4},type: {type(y4)}')
    #Case-Sensitive
    #Variable names are case-sensitive.
    a = 4
    A = "Sally"
    print(f'a variable in case-sensitive, a: {a},type: {type(a)}')
    print(f'a variable in case-sensitive, A: {A},type: {type(A)}')
    #A will not overwrite a

    #Type Casting
    #If you want to specify the data type of each variable, this can be done with casting.
    x5 = str(3)    # x5 will be '3'
    y5 = int(3)    # y5 will be 3
    z5 = float(3)  # z5 will be 3.0
    x6 = list([1,2,3]) # x6 will be [1,2,3]
    x7 = dict({'a':1})
    x8 = tuple((1,2,3))
    x9 = set({1,2,3})
    print(f'Data type of each variable using casting str() x5: {x5},type: {type(x5)}')
    print(f'Data type of each variable using casting int() y5: {y5},type: {type(y5)}')
    print(f'Data type of each variable using casting float() z5: {z5},type: {type(z5)}')
    print(f'Data type of each variable using casting list() x6: {x6},type: {type(x6)}')
    print(f'Data type of each variable using casting dict() x7: {x7},type: {type(x7)}')
    print(f'Data type of each variable using casting tuple() x8: {x8},type: {type(x8)}')
    print(f'Data type of each variable using casting tuple() x9: {x9},type: {type(x9)}')

    #Many Values to Multiple Variables
    #Python allows you to assign values to multiple variables in one line:
    x_, y_, z_ = "Orange", "Banana", "Cherry"
    print(f"Multiple variables name x_, y_, z_ with different value : {x_}, {y_}, {z_}")

    #One Value to Multiple Variables
    #And you can assign the same value to multiple variables in one line:
    x_1 = y_1 = z_1 = "Orange"
    print(f"One value 'orange' with Multiple variables name x_1_, y_1, z_1 : {x_1}, {y_1}, {z_1}")


    #Unpack a Collection
    #If you have a collection of values in a list, tuple etc. Python allows you to extract the values into variables. This is called unpacking.
    #Unpack a list:
    fruits = ["apple", "banana", "cherry"]
    print(f'fruits: {fruits}')
    _x, _y, _z = fruits
    print(f"Unpack the {fruits} values with different variable value _x, _y, _z: {_x, _y, _z}")

    # Python - Output Variables
    # Output Variables
    # The Python print() function is often used to output variables.
    _x_ = "Python is awesome"
    print(f"The Python print() function is often used to output variables: {_x_}")

    # In the print() function, you output multiple variables, separated by a comma:
    _x__ = "Python"
    _y__ = "is"
    _z__ = "awesome"
    print(f"In the print() function, you output multiple variables, separated by a comma: {_x__, _y__, _z__}")

    # You can also use the + operator to output multiple variables:
    x__ = "Python "
    y__ = "is "
    z__ = "awesome"
    print(f'Use + operator to output multiple variables even with space character "Python " and "is ": {x__ + y__ + z__}') # Notice the space character after "Python " and "is ", without them the result would be "Pythonisawesome".

    # For numbers, the + character works as a mathematical operator:
    x_1 = 5
    y_1 = 10
    print(f'For numbers x_1, y_1: {x_1}, {y_1}, + character works as a mathematical operator: {x_1 + y_1}')

    #The best way to output multiple variables in the print() function is to separate them with commas, which even support different data types:
    x_2 = 5
    y_2 = "John"
    print(f'print() function is to separate them with commas of output multiple variables with different data types : {x_2, y_2}')


if __name__ == '__main__':
    test_variablenames()
    test_createvariables()
    unittest.main()

# --------------------------------Program Output--------------------------------------------
# PS C:\Users\Anamika\Python_codes\myenv\tests\Python_Basics> python .\test_variables.py
# Create a variable outside a function with the same name as the global variable: new begining
# Create a variable x1 outside a function: awesome
# myvar: John
# my_var: John
# _my_var: John
# MYVAR: John
# myvar2: John
# x1: 3, type: <class 'str'>
# y1: 3,type: <class 'int'>
# z1: 3.0,type: <class 'float'>
# x2: 5,type: <class 'int'>
# y3: John,type: <class 'str'>
# x3 variable in double quotes, x3: John,type: <class 'str'>
# y3 variable in single quotes, y3: John,type: <class 'str'>
# a variable in case-sensitive, a: 4,type: <class 'int'>
# a variable in case-sensitive, A: Sally,type: <class 'str'>
# Data type of each variable using casting str() x5: 3,type: <class 'str'>
# Data type of each variable using casting int() y5: 3,type: <class 'int'>
# Data type of each variable using casting float() z5: 3.0,type: <class 'float'>
# Data type of each variable using casting list() x6: [1, 2, 3],type: <class 'list'>
# Data type of each variable using casting dict() x7: {'a': 1},type: <class 'dict'>
# Data type of each variable using casting tuple() x8: (1, 2, 3),type: <class 'tuple'>
# Data type of each variable using casting tuple() x9: {1, 2, 3},type: <class 'set'>
# Multiple variables name x_, y_, z_ with different value : Orange, Banana, Cherry
# One value 'orange' with Multiple variables name x_1_, y_1, z_1 : Orange, Orange, Orange
# fruits: ['apple', 'banana', 'cherry']
# Unpack the ['apple', 'banana', 'cherry'] values with different variable value _x, _y, _z: ('apple', 'banana', 'cherry')
# The Python print() function is often used to output variables: Python is awesome
# In the print() function, you output multiple variables, separated by a comma: ('Python', 'is', 'awesome')
# Use + operator to output multiple variables even with space character "Python " and "is ": Python is awesome
# For numbers x_1, y_1: 5, 10, + character works as a mathematical operator: 15
# print() function is to separate them with commas of output multiple variables with different data types : (5, 'John')
# Create a variable inside a function with the same name as the global variable: fantastic
# Global variable outside: awesome
# Global variable used inside a function x1: awesome
# Not assigning any value to x1 in inside the function: awesome
# After assigning value to x1 in inside the function: fantastic
# Global variable inside function assigned with 'fantastic' value for x1 variable: fantastic
# Inside function accessing outside variable x:  awesome
# Python is awesome
# Inside function accessing inside global variable x :fantastic
# Python is fantastic

# ----------------------------------------------------------------------
# Ran 0 tests in 0.000s

# OK
# PS C:\Users\Anamika\Python_codes\myenv\tests\Python_Basics> 