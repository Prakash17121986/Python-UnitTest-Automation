import unittest

def test_datatypes_func():
    """
    Built-in Data Types
    In programming, data type is an important concept.
    Variables can store data of different types, and different types can do different things.
    Python has the following data types built-in by default, in these categories:
    Text Type:	str
    Numeric Types:	int, float, complex
    Sequence Types:	list, tuple, range
    Mapping Type:	dict
    Set Types:	set, frozenset
    Boolean Type:	bool
    Binary Types:	bytes, bytearray, memoryview
    None Type:	NoneType
    You can get the data type of any object by using the type() function:
    Print the data type of the variable x
    """
    print(f'__doc__: {test_datatypes_func.__doc__}')



def test_datatypes_string():
    """
    Text Type:	str
    """
    print(f'__doc__: {test_datatypes_string.__doc__}')
    x = 5
    print(f'type of x variable, {type(x)}')
    x1 = "Hello World" #string
    print(f'variable, type of x1 variable, {x1}, {type(x1)}\n')

test_datatypes_func()

def test_datatypes_integer():
    """
    Numeric Types:	int
    """
    print(f'__doc__: {test_datatypes_integer.__doc__}')
    x2 = 20 # integer
    print(f'variable, type of x2 variable, {x2}, {type(x2)}\n')


def test_datatypes_float():
    """
    Numeric Types:	float
    """
    print(f'__doc__: {test_datatypes_float.__doc__}')

    x3 = 2.5  # integer
    print(f'variable, type of x3 variable, {x3}, {type(x3)}\n')


def test_datatypes_complex():
    """
    Numeric Types:	complex
    """
    print(f'__doc__: {test_datatypes_complex.__doc__}')

    x4 = 1j
    print(f'variable, type of x4 variable, {x4}, {type(x4)}\n')


def test_datatypes_list():
    """
    Sequence Types:	list
    """
    print(f'__doc__: {test_datatypes_list.__doc__}')
    x5 = ["apple", "banana", "cherry"] # list
    print(f'variable, type of x5 variable, {x5}, {type(x5)}\n')


def test_datatypes_tuple():
    """
    Sequence Types:	tuple
    """
    print(f'__doc__: {test_datatypes_tuple.__doc__}')
    x6 = ("apple", "banana", "cherry") # tuple
    print(f'variable, type of x6 variable, {x6}, {type(x6)}\n')



def test_datatypes_range():
    """
    Sequence Types:	range
    """
    print(f'__doc__: {test_datatypes_range.__doc__}')
    x7 = range(6) # range
    print(f'variable, type of x7 variable, {x7}, {type(x7)}\n')



def test_datatypes_dictionary():
    """
    Sequence Types:	range
    """
    print(f'__doc__: {test_datatypes_dictionary.__doc__}')
    x8 = {"name" : "John", "age" : 36} # dict
    print(f'variable, type of x8 variable, {x8}, {type(x8)}\n')


def test_datatypes_set():
    """
    Set Types:	set
    """
    print(f'__doc__: {test_datatypes_set.__doc__}')
    x9 = {"apple", "banana", "cherry"} # set
    print(f'variable, type of x9 variable, {x9}, {type(x9)}\n')



def test_datatypes_frozenset():
    """
    Set Types:	frozenset
    """
    print(f'__doc__: {test_datatypes_frozenset.__doc__}')
    x10 = frozenset({"apple", "banana", "cherry"}) # frozen set
    print(f'variable, type of x10 variable, {x10}, {type(x10)}\n')



def test_datatypes_bool():
    """
    Boolean Type:	bool
    """
    x11 = True # bool
    print(f'__doc__: {test_datatypes_bool.__doc__}')
    print(f'variable, type of x11 variable, {x11}, {type(x11)}\n')


def test_datatypes_bytes():
    """
    Binary Types: bytes
    """
    x12 = b"Hello" # bytes
    print(f'__doc__: {test_datatypes_bytes.__doc__}')
    print(f'variable, type of x12 variable, {x12}, {type(x12)}\n')


def test_datatypes_bytearray():
    """
    Binary Types: bytearray
    """
    x13 = bytearray(5) # byte array
    print(f'__doc__: {test_datatypes_bytearray.__doc__}')
    print(f'variable, type of x13 variable, {x13}, {type(x13)}\n')



def test_datatypes_memoryview():
    """
    Binary Types: memoryview
    """
    x14 = memoryview(bytes(5)) #memoryview
    print(f'__doc__: {test_datatypes_bytearray.__doc__}')
    print(f'variable, type of x14 variable, {x14}, {type(x14)}\n')



