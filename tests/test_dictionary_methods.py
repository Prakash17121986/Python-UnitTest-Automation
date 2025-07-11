import unittest

class test_dict_datatype(unittest.TestCase):   
  
    def test_dict_methods(self, dict1, thisdict={}):
        '''
        Dictionaries are used to store data values in key: value pairs
        A dictionary is a collection which is ordered, changeable and does not allow duplicates
        Dictionaries are written with curly braces, and have keys and values
        Index values are called keys
        Keys are unique within a dictionary while values may not be
        It is generally used when we have a huge amount of data. 
        Dictioanries are optimized for reteriving data
        We must know the key to reterive the value
        items have  a defined order and that order will not change
        dictionaries are changeable, meaning that we can change, add or remove items after the dictionary has been created.
        Dictioanries cannot have two items with the same key
        Duplicate values will overwrite exisiting values
        {} - dictionary literals
        dict() - constructor method or function to create a dict object 
        '''
        self.dict1 = {}
        print("Create empty dictionary", dict1)
        dict1['a']=1
        dict1['b']=2
        dict1['c']=3
        print("After update keys and values in dict1", dict1)
        print("Type",type(dict1))
        print("Keys", dict1.keys()) # The keys() method will return a list of all the keys in the dictionary. Get a list of keys
        print("values", dict1.values())
        print(list(dict1.keys())) # list of all keys from the dict1
        print(list(dict1.values())) # list of all values from the dict1
        print("items", dict1.items()) # The items() method will return each item in a dictionary, as tuples in a list
        dict1.update({'d':4}) # The update() method will update the dictionary with the items from the given argument. The argument must be a dictionary, or an iterable object with key : value pairs.
        dict1['c']=7
        print("Changing the value 7 to 'c' key", dict1) # changing value for the existing key
        print("after update new key and value", dict1) # update the items
        print("Get the value by using key 'a'", dict1['a']) # access the items
        print("Get the value by key using get() method", dict1.get("a")) # access the items using get method
        print("len of dict1", len(dict1)) # how many items a dictionary has, use the len() function:
        dict1["colors"] = ["red","white","blue"] # add new items
        dict1["brand"] = "Maruti" # add new items
        dict1["Year"] = 2025 # add new items
        dict1["Model"] = "Swift" # add new items
        print("After update keys and values in dict1", dict1) # values in dictioanry items can be of any data type, str, list, tuple, boolean, int 
        if "Model" in dict1:
            print("Yes, 'Model' is one of the keys in the dict1 dictionary")
        print("after remove the item using pop() method", dict1.pop('Model')) # The pop() method removes the item with the specified key name
        print("After pop the item 'Model' in dict1", dict1) 
        print("After pop the item 'Model' in dict1", dict1.popitem()) # The popitem() method removes the last inserted item
        print("After popitem() in dict1", dict1) 
        del dict1['brand'] #The del keyword removes the item with the specified key name
        print("After remove the item 'brand' using del keyword in dict1:", dict1)
        # The clear() method empties the dictionary:
        # You can loop through a dictionary by using a for loop
        for x in dict1: # Print all key names in the dictionary, one by one
            print(x)
        
        for x in dict1: # Print all values by using key in the dictionary
            print(dict1[x])

        for x in dict1.values(): #You can also use the values() method to return values of a dictionary
            print(x)

        for x in dict1.keys(): #You can also use the keys() method to return keys of a dictionary
            print(x)

        for x, y in dict1.items(): #You can also use the item() method to return keys and values of a dictionary
            print(x, y)

        #display a dictionary in sorted order on keys
        for x in sorted(dict1):
            print(x, dict1[x])

        print("clear the dictionary", dict1.clear())
        print("dict1", dict1)


# if __name__ == '__main__':
#     obj = test_dict_datatype()
#     obj.test_dict_methods({'a':1,'b':2,'c':3,'d':4,'a':1}, thisdict={})
#     unittest.main()
  
    # -----------------------Program Output-----------------------------------------------
    # PS C:\Users\Anamika\Python_codes> & C:/Users/Anamika/AppData/Local/Programs/Python/Python310/python.exe c:/Users/Anamika/Python_codes/Project/tests/all_tests/DSA/test_dictionary_methods.py
    # Create empty dictionary {'a': 1, 'b': 2, 'c': 3, 'd': 4}
    # After update keys and values in dict1 {'a': 1, 'b': 2, 'c': 3, 'd': 4}
    # Type <class 'dict'>
    # Keys dict_keys(['a', 'b', 'c', 'd'])
    # values dict_values([1, 2, 3, 4])
    # ['a', 'b', 'c', 'd']
    # [1, 2, 3, 4]
    # items dict_items([('a', 1), ('b', 2), ('c', 3), ('d', 4)])
    # Changing the value 7 to 'c' key {'a': 1, 'b': 2, 'c': 7, 'd': 4}
    # after update new key and value {'a': 1, 'b': 2, 'c': 7, 'd': 4}
    # Get the value by using key 'a' 1
    # Get the value by key using get() method 1
    # len of dict1 4
    # After update keys and values in dict1 {'a': 1, 'b': 2, 'c': 7, 'd': 4, 'colors': ['red', 'white', 'blue'], 'brand': 'Maruti', 'Year': 2025, 'Model': 'Swift'}
    # Yes, 'Model' is one of the keys in the dict1 dictionary
    # after remove the item using pop() method Swift
    # After pop the item 'Model' in dict1 {'a': 1, 'b': 2, 'c': 7, 'd': 4, 'colors': ['red', 'white', 'blue'], 'brand': 'Maruti', 'Year': 2025}
    # After pop the item 'Model' in dict1 ('Year', 2025)
    # After popitem() in dict1 {'a': 1, 'b': 2, 'c': 7, 'd': 4, 'colors': ['red', 'white', 'blue'], 'brand': 'Maruti'}
    # After remove the item 'brand' using del keyword in dict1: {'a': 1, 'b': 2, 'c': 7, 'd': 4, 'colors': ['red', 'white', 'blue']}        
    # a
    # b
    # c
    # d
    # colors
    # 1
    # 2
    # 7
    # 4
    # ['red', 'white', 'blue']
    # 1
    # 2
    # 7
    # 4
    # ['red', 'white', 'blue']
    # a
    # b
    # c
    # d
    # colors
    # a 1
    # b 2
    # c 7
    # d 4
    # colors ['red', 'white', 'blue']
    # a 1
    # b 2
    # c 7
    # colors ['red', 'white', 'blue']
    # d 4
    # clear the dictionary None
    # dict1 {}

    # ----------------------------------------------------------------------
    # Ran 0 tests in 0.000s

    # OK
    # PS C:\Users\Anamika\Python_codes> 