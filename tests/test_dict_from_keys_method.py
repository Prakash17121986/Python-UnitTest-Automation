import unittest

def test_dict_from_keys(b = 0, a = ('key1', 'key2', 'key3'), c= None):
    # The fromkeys() method returns a dictionary with the specified keys and the specified value.
    a = ('key1', 'key2', 'key3')
    b = 0
    thisdict = dict.fromkeys(a, b)
    print("thisdict", thisdict)
    c = thisdict.copy() # The copy() method returns a copy of the specified dictionary.
    print("copy of thisdict", c)
    c = thisdict.setdefault("color", "white") 
    # Get the value of the "color" item, if the "color" item does not exist, insert "color" with the value "white":
    # The setdefault() method returns the value of the item with the specified key.
    # If the key does not exist, insert the key, with the specified value, see example below
    print("After update dictionary", c)
    print(thisdict)

# if __name__ == '__main__':
#     test_dict_from_keys(b = 0, a = ('key1', 'key2', 'key3'), c= None)
#     unittest.main()

# PS C:\Users\Anamika\Python_codes> & C:/Users/Anamika/AppData/Local/Programs/Python/Python310/python.exe c:/Users/Anamika/Python_codes/Project/tests/all_tests/DSA/test_dict_from_keys_method.py
# thisdict {'key1': 0, 'key2': 0, 'key3': 0}
# copy of thisdict {'key1': 0, 'key2': 0, 'key3': 0}
# After update dictionary white
# {'key1': 0, 'key2': 0, 'key3': 0, 'color': 'white'}

# ----------------------------------------------------------------------
# Ran 0 tests in 0.000s

# OK
# PS C:\Users\Anamika\Python_codes> 