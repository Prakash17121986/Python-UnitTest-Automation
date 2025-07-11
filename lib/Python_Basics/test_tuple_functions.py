import unittest

def test_create_tuple():
    """
    Tuple - Tuples are used to store multiple items in a single variable.
    Tuple is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Set, and Dictionary, all with different qualities and usage.
    A tuple is a collection which is ordered and unchangeable.
    Tuples are written with round brackets.
    Tuple Items - Tuple items are ordered, unchangeable, and allow duplicate values.
    Tuple items are indexed, the first item has index [0], the second item has index [1] etc.
    When we say that tuples are ordered, it means that the items have a defined order, and that order will not change.
    Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created.
    """
    print(f'__doc__: {test_create_tuple.__doc__}')
    #Create a Tuple
    _tuple = ("apple", "banana", "cherry")
    print(f'_tuple: {_tuple}')



def test_python_collections():
    """
    Python Collections (Arrays)
    There are four collection data types in the Python programming language:
    List is a collection which is ordered and changeable. Allows duplicate members.
    Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
    Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
    Dictionary is a collection which is ordered** and changeable. No duplicate members.
    *Set items are unchangeable, but you can remove and/or add items whenever you like.
    **As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.
    When choosing a collection type, it is useful to understand the properties of that type.
    Choosing the right type for a particular data set could mean retention of meaning, and, it could mean an increase in efficiency or security.
    """
    print(f'__doc__: {test_python_collections.__doc__}')

def test_accessing_elements_positive_index():
    """
    Tuple Items - Tuple items are ordered, unchangeable, and allow duplicate values.
    Tuple items are indexed, the first item has index [0], the second item has index [1] etc.
    """
    print(f'__doc__: {test_accessing_elements_positive_index.__doc__}')
    #Create a Tuple
    _tuple = ("apple", "banana", "cherry")
    print(f"_tuple: {_tuple}")
    print(f"Accessing element using positive index from _tuple")
    print(f"Accessing tuple element 0: {_tuple[0]}")
    print(f"Accessing tuple element 1: {_tuple[1]}")
    print(f"Accessing tuple element 2: {_tuple[2]}")

def test_accessing_elements_negative_index():
    """
    Tuple Items - Tuple items are ordered, unchangeable, and allow duplicate values.
    Tuple items are indexed, the first item has index [-1], the second item has index [-2] etc.
    Negative indexing means start from the end.
    -1 refers to the last item, -2 refers to the second last item etc.
    """
    print(f'__doc__: {test_accessing_elements_negative_index.__doc__}')
    #Create a Tuple
    _tuple = ("apple", "banana", "cherry")
    print(f"_tuple: {_tuple}")
    print(f"Accessing element using negative index from _tuple")
    print(f"Accessing tuple element 0: {_tuple[-1]}")
    print(f"Accessing tuple element 1: {_tuple[-2]}")
    print(f"Accessing tuple element 2: {_tuple[-3]}")


def test_accessing_elements_range_of_index():
    """
    Tuple Items - Tuple items are ordered, unchangeable, and allow duplicate values.
    Tuple items are indexed, the first item has index [0],[1],[-1], the second item has index [-2] etc.
    You can specify a range of indexes by specifying where to start and where to end the range.
    When specifying a range, the return value will be a new tuple with the specified items.
    Note: The search will start at index 2 (included) and end at index 5 (not included).
    Remember that the first item has index 0.
    """
    print(f'__doc__: {test_accessing_elements_range_of_index.__doc__}')
    #Create a Tuple
    this_tuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
    print(f"this_tuple: {this_tuple}")
    print(f"Accessing tuple element 0: {this_tuple[2:5]}")
    print(f"The below example returns the items from the beginning to, but NOT included, kiwi:")
    print(f"Positive Index: {this_tuple[:4]}")
    print(f"Negative Index: {this_tuple[:-4]}")



