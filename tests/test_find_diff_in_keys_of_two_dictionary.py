import unittest
from collections import ChainMap

class test_find_diff_in_keys_of_two_dict(unittest.TestCase):

    def test_find_difference_in_keys_of_two_dictionary(self, dict1, dict2):
            self.dict1 = {}
            self.dict2 = {}
            dict1 = {'1': 'Mon', '2': 'Tue', '3': 'Wed'}
            dict2 = {'3': 'Wed', '4': 'Thur', '5': 'Fri'}
            print(f"dict1: {dict1}")
            print(f"dict2: {dict2}")
            res1 = set(dict1) - set(dict2) # differnce of keys in dict1 & dict2
            res2 = set(dict2) - set(dict1) # differnce of keys in dict2 & dict1
            print("res1:", res1)
            print("res2:", res2)
            res2 = ChainMap(dict1, dict2)
            print("After merge two dictinaries dict1 using ChainMap func, dict2", res2)

# if __name__ == '__main__':
#     obj = test_find_diff_in_keys_of_two_dict()
#     obj.test_find_difference_in_keys_of_two_dictionary({'1': 'Mon', '2': 'Tue', '3': 'Wed'},{'3': 'Wed', '4': 'Thur', '5': 'Fri'})
#     unittest.main()
  

# -----------------------------Program Output-----------------------------------------
#  PS C:\Users\Anamika\Python_codes> & C:/Users/Anamika/AppData/Local/Programs/Python/Python310/python.exe c:/Users/Anamika/Python_codes/Project/tests/all_tests/DSA/test_find_diff_in_keys_of_two_dictionary.py
# dict1: {'1': 'Mon', '2': 'Tue', '3': 'Wed'}
# dict2: {'3': 'Wed', '4': 'Thur', '5': 'Fri'}
# res1: {'2', '1'}
# res2: {'4', '5'}
# After merge two dictinaries dict1 using ChainMap func, dict2 ChainMap({'1': 'Mon', '2': 'Tue', '3': 'Wed'}, {'3': 'Wed', '4': 'Thur', '5': 'Fri'})

# ----------------------------------------------------------------------
# Ran 0 tests in 0.000s

# OK
# PS C:\Users\Anamika\Python_codes> 