import unittest

class test_find_common_keys_in_list_dict(unittest.TestCase):

    # How to get common keys in list and dictonary 
    def test_find_common_keys_listdict(self, dict1, myresult):
        self.dict1 = {}
        dict1 = {1:'a', 2:'b', 3:'c', 4:'d'}
        print("dict1:", dict1)
        self.myresult = [1,2,3]
        print("list", myresult)
        print("Common keys in list and dictonary", [e for e in dict1 if e in myresult])
        
# if __name__ == '__main__':
#     obj = test_find_common_keys_in_list_dict()
#     obj.test_find_common_keys_listdict({1:'a', 2:'b', 3:'c', 4:'d'},[1,2,3])
#     unittest.main()

    # --------------------Program Output--------------------------------------------------
    # PS C:\Users\Anamika\Python_codes> & C:/Users/Anamika/AppData/Local/Programs/Python/Python310/python.exe c:/Users/Anamika/Python_codes/Project/tests/all_tests/DSA/test_find_common_keys_in_list_and_dict.py
    # dict1: {1: 'a', 2: 'b', 3: 'c', 4: 'd'}
    # list [1, 2, 3]
    # Common keys in list and dictonary [1, 2, 3]

    # ----------------------------------------------------------------------
    # Ran 0 tests in 0.000s

    # OK
    # PS C:\Users\Anamika\Python_codes> 