def test_tuple_duplicates():
    """
    Allow Duplicates - Since tuples are indexed, they can have items with the same value:
    """
    print(f'__doc__: {test_tuple_duplicates.__doc__}')
    tuple_ = ("apple", "banana", "cherry", "apple", "cherry")
    print(f"tuple_ contains duplicate values: {tuple_}")



def test_tuple_length():
    """
    Tuple length - To determine how many items a tuple has, use the len() function
    """
    print(f'__doc__: {test_tuple_length.__doc__}')
    this_tuple = ("apple", "banana", "cherry")
    print(f"tuple_ length: {this_tuple}, len: {len(this_tuple)}")


def test_tuple_create_with_one_item():
    """
    To create a tuple with only one item, you have to add a comma after the item, otherwise Python will not recognize it as a tuple.
    # NOT a tuple
    #this_tuple = ("apple")
    #print(type(this_tuple))
    """
    print(f'__doc__: {test_tuple_create_with_one_item.__doc__}')
    
    this_tuple = ("apple",)
    print(f"tuple_ create a tuple with only one item: {this_tuple}, type: {type(this_tuple)}")

def test_tuple_items_data_types():
    """
    Tuple items can be of any data type:String, int and boolean data types
    A tuple can contain different data types:
    A tuple with strings, integers and boolean values:
    """
    print(f'__doc__: {test_tuple_items_data_types.__doc__}')

    tuple1 = ("apple", "banana", "cherry")
    tuple2 = (1, 5, 7, 9, 3)
    tuple3 = (True, False, False)
    tuple4 = ("abc", 34, True, 40, "male")
    print(f"tuple1: {tuple1}")
    print(f"tuple2 : {tuple2 }")
    print(f"tuple3: {tuple3}")
    print(f"tuple4: {tuple4}")
    print(f"Tuple with different data types: {tuple1}, {tuple2}, {tuple3}, {tuple4}")
    


def test_tuple_items_types():
    """
    Tuple items can be of any data type:String, int and boolean data types
    A tuple can contain different data types:
    A tuple with strings, integers and boolean values:
    """
    print(f'__doc__: {test_tuple_items_types.__doc__}')
    tuple1 = ("apple", "banana", "cherry")
    tuple2 = (1, 5, 7, 9, 3)
    tuple3 = (True, False, False)
    tuple4 = ("abc", 34, True, 40, "male")
    print(f"tuple1: {tuple1}")
    print(f"tuple2 : {tuple2 }")
    print(f"tuple3: {tuple3}")
    print(f"tuple4: {tuple4}")
    print(f"Tuple with different data types: {tuple1}, {tuple2}, {tuple3}, {tuple4}")
    print(f"data types tuple1 {type(tuple1[0])}, {type(tuple1[1])}, {type(tuple1[2])}")
    print(f"data types tuple2: {type(tuple2[0])}, {type(tuple2[1])}, {type(tuple2[2])}, {type(tuple2[3])}, {type(tuple2[4])}")
    print(f"data types tuple3 {type(tuple3[0])}, {type(tuple3[1])}, {type(tuple3[2])}")
    print(f"data types tuple4: {type(tuple4[0])}, {type(tuple4[1])}, {type(tuple4[2])}, {type(tuple4[3])},{type(tuple4[4])}")
    

def test_tuple_constructor():
    """
    The tuple() Constructor
    It is also possible to use the tuple() constructor to make a tuple.
    Using the tuple() method to make a tuple:
    """
    print(f'__doc__: {test_tuple_constructor.__doc__}')
    this_tuple = tuple(("apple", "banana", "cherry"))  # note the double round-brackets
    print(f"this_tuple using constructor method: {this_tuple}")




def test_tuple_update():
    """
    Python - Update tuples
    Tuple are unchangeable, meaning that you cannot change, add, or remove items once the tuple is created.
    But there are some workarounds.
    Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.
    But there is a workaround. You can convert the tuple into a list, change the list, and convert the list back into a tuple.
    Convert the tuple into a list to be able to change it:
    """
    print(f'__doc__: {test_tuple_update.__doc__}')
    x = ("apple", "banana", "cherry")
    print(f"Tuple x: {x}")
    y = list(x)
    print(f"converting x tuple to a list y: {y}")
    y[1] = "kiwi"
    x = tuple(y)
    print(f"converting x list to a tuple y: {x}")


