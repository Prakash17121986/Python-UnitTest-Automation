import unittest

def test_create_dictionary():
    """
    Dictionaries are used to store data values in key:value pairs.
    A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
    As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.
    Dictionaries are written with curly brackets, and have keys and values:
    Create and print a dictionary
    Dict items are ordered, changeable, and do not allow duplicates.
    Dictionary items are presented in key:value pairs, and can be referred to by using the key name.
    Ordered or Unordered?
    When we say that dictionaries ordered, it means that the items have a defined order, and that order will not change.
    Unordered means that the items do not have a defined order, you cannot refer to an item by using an index.
    Dictionaries are changeable, meaning that we can change, add or remove items after the dictionary has been created.
    Duplicates Not Allowed
    Dictionaries cannot have two items with the same key:
    
    Python Collections (Arrays)
    There are four collection data types in the Python programming language:
    List is a collection which is ordered and changeable. Allows duplicate members.
    Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
    Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
    Dictionary is a collection which is ordered** and changeable. No duplicate members.
    Set items are unchangeable, but you can remove and/or add items whenever you like.
    
    When choosing a collection type, it is useful to understand the properties of that type.
    Choosing the right type for a particular data set could mean retention of meaning, and, it could mean an increase in efficiency or security.
    # dict is Mutable, unordered, does not allow duplicates, empty dictionary = dict(),
    # set with single item 
    # item = {'a':1, 'b':2}
    # dictionary with single item - item['a'];
    # dictionary keys can be string, list or tuple
    # dictionary value can be any datatype
    # set can store any datatype except dictionary and List
    """
    #print(f'__doc___= {test_create_dictionary.__doc__}')
    this_dict = {
      "brand": "Ford",
      "model": "Mustang",
      "year": 1964
    }

    print(f'this_dict, {this_dict}')

    #Print the "brand" value of the dictionary:
    print(f'Print the "brand" value of the dictionary, {this_dict["brand"]}')

def test_length_dictionary():
    """
    To determine how many items a dictionary has, use the len() function
    Dictionary Items - Data Types
    The values in dictionary items can be of any data type:
    """
    #print(f'__doc___= {test_length_dictionary.__doc__}')
    len_dict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964 }
    #Print the number of items in the dictionary:
    print(f'len_dict, {len_dict}')
    print(f'length of len_dict, {len(len_dict)}')



def test_dictionary_with_different_datatypes():
    """
    type()
    From Python's perspective, dictionaries are defined as objects with the data type 'dict':
    <class 'dict'>
    """
    #print(f'__doc___= {test_dictionary_with_different_datatypes.__doc__}')
    datatypes_dict = {
      "brand": "Ford",
      "electric": False,
      "year": 1964,
      "colors": ["red", "white", "blue"]
    }
    # Example
    # Print the data type of dictionary:
    print(f'Dictinary: datatypes_dict, {datatypes_dict}')
    print(f'Type of datatypes_dict, {type(datatypes_dict)}')



def test_dictionary_constructor_method():
    """
    #The dict() Constructor
    #It is also possible to use the dict() constructor to make a dictionary.
    #Using the dict() method to make a dictionary:
    """
    #print(f'__doc___= {test_dictionary_constructor_method.__doc__}')
    constructor_dict = dict(name = "John", age = 36, country = "Norway")
    print(f'Using the dict() method to make a dictionary, {constructor_dict}')


def test_dictionary_accessing_elements():
    """
    Python - Access Dictionary Items
    Accessing Items - You can access the items of a dictionary by referring to its key name, inside square brackets:
    Get the value of the "model" key:
    """
    #print(f'__doc___= {test_dictionary_accessing_elements.__doc__}')
    element_dict = {
      "brand": "Ford",
      "model": "Mustang",
      "year": 1964
    }
    print(f'Access Dictionary Items: {element_dict}')
    val = element_dict["model"]
    print(f'Get the value of the "model" key: {val}')



def test_dictionary_get():
    """
    There is also a method called get() that will give you the same result:
    #Get the value of the "model" key:
    """
    #print(f'__doc___= {test_dictionary_get.__doc__}')

    elem_dict = {
      "brand": "Ford",
      "model": "Mustang",
      "year": 1964
    }
    print(f'elem_dict: {elem_dict}')
    x1 = elem_dict.get("model")
    print(f'Get the value of the "model" key: {x1}')

def test_dictionary_keys():
    """
    Get Keys
    The keys() method will return a list of all the keys in the dictionary.
    Get a list of the keys:
    The list of the keys is a view of the dictionary, meaning that any changes done to the dictionary will be reflected in the keys list.
    """
    #print(f'__doc___= {test_dictionary_keys.__doc__}')

    elem_dict = {
      "brand": "Ford",
      "model": "Mustang",
      "year": 1964
    }
    print(f'elem_dict: {elem_dict}')
    x2 = elem_dict.keys()
    print(f'Get a list of the keys: {x2}')


