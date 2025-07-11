import unittest

class test_swap_keys_values(unittest.TestCase):

    def test_swap_keys_values_in_dictionary(self, dict1):
            # swapping keys and values in dictonary - values as key and key as value

            self.dict1 = {1:'One', 2:'Two', 3:'Three'}
            print("Given dictionary", dict1)
            swapped_dict = {value: key for key, value in dict1.items()}
            print("Swapped dictionary", swapped_dict)

# if __name__ == '__main__':
#     obj = test_swap_keys_values()
#     obj.test_swap_keys_values_in_dictionary({1:'One', 2:'Two', 3:'Three'})
#     unittest.main()

# PS C:\Users\Anamika\Python_codes> & C:/Users/Anamika/AppData/Local/Programs/Python/Python310/python.exe c:/Users/Anamika/Python_codes/Project/tests/all_tests/DSA/test_swap_keys_values.py
# Given dictionary {1: 'One', 2: 'Two', 3: 'Three'}
# Swapped dictionary {'One': 1, 'Two': 2, 'Three': 3}

# ----------------------------------------------------------------------
# Ran 0 tests in 0.000s

# OK
# PS C:\Users\Anamika\Python_codes> 