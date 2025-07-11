
import unittest


def test_integers():
    """
    Python Numbers
    There are three numeric types in Python:
    int
    float
    complex
    <class 'int'>
    <class 'float'>
    <class 'complex'>
    1.0
    2.5
    (1+0j)
    <class 'float'>
    <class 'int'>
    <class 'complex'>
    #Variables of numeric types are created when you assign a value to them:
    #To verify the type of any object in Python, use the type() function:
    # Int, or integer, is a whole number, positive or negative, without decimals, of unlimited length.
    """
    x = 1    # int
    y = 2.8  # float
    z = 1j   # complex
    # Integers:
    #print(f'__doc__: {test_integers.__doc__}')

    print(f'Integer numbers')
    print(f'variable x: {x}')
    #print("type of x:", {type(x)})
    print(f'variable y: {y}')
    #print("type of y:", {type(y)})
    print(f'variable z: {z}')
    #print("type of z:", {type(z)})
  
    x1 = 1
    y1 = 35656222554887711
    z1 = -3255522
    
    print(f'variable x1: {x1}')
    #print("type of x1:", {type(x1)})
    print(f'variable y1: {y1}')
    #print("type of y1:", {type(y1)})
    print(f'variable z1: {z1}')
    #print("type of z1:", {type(z1)})


def test_float():
    """
    #Float, or "floating point number" is a number, positive or negative, containing one or more decimals.
    #Float can also be scientific numbers with an "e" to indicate the power of 10.
    """
    x2 = 1.10
    y2 = 1.0
    z2 = -35.59
    print(f'float numbers')
    print(f'variable x2: {x2}')
    #print("type of x2:", {type(x2)})
    print(f'variable y2: {y2}')
    #print("type of y2:", {type(y2)})
    print(f'variable z2: {z2}')
    #print("type of z2:", {type(z2)})


    x3 = 35e3
    y3 = 12E4
    z3 = -87.7e100
   
    
    print(f'variable x3: {x3}')
    #print("type of x3:", {type(x3)})
    print(f'variable y3: {y3}')
    #print("type of y3:", {type(y3)})
    print(f'variable z3: {z3}')
    #print("type of z3:", {type(z3)})



def test_complex():
    """
    #Complex numbers are written with a "j" as the imaginary part
    #Type Conversion
    #You can convert from one type to another with the int(), float(), and complex() methods:
    #Convert from one type to another
    #Note: You cannot convert complex numbers into another number type.
    #Random Number
    #Python does not have a random() function to make a random number, but Python has a built-in module called random that can be used to make random numbers:
    #Example
    #Import the random module, and display a random number from 1 to 9:
    #import random
    #print(random.randrange(1, 10))
    """
    x = 3+5j
    y = 5j
    z = -5j
    print(f'complex numbers')
    print(f'variable x: {x}')
    #print("type of x:", {type(x)})
    print(f'variable y: {y}')
    #print("type of y:", {type(y))
    print(f'variable z: {z}')
    #print("type of z:", {type(z))

    x = 1    # int
    y = 2.8  # float
    z = 1j   # complex

    #convert from int to float:
    a = float(x)

    #convert from float to int:
    b = int(y)

    #convert from int to complex:
    c = complex(x)

    print(f'variable a: {a}')
    #print("type of a:", (type(a)})
    print(f'variable b: {b}')
    #print("type of b:", (type(b)})
    print(f'variable c: {c}')
    #print("type of c:", (type(c)})



if __name__ == '__main__':
    test_integers()
    test_float()
    test_complex()
    unittest.main()

    # --------------------------------Program Output ---------------------------------------------
    # PS C:\Users\Anamika\Python_codes\myenv\tests\Python_Basics> & C:/Users/Anamika/Python_codes/myenv/Scripts/python.exe c:/Users/Anamika/Python_codes/myenv/tests/Python_Basics/test_numbers.py
    # __doc__:
    #     Python Numbers
    #     There are three numeric types in Python:
    #     int
    #     float
    #     complex
    #     <class 'int'>
    #     <class 'float'>
    #     <class 'complex'>
    #     1.0
    #     2
    #     (1+0j)
    #     <class 'float'>
    #     <class 'int'>
    #     <class 'complex'>
    #     #Variables of numeric types are created when you assign a value to them:
    #     #To verify the type of any object in Python, use the type() function:
    #     # Int, or integer, is a whole number, positive or negative, without decimals, of unlimited length.

    # variable, type of x variable, 1, <class 'int'>
    # variable, type of y variable, 2.8, <class 'float'>
    # variable, type of x variable, 1j, <class 'complex'>
    # variable, type of x1 variable, 1, <class 'int'>
    # variable, type of y1 variable, 35656222554887711, <class 'int'>
    # variable, type of z1 variable, -3255522, <class 'int'>
    # variable, type of x2 variable, 1.1, <class 'float'>
    # variable, type of y2 variable, 1.0, <class 'float'>
    # variable, type of z2 variable, -35.59, <class 'float'>
    # variable, type of x3 variable, 35000.0, <class 'float'>
    # variable, type of y3 variable, 120000.0, <class 'float'>
    # variable, type of z3 variable, -8.77e+101, <class 'float'>
    # variable, type of x variable, (3+5j), <class 'complex'>
    # variable, type of y variable, 5j, <class 'complex'>
    # variable, type of x variable, (-0-5j), <class 'complex'>
    # variable, type of a variable, 1.0, <class 'float'>
    # variable, type of b variable, 2, <class 'int'>
    # variable, type of c variable, (1+0j), <class 'complex'>

    # ----------------------------------------------------------------------
    # Ran 0 tests in 0.000s

    # OK
    # PS C:\Users\Anamika\Python_codes\myenv\tests\Python_Basics> 