def test_dictionary_add_new_item():
    """
    Add a new item to the original dictionary, and see that the keys list gets updated as well:
    """
    #print(f'__doc___= {test_dictionary_add_new_item.__doc__}')
    new_item = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
    }
    print(f'new_item: {new_item}')
    x3 = new_item.keys()
    print(f'before the key change: {x3}') #before the change
    new_item["color"] = "white"
    print(f'After the key change: {x3}') #after the change

  
def test_dictionary_values():
    """
    The list of the values is a view of the dictionary, meaning that any changes done to the dictionary will be reflected in the values list.
    Make a change in the original dictionary, and see that the values list gets updated as well:
    #Definition and Usage
    #The values() method returns a view object. The view object contains the values of the dictionary, as a list.
    #The view object will reflect any changes done to the dictionary, see example below.
    #Syntax
    #dictionary.values()
    #When a values changed in the dictionary, the view object also gets updated:
    #Python Dictionary values() Method
    #Return the values:
    #The values() method will return a list of all the values in the dictionary.
    #Example
    #Get a list of the values:
    """
    #print(f'__doc___= {test_dictionary_values.__doc__}')
    new_item = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
    }
    print(f'new_item: {new_item}')
    x4 = new_item.values()
    print(f'Get a list of the values: {x4}') #before the change
    print(f'before the value change for year key: {x4}') #before the value change for 'year' key
    new_item["year"] = 2020
    print(f'After the value change for year key: {x4}') #after the value change for 'year' key

def test_dictionary_items():
    """
    Get Items
    The items() method will return each item in a dictionary, as tuples in a list.
    Get a list of the key:value pairs
    The returned list is a view of the items of the dictionary, meaning that any changes done to the dictionary will be reflected in the items list.
    Make a change in the original dictionary, and see that the items list gets updated as well:
    """
    #print(f'__doc___= {test_dictionary_items.__doc__}')
    car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
    }
    print(f'car: {car}')
    x5 = car.items()
    print(f'Get a list of the key:value pairs: {x5}') #before the change
    car["year"] = 2020
    print(f'Get a list of the key:value pairs after the value change for year key : {x5}') #after the change

    # Example
    # Add a new item to the original dictionary, and see that the items list gets updated as well:

    car = {
      "brand": "Ford",
      "model": "Mustang",
      "year": 1964
    }

    print(f'Get a list of the key:value pairs: {car.items()}') #before the change
    car["color"] = "red"
    print(f'Get a list of the key:value pairs after updating new key and value: {car}') #after the change


def test_dictionary_key_exists():
    """
    Check if Key Exists
    To determine if a specified key is present in a dictionary use the in keyword:
    Check if "model" is present in the dictionary:
    Python - Change Dictionary Items
    Change Values
    You can change the value of a specific item by referring to its key name:
    Change the "year" to 2018:
    """
    #print(f'__doc___= {test_dictionary_key_exists.__doc__}')
    this_dict = {
      "brand": "Ford",
      "model": "Mustang",
      "year": 1964
    }
    print(f'this_dict: {this_dict}')

    if "model" in this_dict:
        print(f"Yes, 'model' is one of the keys in the {this_dict} dictionary")
    else:
        print(f"No, 'model' key does not exist in the {this_dict} dictionary")


def test_dictionary_update():
    """
    Update Dictionary
    The update() method will update the dictionary with the items from the given argument.
    The argument must be a dictionary, or an iterable object with key:value pairs.
    Update the "year" of the car by using the update() method:
    Python - Add Dictionary Item
    Adding Items
    Adding an item to the dictionary is done by using a new index key and assigning a value to it:
    #Update Dictionary
    #The update() method will update the dictionary with the items from a given argument.
    If the item does not exist, the item will be added.
    The argument must be a dictionary, or an iterable object with key:value pairs.
    Add a color item to the dictionary by using the update() method:
    Definition and Usage
    The update() method inserts the specified items to the dictionary.
    The specified items can be a dictionary, or an iterable object with key value pairs.
    iterable	A dictionary or an iterable object with key value pairs, that will be inserted to the dictionary
    """
    #print(f'__doc___= {test_dictionary_update.__doc__}')
    dict_val = {
      "brand": "Ford",
      "model": "Mustang",
      "year": 1964
    }

    print(f'dict_val: {dict_val}')
    print(f'Get a list of the key:value pairs: {dict_val}') #before the change
    dict_val.update({"year": 2020})
    print(dict_val)
    print(f'Get a list of the key:value pairs after value change for year key : {dict_val}') #after the change

    dict_val["color"] = "red"
    print(dict_val)
    print(f'Get a list of the key:value pairs after updating new key and value : {dict_val}') #after the change
 



