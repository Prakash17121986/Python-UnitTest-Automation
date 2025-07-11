import unittest

class test_merge_dict_method(unittest.TestCase):   

    def test_merge_two_dictionary(self, dict1, dict2):
            self.dict1 = {}
            self.dict2 = {}
            dict1 = {1: 'a', 2: 'b'}
            dict2 = {2: 'c', 4: 'd'}
            print(f'Given dictionary dict1: {dict1}, dict2: {dict2} ')
            print(f'Merge dictionary of dict1 & dict2: {dict1 | dict2} ')
            print(f'Merge dictionary keys of dict1 & dict2: {*dict1, *dict2}')
        
# if __name__ == '__main__':
#     obj = test_merge_dict_method()
#     obj.test_merge_two_dictionary({1: 'a', 2: 'b'},{2: 'c', 4: 'd'})
#     unittest.main()
  
    # ----------------------Program Output------------------------------------------------
    # PS C:\Users\Anamika\Python_codes> & C:/Users/Anamika/AppData/Local/Programs/Python/Python310/python.exe c:/Users/Anamika/Python_codes/Project/tests/all_tests/DSA/test_merge_two_dictionary.py
    # Given dictionary dict1: {1: 'a', 2: 'b'}, dict2: {2: 'c', 4: 'd'} 
    # Merge dictionary of dict1 & dict2: {1: 'a', 2: 'c', 4: 'd'}
    # Merge dictionary keys of dict1 & dict2: (1, 2, 2, 4)

    # ----------------------------------------------------------------------
    # Ran 0 tests in 0.000s

    # OK
    # PS C:\Users\Anamika\Python_codes> 