def test_datatypes_none():
    """
    Binary Types: memoryview
    """
    x15 = None # NoneType #None
    print(f'__doc__: {test_datatypes_none.__doc__}')
    print(f'variable, type of x1 variable, {x15}, {type(x15)}\n')



if __name__ == '__main__':
    test_datatypes_func()
    test_datatypes_bytes()
    test_datatypes_list()
    test_datatypes_string()
    test_datatypes_complex()
    test_datatypes_set()
    test_datatypes_range()
    test_datatypes_dictionary()
    test_datatypes_tuple()
    test_datatypes_frozenset()
    test_datatypes_bool()
    test_datatypes_bytearray()
    test_datatypes_memoryview()
    test_datatypes_none()
    unittest.main()

    # -------------------------Program output-------------------------------------

    # PS C:\Users\Anamika\Python_codes\myenv\tests\Python_Basics> python .\test_datatypes.py            
    # __doc__: 
    #     Built-in Data Types
    #     In programming, data type is an important concept.
    #     Variables can store data of different types, and different types can do different things.
    #     Python has the following data types built-in by default, in these categories:
    #     Text Type:  str
    #     Numeric Types:      int, float, complex
    #     Sequence Types:     list, tuple, range
    #     Mapping Type:       dict
    #     Set Types:  set, frozenset
    #     Boolean Type:       bool
    #     Binary Types:       bytes, bytearray, memoryview
    #     None Type:  NoneType
    #     You can get the data type of any object by using the type() function:
    #     Print the data type of the variable x

    # __doc__:
    #     Numeric Types:      int

    # variable, type of x2 variable, 20, <class 'int'>

    # __doc__:
    #     Numeric Types:      float

    # variable, type of x3 variable, 2.5, <class 'float'>

    # __doc__:
    #     Built-in Data Types
    #     In programming, data type is an important concept.
    #     Variables can store data of different types, and different types can do different things.
    #     Python has the following data types built-in by default, in these categories:
    #     Text Type:  str
    #     Numeric Types:      int, float, complex
    #     Sequence Types:     list, tuple, range
    #     Mapping Type:       dict
    #     Set Types:  set, frozenset
    #     Boolean Type:       bool
    #     Binary Types:       bytes, bytearray, memoryview
    #     None Type:  NoneType
    #     You can get the data type of any object by using the type() function:
    #     Print the data type of the variable x

    # __doc__:
    #     Binary Types: bytes

    # variable, type of x12 variable, b'Hello', <class 'bytes'>

    # __doc__:
    #     Sequence Types:     list

    # variable, type of x5 variable, ['apple', 'banana', 'cherry'], <class 'list'>

    # __doc__:
    #     Text Type:  str

    # type of x variable, <class 'int'>
    # variable, type of x1 variable, Hello World, <class 'str'>

    # __doc__:
    #     Numeric Types:      complex

    # variable, type of x4 variable, 1j, <class 'complex'>

    # __doc__:
    #     Set Types:  set

    # variable, type of x9 variable, {'apple', 'banana', 'cherry'}, <class 'set'>

    # __doc__:
    #     Sequence Types:     range

    # variable, type of x7 variable, range(0, 6), <class 'range'>

    # __doc__:
    #     Sequence Types:     range

    # variable, type of x8 variable, {'name': 'John', 'age': 36}, <class 'dict'>

    # __doc__:
    #     Sequence Types:     tuple

    # variable, type of x6 variable, ('apple', 'banana', 'cherry'), <class 'tuple'>

    # __doc__:
    #     Set Types:  frozenset

    # variable, type of x10 variable, frozenset({'apple', 'banana', 'cherry'}), <class 'frozenset'>

    # __doc__:
    #     Boolean Type:       bool

    # variable, type of x11 variable, True, <class 'bool'>

    # __doc__:
    #     Binary Types: bytearray

    # variable, type of x13 variable, bytearray(b'\x00\x00\x00\x00\x00'), <class 'bytearray'>

    # __doc__:
    #     Binary Types: bytearray

    # variable, type of x14 variable, <memory at 0x0000020C84EFE8C0>, <class 'memoryview'>

    # __doc__:
    #     Binary Types: memoryview

    # variable, type of x1 variable, None, <class 'NoneType'>


    # ----------------------------------------------------------------------
    # Ran 0 tests in 0.000s

    # OK
    # PS C:\Users\Anamika\Python_codes\myenv\tests\Python_Basics> 