def test_dictionary_pop():
    """
    Python - Remove Dictionary Items
    Removing Items
    There are several methods to remove items from a dictionary:
    ExampleGet your own Python Server
    The pop() method removes the item with the specified key name:
    """
    #print(f'__doc___= {test_dictionary_pop.__doc__}')
    _dict = {
      "brand": "Ford",
      "model": "Mustang",
      "year": 1964
    }
    print(f'_dict_val: {_dict}')

    _dict.pop("model")
    print(f"After pop the 'model' key in _dict_val: {_dict}")

    #Example
    #The popitem() method removes the last inserted item (in versions before 3.7, a random item is removed instead):
    _dict.popitem()
    print(f"After pop item(last key and value will be out of _dict_val): {_dict}")



def test_dictionary_del():
    """
    The del keyword removes the item with the specified key name
    The del keyword can also delete the dictionary completely:
    """
    #print(f'__doc___= {test_dictionary_del.__doc__}')
    dict_ = {
      "brand": "Ford",
      "model": "Mustang",
      "year": 1964
    }
    print(f'dict_: {dict_}')

    del dict_["model"]
    print(f"After delete 'Model' key in dict_): {dict_}")



def test_dictionary_clear():
    """
    The clear() method empties the dictionary:
    """
    #print(f'__doc___= {test_dictionary_clear.__doc__}')
    _dict = {
      "brand": "Ford",
      "model": "Mustang",
      "year": 1964
    }
    print(f'_dict: {_dict}')

    _dict.clear()
    print(f"After clear the dictionary _dict): {_dict}")



def test_dictionary_forloop():
    """
    #Python - Loop Dictionaries
    #Loop Through a Dictionary
    #You can loop through a dictionary by using a for loop.
    #When looping through a dictionary, the return value are the keys of the dictionary, but there are methods to return the values as well.
    #ExampleGet your own Python Server
    #Print all key names in the dictionary, one by one:
    """
    #print(f'__doc___= {test_dictionary_forloop.__doc__}')
    _dict = {
      "brand": "Ford",
      "model": "Mustang",
      "year": 1964
    }
    print(f'_dict: {_dict}')

    #Example
    #Loop through both keys and values, by using the items() method:
    for key, value in _dict.items():
        print(f"Loop through both keys and values: {key} value: {value}")

    #Example
    #You can also use the values() method to return values of a dictionary:
    #Print all values in the dictionary, one byone:
    for value in _dict.values():
      print(f"Iterate value one by one: {value}")

    #Example
    #You can use the keys() method to return the keys of a dictionary:
    for key in _dict.keys():
      print(f"Iterate key one by one: {key}")

  
def test_dictionary_copy():
    """
    #Python - Copy Dictionaries
    Copy a Dictionary
    You cannot copy a dictionary simply by typing dict2 = dict1, because: dict2 will only be a reference to dict1, and changes made in dict1 will automatically also be made in dict2.
    There are ways to make a copy, one way is to use the built-in Dictionary method copy().
    ExampleGet your own Python Server
    Make a copy of a dictionary with the copy() method:
    """
    #print(f'__doc___= {test_dictionary_copy.__doc__}')
    _dict = {
      "brand": "Ford",
      "model": "Mustang",
      "year": 1964
    }

    print(f'_dict: {_dict}')

    mydict = _dict.copy()
    print(f'After copy of mydict: {mydict}')

    #Example
    #Make a copy of a dictionary with the dict() function:

    dict1 = {
      "brand": "Ford",
      "model": "Mustang",
      "year": 1964
    }
    print(f'dict1: {dict1}')
    mydict = dict(dict1)
    print(f'After copy of mydict: {mydict}')



