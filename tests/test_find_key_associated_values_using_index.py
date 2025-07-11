import unittest

def test_key_associated_values_using_index(dict1):
        # swapping keys and values in dictonary - values as key and key as value

        dict1 = {'One': 100, 'Two': 200, 'Three': 300}
        dict_keys = list(dict1.keys())
        dict_values = list(dict1.values())

        dict_position = dict_values.index(100)
        print("The values at position 100 is", dict_keys[dict_position])

        dict_position = dict_values.index(200)
        print("The values at position 200 is", dict_keys[dict_position])

        dict_position = dict_values.index(300)
        print("The values at position 300 is", dict_keys[dict_position])

# if __name__ == '__main__':
#     test_key_associated_values_using_index({'One': 100, 'Two': 200, 'Three': 300})
#     unittest.main()

        # -----------------------Program Output-----------------------------------------------
        # PS C:\Users\Anamika\Python_codes> & C:/Users/Anamika/AppData/Local/Programs/Python/Python310/python.exe c:/Users/Anamika/Python_codes/Project/tests/all_tests/DSA/test_key_associated_values_using_index.py
        # The values at position 100 is One
        # The values at position 200 is Two
        # The values at position 300 is Three

        # ----------------------------------------------------------------------
        # Ran 0 tests in 0.000s

        # OK
        # PS C:\Users\Anamika\Python_codes> 