def test_tuple_update_list_tuple_conversion():
    """
    Python - Update tuples
    Tuple are unchangeable, meaning that you cannot change, add, or remove items once the tuple is created.
    Since tuples are immutable, they do not have a built-in append() method, but there are other ways to add items to a tuple.
    Convert into a list:
    1.Just like the workaround for changing a tuple, you can convert it into a list, add your item(s), and convert it back into a tuple.
    2.Convert the tuple into a list, add "orange", and convert it back into a tuple:
    Add tuple to a tuple. You are allowed to add tuples to tuples, so if you want to add one item, (or many), create a new tuple with the item(s), and add it to the existing tuple:
    """
    print(f'__doc__: {test_tuple_update_list_tuple_conversion.__doc__}')
    this_tuple = ("apple", "banana", "cherry")
    print(f"this_tuple : {this_tuple}")
    y = list(this_tuple)
    print(f"list before append: {y}")
    y.append("orange")
    print(f"list after append: {y}")
    this_tuple = tuple(y)
    print(f"After list to tuple conversion: {this_tuple}")


def test_update_tuple_to_tuple():
    """
    Convert into a list:
    1.Just like the workaround for changing a tuple, you can convert it into a list, add your item(s), and convert it back into a tuple.
    2.Convert the tuple into a list, add "orange", and convert it back into a tuple:
    3. Add tuple to a tuple. You are allowed to add tuples to tuples, so if you want to add one item, (or many), create a new tuple with the item(s), and add it to the existing tuple:
    """
    print(f'__doc__: {test_update_tuple_to_tuple.__doc__}')
    this_tuple = ("apple", "banana", "cherry")
    print(f"this_tuple : {this_tuple}")
    y = list(this_tuple)
    print(f"converting this_tuple tuple to a list y: {y}")
    print(f"list before append: {y}")
    y.append("orange")
    print(f"list after append: {y}")
    y = ("Watermelon",)
    print(f"y : {y}")
    this_tuple += y
    print(f"Add tuple of tuple:  {this_tuple}")


def test_unpack_tuple():
    """
    Unpacking a Tuple
    When we create a tuple, we normally assign values to it. This is called "packing" a tuple:
    Packing a tuple:
    In Python, we are also allowed to extract the values back into variables. This is called "unpacking" a tuple:
    Note: The number of variables must match the number of values in the tuple, if not, you must use an asterisk to collect the remaining values as a list.
    """
    print(f'__doc__: {test_unpack_tuple.__doc__}')
    #Packing a tuple:

    fruits = ("apple", "banana", "cherry")
    print(f"fruits:  {fruits}")
    (green, yellow, red) = fruits
    
    print(f"Unpacking tuple:  {green}, {yellow}, {red}")


def test_unpack_tuple_asterisk():
    """
    Unpacking a Tuple
    When we create a tuple, we normally assign values to it. This is called "packing" a tuple:
    Packing a tuple:
    In Python, we are also allowed to extract the values back into variables. This is called "unpacking" a tuple:
    Note: The number of variables must match the number of values in the tuple, if not, you must use an asterisk to collect the remaining values as a list.
    If the number of variables is less than the number of values, you can add an * to the variable name and the values will be assigned to the variable as a list:
    If the asterisk is added to another variable name than the last, Python will assign values to the variable until the number of values left matches the number of variables left.
    """
    print(f'__doc__: {test_unpack_tuple_asterisk.__doc__}')
    #Packing a tuple:
    fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
    print(f"fruits:  {fruits}")

    (green, yellow, *red) = fruits
    print(f"Unpacking tuple:  {green}, {yellow}")
    print(f"*Asterisk of red:  {red}")

    fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
    print("fruits", fruits)
    
    (green, *tropic, red) = fruits
    print(f"Unpacking tuple:  {green}, {red}")
    print(f"*Asterisk of red:  {tropic}")


