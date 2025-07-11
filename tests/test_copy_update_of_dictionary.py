import unittest

class test_dict_copy_update(unittest.TestCase):   

    def test_copy_update_of_dictionary(self, dict1, dict2):
           
        self.dict_1 = {1: 'a', 2: 'b'}
        self.dict_2 = {2: 'c', 4: 'd'}
        print(f'Given dictionary dict1: {dict1}, dict2: {dict2} ')
        dict3 = self.dict_2.copy()
        print(f'copy of dictionary dict2: {dict3}')
        dict3.update(self.dict_1)
        print(f'copy and update of dictionary dict2 and dict1: {dict3}')

# if __name__ == '__main__':
    # obj = test_dict_copy_update()
    # obj.test_copy_update_of_dictionary({1: 'a', 2: 'b'},{2: 'c', 4: 'd'})
    # unittest.main()


    # --------------------------Program Output--------------------------------------------
    # PS C:\Users\Anamika\Python_codes> & C:/Users/Anamika/AppData/Local/Programs/Python/Python310/python.exe c:/Users/Anamika/Python_codes/Project/tests/all_tests/DSA/test_test_copy_update_of_dictionary.py
    # Given dictionary dict1: {1: 'a', 2: 'b'}, dict2: {2: 'c', 4: 'd'} 
    # copy of dictionary dict2: {2: 'c', 4: 'd'}
    # copy and update of dictionary dict2 and dict1: {2: 'b', 4: 'd', 1: 'a'}

    # ----------------------------------------------------------------------
    # Ran 0 tests in 0.000s

    # OK
    # PS C:\Users\Anamika\Python_codes> 