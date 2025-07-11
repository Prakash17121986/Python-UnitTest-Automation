import unittest

def test_typecasting():
    '''
    Specify a Variable Type
    There may be times when you want to specify a type on to a variable.
    This can be done with casting. Python is an object-orientated language, and as such it uses classes to define data types, including its primitive types.
    Casting in python is therefore done using constructor functions:
    int() - constructs an integer number from an integer literal, a float literal (by removing all decimals), or a string literal (providing the string represents a whole number)
    float() - constructs a float number from an float literal, a float literal or a string literal (providing the string represents a float or an integer)
    str() - constructs a string from a wide variety of data types, including strings, integer literals and float literals
    '''
    #print(f'__doc__: {test_typecasting.__doc__}')
    #Integers:

    x = int(1)   # x will be 1
    y = int(2.8) # y will be 2
    z = int("3") # z will be 3
    print(f'{x}: type of x: {type(x)}')
    print(f'{y}: type of y: {type(y)}')
    print(f'{z}, type of z: {type(z)}')


    #Floats
    x1 = float(1)     # x will be 1.0
    y1 = float(2.8)   # y will be 2.8
    z1 = float("3")   # z will be 3.0
    print(f'{x1}: type of x1: {type(x1)}')
    print(f'{y1}: type of y1: {type(y1)}')
    print(f'{z1}, type of z1: {type(z1)}')
    #Strings:

    x2 = str("s1") # x will be 's1'
    y2 = str(2)    # y will be '2'
    z2 = str(3.0)  # z will be '3.0'
    print(f'{x2}: type of x2: {type(x2)}')
    print(f'{y2}: type of y2: {type(y2)}')
    print(f'{z2}, type of z2: {type(z2)}')



if __name__ == '__main__':
    test_typecasting()
    unittest.main()

# --------------------------------------Program Output------------------------------------
# PS C:\Users\Anamika\Python_codes\myenv\tests\Python_Basics> python .\test_type_casting.py
# __doc__: 
#     Specify a Variable Type
#     There may be times when you want to specify a type on to a variable.
#     This can be done with casting. Python is an object-orientated language, and as such it uses classes to define data types, including its primitive types.
#     Casting in python is therefore done using constructor functions:
#     int() - constructs an integer number from an integer literal, a float literal (by removing all decimals), or a string literal (providing the string represents a whole number)
#     float() - constructs a float number from an float literal, a float literal or a string literal (providing the string represents a float or an integer)
#     str() - constructs a string from a wide variety of data types, including strings, integer literals and float literals

# 1: type of x: <class 'int'>
# 2: type of y: <class 'int'>
# 3, type of z: <class 'int'>
# 1.0: type of x1: <class 'float'>
# 2.8: type of y1: <class 'float'>
# 3.0, type of z1: <class 'float'>
# s1: type of x2: <class 'str'>
# 2: type of y2: <class 'str'>
# 3.0, type of z2: <class 'str'>

# ----------------------------------------------------------------------
# Ran 0 tests in 0.000s

# OK
# PS C:\Users\Anamika\Python_codes\myenv\tests\Python_Basics> 