def test_join_tuples():
    """
    Join Two Tuples
    To join two or more tuples you can use the + operator:
    """
    print(f'__doc__: {test_join_tuples.__doc__}')
    tuple1 = ("a", "b", "c")
    tuple2 = (1, 2, 3)
    print(f"tuple1:  {tuple1}")
    print(f"tuple2: {tuple2}")
    tuple3 = tuple1 + tuple2
    print("tuple3 = Concatenation of tuple and tuple 2: {tuple3}")


def test_multiply_tuples():
    """
    If you want to multiply the content of a tuple a given number of times, you can use the * operator:
    """
    print(f'__doc__: {test_multiply_tuples.__doc__}')
    tuple1 = ("a", "b", "c")
    tuple2 = (1, 2, 3)
    print(f"tuple1: {tuple1}")
    print(f"tuple2: {tuple2}")
    tuple3 = tuple1 * 2
    tuple4 = tuple2 * 2
    print(f"tuple3 = Multiplication of tuple 1: {tuple3}")
    print(f"tuple4 = Multiplication of tuple 2: {tuple4}")
    fruits = ("apple", "banana", "cherry")
    print(f"fruits: {fruits}")
    my_tuple = fruits * 2
    print(f"my_tuple after multiplication of 2: {my_tuple}")

def test_tuples_count_method():
    """
    Python Tuple count() Method
    Definition and Usage
    The count() method returns the number of times a specified value appears in the tuple.
    Syntax: tuple.count(value)
    value - Required. The item to search for
    """
    print(f'__doc__: {test_tuples_count_method.__doc__}')
    this_tuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
    x = this_tuple.count(5)
    print(f"this_tuple: {this_tuple}")
    print(f"tuple count, this_tuple.count(5) assigned to x : {x}")

def test_tuples_index_method():
    """
    Python Tuple count() Method
    Definition and Usage
    Definition and Usage
    The index() method finds the first occurrence of the specified value.
    The index() method raises an exception if the value is not found.
    Search for the first occurrence of the value 8, and return its position:
    """
    print(f'__doc__: {test_tuples_index_method.__doc__}')
    this_tuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
    x = this_tuple.index(8)
    print(f"this_tuple: {this_tuple}")
    print(f"tuple count, this_tuple.index(8) assigned to x : {x}")


def test_for_loop_through_tuple():
    """
    You can loop through the tuple items by using a for loop.
    Iterate through the items and print the values:
    """
    print(f'__doc__: {test_for_loop_through_tuple.__doc__}')
    _this_tuple = ("apple", "banana", "cherry")
    for x in _this_tuple:
        print(f'Iterate through the items: {x}')


def test_tuple_for_loop_range_len():
    """
    Loop Through the Index Numbers
    You can also loop through the tuple items by referring to their index number.
    Use the range() and len() functions to create a suitable iterable.
    """
    print(f'__doc__: {test_tuple_for_loop_range_len.__doc__}')
    this_tuple = ("apple", "banana", "cherry")
    for i in range(len(this_tuple)):
        print(f"this_tuple: {this_tuple[i]}")


def test_tuple_while_loop_len():
    """
    Using a While Loop
    You can loop through the tuple items by using a while loop.
    Use the len() function to determine the length of the tuple, then start at 0 and loop your way through the tuple items by referring to their indexes.
    Remember to increase the index by 1 after each iteration.
    """
    print(f'__doc__: {test_tuple_while_loop_len.__doc__}')
    this_tuple = ("apple", "banana", "cherry")
    i = 0
    while i < len(this_tuple):
        print(f"this_tuple: {this_tuple[i]}")
        i = i + 1



