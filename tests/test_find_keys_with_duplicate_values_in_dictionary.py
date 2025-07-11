import unittest

class test_keys_values_exchange_in_dictionary(unittest.TestCase):

    # Find keys with duplicate values in dictionary in Python
    def test_find_keys_with_duplicate_values_in_dictionary(self, dict1={}):
        self.dict1 = {}
        dict1 = {'Sun': 5, 'Mon': 3, 'Tue': 5, 'Wed': 3}
        print("Given dictionary", dict1)
        k_v_exchanged = {}
        for key, value in dict1.items():
            if key not in k_v_exchanged:
                k_v_exchanged[value] = key
            else:
                k_v_exchanged[value].append(key)

        print(f'After removing keys with duplicate values: {k_v_exchanged}')

# if __name__ == '__main__':
#     obj = test_keys_values_exchange_in_dictionary()
#     obj.test_find_keys_with_duplicate_values_in_dictionary({'Sun': 5, 'Mon': 3, 'Tue': 5, 'Wed': 3})
#     unittest.main()

    # -----------------------Program Output-----------------------------------------------
    # PS C:\Users\Anamika\Python_codes> & C:/Users/Anamika/AppData/Local/Programs/Python/Python310/python.exe c:/Users/Anamika/Python_codes/Project/tests/all_tests/DSA/test_find_keys_with_duplicate_values_in_dictionary.py
    # Given dictionary {'Sun': 5, 'Mon': 3, 'Tue': 5, 'Wed': 3}
    # After removing keys with duplicate values: {5: 'Tue', 3: 'Wed'}

    # ----------------------------------------------------------------------
    # Ran 0 tests in 0.000s

    # OK
    # PS C:\Users\Anamika\Python_codes>