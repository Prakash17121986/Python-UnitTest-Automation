import unittest

class test_split_single_dict_to_multiple_dict(unittest.TestCase):

    def test_split_single_dict_to_multiple_dict(self, dict1, Chunklen):
            self.dict1 = {}
            self.Chunklen = 2 # dictlist[i:i + Chunklen] - split 1 keys, 1 values as 2 sets in one dictionary
            dict1 = {1:'a', 2:'b', 3:'c', 4:'d'}
            print(f'Given dictionary: {dict1}')
            dictlist = list(dict1.items())
            split_output = [dict(dictlist[i:i + Chunklen]) for i in range(0, len(dictlist), Chunklen)]
            print(f'split single dictionary to multiple dictionary using list comphrension method: {split_output}')


# if __name__ == '__main__':
#     obj = test_split_single_dict_to_multiple_dict()
#     obj.test_split_single_dict_to_multiple_dict({1:'a', 2:'b', 3:'c', 4:'d'}, 2)
#     unittest.main()

    # ------------------------Program Output----------------------------------------------
    # PS C:\Users\Anamika\Python_codes> & C:/Users/Anamika/AppData/Local/Programs/Python/Python310/python.exe c:/Users/Anamika/Python_codes/Project/tests/all_tests/DSA/test_split_single_dict_to_multiple_dict.py
    # Given dictionary: {1: 'a', 2: 'b', 3: 'c', 4: 'd'}
    # split single dictionary to multiple dictionary using list comphrension method: [{1: 'a', 2: 'b'}, {3: 'c', 4: 'd'}]

    # ----------------------------------------------------------------------
    # Ran 0 tests in 0.000s

    # OK
    # PS C:\Users\Anamika\Python_codes> 