if __name__ == '__main__':
    test_create_tuple()
    test_python_collections()
    test_accessing_elements_positive_index()
    test_accessing_elements_negative_index()
    test_accessing_elements_range_of_index()
    test_tuple_duplicates()
    test_tuple_length()
    test_tuple_create_with_one_item()
    test_tuple_items_data_types()
    test_tuple_items_types()
    test_tuple_constructor()
    test_tuple_update()
    test_tuple_update_list_tuple_conversion()
    test_update_tuple_to_tuple()
    test_unpack_tuple()
    test_unpack_tuple_asterisk()
    test_join_tuples()
    test_multiply_tuples()
    test_tuples_count_method()
    test_tuples_index_method()
    test_for_loop_through_tuple()
    test_tuple_for_loop_range_len()
    test_tuple_while_loop_len()
    unittest.main()

#--------------------------Program Output--------------------------------------------------
# PS C:\Users\Anamika\Python_codes\myenv\tests\Python_Basics> python .\test_tuple_functions.py
# __doc__: 
#     Tuple - Tuples are used to store multiple items in a single variable.
#     Tuple is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Set, and Dictionary, all with different qualities and usage.
#     A tuple is a collection which is ordered and unchangeable.
#     Tuples are written with round brackets.
#     Tuple Items - Tuple items are ordered, unchangeable, and allow duplicate values.
#     Tuple items are indexed, the first item has index [0], the second item has index [1] etc.
#     When we say that tuples are ordered, it means that the items have a defined order, and that order will not change.
#     Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created.

# _tuple: ('apple', 'banana', 'cherry')
# __doc__:
#     Python Collections (Arrays)
#     There are four collection data types in the Python programming language:
#     List is a collection which is ordered and changeable. Allows duplicate members.
#     Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
#     Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
#     Dictionary is a collection which is ordered** and changeable. No duplicate members.
#     *Set items are unchangeable, but you can remove and/or add items whenever you like.
#     **As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.
#     When choosing a collection type, it is useful to understand the properties of that type.
#     Choosing the right type for a particular data set could mean retention of meaning, and, it could mean an increase in efficiency or security.      

# __doc__:
#     Tuple Items - Tuple items are ordered, unchangeable, and allow duplicate values.
#     Tuple items are indexed, the first item has index [0], the second item has index [1] etc.

# _tuple: ('apple', 'banana', 'cherry')
# Accessing element using positive index from _tuple
# Accessing tuple element 0: apple
# Accessing tuple element 1: banana
# Accessing tuple element 2: cherry
# __doc__:
#     Tuple Items - Tuple items are ordered, unchangeable, and allow duplicate values.
#     Tuple items are indexed, the first item has index [-1], the second item has index [-2] etc.
#     Negative indexing means start from the end.
#     -1 refers to the last item, -2 refers to the second last item etc.

# _tuple: ('apple', 'banana', 'cherry')
# Accessing element using negative index from _tuple
# Accessing tuple element 0: cherry
# Accessing tuple element 1: banana
# Accessing tuple element 2: apple
# __doc__:
#     Tuple Items - Tuple items are ordered, unchangeable, and allow duplicate values.
#     Tuple items are indexed, the first item has index [0],[1],[-1], the second item has index [-2] etc.
#     You can specify a range of indexes by specifying where to start and where to end the range.
#     When specifying a range, the return value will be a new tuple with the specified items.
#     Note: The search will start at index 2 (included) and end at index 5 (not included).
#     Remember that the first item has index 0.

# this_tuple: ('apple', 'banana', 'cherry', 'orange', 'kiwi', 'melon', 'mango')
# Accessing tuple element 0: ('cherry', 'orange', 'kiwi')
# The below example returns the items from the beginning to, but NOT included, kiwi:
# Positive Index: ('apple', 'banana', 'cherry', 'orange')
# Negative Index: ('apple', 'banana', 'cherry')
# __doc__:
#     Allow Duplicates - Since tuples are indexed, they can have items with the same value:

# tuple_ contains duplicate values: ('apple', 'banana', 'cherry', 'apple', 'cherry')
# __doc__:
#     Tuple length - To determine how many items a tuple has, use the len() function

# tuple_ length: ('apple', 'banana', 'cherry'), len: 3
# __doc__:
#     To create a tuple with only one item, you have to add a comma after the item, otherwise Python will not recognize it as a tuple.
#     # NOT a tuple
#     #this_tuple = ("apple")
#     #print(type(this_tuple))