def test_nested_dictionary():
    """
    #Python - Nested Dictionaries
    #A dictionary can contain dictionaries, this is called nested dictionaries.
    #Create a dictionary that contain three dictionaries:
    """
    #print(f'__doc___= {test_nested_dictionary.__doc__}')
    my_family = {
      "child1" : {
        "name" : "Emil",
        "year" : 2004
      },
      "child2" : {
        "name" : "Tobias",
        "year" : 2007
      },
      "child3" : {
        "name" : "Linus",
        "year" : 2011
      }
    }

    print(f'Nested dictionary - A dictionary can contain dictionaries, this is called nested dictionaries: {my_family}')

    print("Create three dictionaries, then create one dictionary that will contain the other three dictionaries")

    child1 = {
      "name" : "Emil",
      "year" : 2004
    }
    child2 = {
      "name" : "Tobias",
      "year" : 2007
    }
    child3 = {
      "name" : "Linus",
      "year" : 2011
    }

    my_family = {
      "child1" : child1,
      "child2" : child2,
      "child3" : child3
    }

    print(f'my_family dictionary: {my_family}')
    print(f'child1 dictionary: {child1}')
    print(f'child2 dictionary: {child2}')
    print(f'child3 dictionary: {child3}')

    print(f'Get value of my_family["child1"]["name"] from nested dictionary {my_family["child1"]["name"]}')
    print(f'Get value of ["child1"]["year"] from nested dictionary {my_family["child1"]["year"]}')

    print(f'Get value of ["child2"]["name"] from nested dictionary {my_family["child2"]["name"]}')
    print(f'Get value of ["child2"]["year"] from nested dictionary {my_family["child2"]["name"]}')

    print(f'Get value of ["child3"]["name"] from nested dictionary {my_family["child3"]["name"]}')
    print(f'Get value of ["child3"]["year"] from nested dictionary {my_family["child3"]["name"]}')

    for key in my_family:
      print(key)
      if "child1" in key: # if key matches, print key, value 
          print(f'Accessing element my_family["child1"]["name"] from nested dictionary, {my_family[key]}')
      elif "child2" in key:
          print(f'Accessing element my_family["child2"]["name"] from nested dictionary, {my_family[key]}')
      elif "child3" in key:
          print(f'Accessing element my_family["child3"]["name"] from nested dictionary, {my_family[key]}')


def test_nested_dictionary_forloop():
    """
    Loop Through Nested Dictionaries
    You can loop through a dictionary by using the items() method like this:
    Loop through the keys and values of all nested dictionaries
    """
    #print(f'__doc___= {test_nested_dictionary_forloop.__doc__}')
    my_family = {
      "child1": {
        "name": "Emil",
        "year": 2004
      },
      "child2": {
        "name": "Tobias",
        "year": 2007
      },
      "child3": {
        "name": "Linus",
        "year": 2011
      }
    }

    for key, value in my_family.items():
      print(f'Iterate key: {key}, value: {value}')


def test_dictionary_fromkeys():
    """
    # Python Dictionary fromkeys() Method
    # Create a dictionary with 3 keys, all with the value 0:
    # Definition and Usage
    # The fromkeys() method returns a dictionary with the specified keys and the specified value.
    # Syntax
    # dict.fromkeys(keys, value)
    # Parameter Values
    # Parameter	Description
    # keys	Required. An iterable specifying the keys of the new dictionary
    # value	Optional. The value for all keys. Default value is None
    # Same example as above, but without specifying the value:
    """
    #print(f'__doc___= {test_dictionary_fromkeys.__doc__}')
    x1 = ('key1', 'key2', 'key3')
    y1 = 0
    print(f'x1: {x1}')
    print(f'y1: {y1}')
    this_dict = dict.fromkeys(x1, y1)
    print(f'dict.fromkeys method used to update keys x1, values y1 in this_dict dictionary : {this_dict}')

    x2 = ('key1', 'key2', 'key3')
    print(f'x2: {x2}')
    this_dict = dict.fromkeys(x2)
    print(f'dict.fromkeys method used to update keys in this_dict dictionary : {this_dict}')



def test_dictionary_popitem():
    """
    Definition and Usage
    The popitem() method removes the item that was last inserted into the dictionary.
    In versions before 3.7, the popitem() method removes a random item.
    The removed item is the return value of the popitem() method, as a tuple
    """
    #print(f'__doc___= {test_dictionary_popitem.__doc__}')
    car = {
      "brand": "Ford",
      "model": "Mustang",
      "year": 1964
    }
    print(f'car: {car}')
    car.popitem()
    print(f'After popitem of car dictionary: {car}')



if __name__ == '__main__':
    test_create_dictionary()
    test_length_dictionary()
    test_dictionary_with_different_datatypes()
    test_dictionary_constructor_method()
    test_dictionary_accessing_elements()
    test_dictionary_get()
    test_dictionary_keys()
    test_dictionary_add_new_item()
    test_dictionary_values()
    test_dictionary_items()
    test_dictionary_key_exists()
    test_dictionary_update()
    test_dictionary_pop()
    test_dictionary_del()
    test_dictionary_clear()
    test_dictionary_forloop()
    test_dictionary_copy()
    test_nested_dictionary()
    test_nested_dictionary_forloop()
    test_dictionary_fromkeys()
    test_dictionary_popitem()
    unittest.main()