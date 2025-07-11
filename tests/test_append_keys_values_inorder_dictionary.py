
import unittest

def test_append_keys_values_inorder_dictionary(dict1):
    dict1 = {1:'a', 2:'b', 3:'c', 4:'d'}
    print("dict1", dict1)
    myresult = list(dict1.keys()) + list(dict1.values())
    print("Append keys and values associated using dict method: ", myresult)
    #output - [1, 2, 3, 4, 'a', 'b', 'c', 'd']

# if __name__ == '__main__':
    # test_append_keys_values_inorder_dictionary({1:'a', 2:'b', 3:'c', 4:'d'})
    # unittest.main()

# PS C:\Users\Anamika\Python_codes> & C:/Users/Anamika/AppData/Local/Programs/Python/Python310/python.exe c:/Users/Anamika/Python_codes/Project/tests/all_tests/DSA/test_append_keys_values_inorder_dictionary.py
# dict1 {1: 'a', 2: 'b', 3: 'c', 4: 'd'}
# Append keys and values associated using dict method:  [1, 2, 3, 4, 'a', 'b', 'c', 'd']

# ----------------------------------------------------------------------
# Ran 0 tests in 0.000s

# OK
# PS C:\Users\Anamika\Python_codes>