# tuple_ create a tuple with only one item: ('apple',), type: <class 'tuple'>
# __doc__:
#     Tuple items can be of any data type:String, int and boolean data types
#     A tuple can contain different data types:
#     A tuple with strings, integers and boolean values:

# tuple1: ('apple', 'banana', 'cherry')
# tuple2 : (1, 5, 7, 9, 3)
# tuple3: (True, False, False)
# tuple4: ('abc', 34, True, 40, 'male')
# Tuple with different data types: ('apple', 'banana', 'cherry'), (1, 5, 7, 9, 3), (True, False, False), ('abc', 34, True, 40, 'male')
# __doc__:
#     Tuple items can be of any data type:String, int and boolean data types
#     A tuple can contain different data types:
#     A tuple with strings, integers and boolean values:

# tuple1: ('apple', 'banana', 'cherry')
# tuple2 : (1, 5, 7, 9, 3)
# tuple3: (True, False, False)
# tuple4: ('abc', 34, True, 40, 'male')
# Tuple with different data types: ('apple', 'banana', 'cherry'), (1, 5, 7, 9, 3), (True, False, False), ('abc', 34, True, 40, 'male')
# data types tuple1 <class 'str'>, <class 'str'>, <class 'str'>
# data types tuple2: <class 'int'>, <class 'int'>, <class 'int'>, <class 'int'>, <class 'int'>
# data types tuple3 <class 'bool'>, <class 'bool'>, <class 'bool'>
# data types tuple4: <class 'str'>, <class 'int'>, <class 'bool'>, <class 'int'>,<class 'str'>
# __doc__:
#     The tuple() Constructor
#     It is also possible to use the tuple() constructor to make a tuple.
#     Using the tuple() method to make a tuple:

# this_tuple using constructor method: ('apple', 'banana', 'cherry')
# __doc__:
#     Python - Update tuples
#     Tuple are unchangeable, meaning that you cannot change, add, or remove items once the tuple is created.
#     But there are some workarounds.
#     Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.
#     But there is a workaround. You can convert the tuple into a list, change the list, and convert the list back into a tuple.
#     Convert the tuple into a list to be able to change it:

# Tuple x: ('apple', 'banana', 'cherry')
# converting x tuple to a list y: ['apple', 'banana', 'cherry']
# converting x list to a tuple y: ('apple', 'kiwi', 'cherry')
# __doc__:
#     Python - Update tuples
#     Tuple are unchangeable, meaning that you cannot change, add, or remove items once the tuple is created.
#     Since tuples are immutable, they do not have a built-in append() method, but there are other ways to add items to a tuple.
#     Convert into a list:
#     1.Just like the workaround for changing a tuple, you can convert it into a list, add your item(s), and convert it back into a tuple.
#     2.Convert the tuple into a list, add "orange", and convert it back into a tuple:
#     Add tuple to a tuple. You are allowed to add tuples to tuples, so if you want to add one item, (or many), create a new tuple with the item(s), and add it to the existing tuple:

# this_tuple : ('apple', 'banana', 'cherry')
# list before append: ['apple', 'banana', 'cherry']
# list after append: ['apple', 'banana', 'cherry', 'orange']
# After list to tuple conversion: ('apple', 'banana', 'cherry', 'orange')
# __doc__:
#     Convert into a list:
#     1.Just like the workaround for changing a tuple, you can convert it into a list, add your item(s), and convert it back into a tuple.
#     2.Convert the tuple into a list, add "orange", and convert it back into a tuple:
#     3. Add tuple to a tuple. You are allowed to add tuples to tuples, so if you want to add one item, (or many), create a new tuple with the item(s), and add it to the existing tuple:

# this_tuple : ('apple', 'banana', 'cherry')
# converting this_tuple tuple to a list y: ['apple', 'banana', 'cherry']
# list before append: ['apple', 'banana', 'cherry']
# list after append: ['apple', 'banana', 'cherry', 'orange']
# y : ('Watermelon',)
# Add tuple of tuple:  ('apple', 'banana', 'cherry', 'Watermelon')
# __doc__:
#     Unpacking a Tuple
#     When we create a tuple, we normally assign values to it. This is called "packing" a tuple:
#     Packing a tuple:
#     In Python, we are also allowed to extract the values back into variables. This is called "unpacking" a tuple:
#     Note: The number of variables must match the number of values in the tuple, if not, you must use an asterisk to collect the remaining values as a list.

# fruits:  ('apple', 'banana', 'cherry')
# Unpacking tuple:  apple, banana, cherry
# __doc__:
#     Unpacking a Tuple
#     When we create a tuple, we normally assign values to it. This is called "packing" a tuple:
#     Packing a tuple:
#     In Python, we are also allowed to extract the values back into variables. This is called "unpacking" a tuple:
#     Note: The number of variables must match the number of values in the tuple, if not, you must use an asterisk to collect the remaining values as a list.
#     If the number of variables is less than the number of values, you can add an * to the variable name and the values will be assigned to the variable as a list:
#     If the asterisk is added to another variable name than the last, Python will assign values to the variable until the number of values left matches the number of variables left.

# fruits:  ('apple', 'banana', 'cherry', 'strawberry', 'raspberry')
# Unpacking tuple:  apple, banana
# *Asterisk of red:  ['cherry', 'strawberry', 'raspberry']
# fruits ('apple', 'mango', 'papaya', 'pineapple', 'cherry')
# Unpacking tuple:  apple, cherry
# *Asterisk of red:  ['mango', 'papaya', 'pineapple']
# __doc__:
#     Join Two Tuples
#     To join two or more tuples you can use the + operator:

# tuple1:  ('a', 'b', 'c')
# tuple2: (1, 2, 3)
# tuple3 = Concatenation of tuple and tuple 2: {tuple3}
# __doc__:
#     If you want to multiply the content of a tuple a given number of times, you can use the * operator:

# tuple1: ('a', 'b', 'c')
# tuple2: (1, 2, 3)
# tuple3 = Multiplication of tuple 1: ('a', 'b', 'c', 'a', 'b', 'c')
# tuple4 = Multiplication of tuple 2: (1, 2, 3, 1, 2, 3)
# fruits: ('apple', 'banana', 'cherry')
# my_tuple after multiplication of 2: ('apple', 'banana', 'cherry', 'apple', 'banana', 'cherry')
# __doc__:
#     Python Tuple count() Method
#     Definition and Usage
#     The count() method returns the number of times a specified value appears in the tuple.
#     Syntax: tuple.count(value)
#     value - Required. The item to search for

# this_tuple: (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
# tuple count, this_tuple.count(5) assigned to x : 2
# __doc__:
#     Python Tuple count() Method
#     Definition and Usage
#     Definition and Usage
#     The index() method finds the first occurrence of the specified value.
#     The index() method raises an exception if the value is not found.
#     Search for the first occurrence of the value 8, and return its position:

# this_tuple: (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
# tuple count, this_tuple.index(8) assigned to x : 3
# __doc__:
#     You can loop through the tuple items by using a for loop.
#     Iterate through the items and print the values:

# Iterate through the items: apple
# Iterate through the items: banana
# Iterate through the items: cherry
# __doc__:
#     Loop Through the Index Numbers
#     You can also loop through the tuple items by referring to their index number.
#     Use the range() and len() functions to create a suitable iterable.

# this_tuple: apple
# this_tuple: banana
# this_tuple: cherry
# __doc__:
#     Using a While Loop
#     You can loop through the tuple items by using a while loop.
#     Use the len() function to determine the length of the tuple, then start at 0 and loop your way through the tuple items by referring to their indexes.
#     Remember to increase the index by 1 after each iteration.

# this_tuple: apple
# this_tuple: banana
# this_tuple: cherry

# ----------------------------------------------------------------------
# Ran 0 tests in 0.000s

# OK
# PS C:\Users\Anamika\Python_codes\myenv\tests\Python_Basics> 