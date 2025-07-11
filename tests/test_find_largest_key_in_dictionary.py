import unittest

class test_largest_key_in_dictionary(unittest.TestCase):

    def test_largest_key_in_dictionary(self, num, dict1, maxlist, Nlist):
        # to extract N largest dictionaries keys (N=4) - 4 max keys
        self.dict1 = {}
        self.maxlist = []
        self.Nlist = []
        self.num = num = 4
        dict1 = {12: 10, 22: 12, 18 : 4, 8: 20, 14: 9, 9: 13}
        print(f'Given dictionary: {dict1}')
        for key in dict1:
            maxlist.append(key) # to find all the keys in maxlist
        for x in range(num):
            maxval = max(maxlist) # to find the first 4 max value from the maxlist
            Nlist.append(maxval) # append the first 4 max values
            maxlist.remove(maxval) # it remove the other values
        print("First 4 largest keys using for loop method", Nlist)

        newlist= []
        for keys, values in sorted(dict1.items(), key=lambda item: item[0], reverse=True)[:num]:
            newlist.append(keys)
        print("Lambda method: The 4 largest keys are: ", newlist)

# if __name__ == '__main__':
#     obj = test_largest_key_in_dictionary()
#     obj.test_largest_key_in_dictionary(4, {12: 10, 22: 12, 18 : 4, 8: 20, 14: 9, 9: 13}, [], [])
#     unittest.main()
  
    # ------------------------Program Output----------------------------------------------
    # PS C:\Users\Anamika\Python_codes> & C:/Users/Anamika/AppData/Local/Programs/Python/Python310/python.exe c:/Users/Anamika/Python_codes/Project/tests/all_tests/DSA/test_largest_key_in_dictionary.py
    # Given dictionary: {12: 10, 22: 12, 18: 4, 8: 20, 14: 9, 9: 13}
    # First 4 largest keys using for loop method [22, 18, 14, 12]
    # Lambda method: The 4 largest keys are:  [22, 18, 14, 12]

    # ----------------------------------------------------------------------
    # Ran 0 tests in 0.000s

    # OK
    # PS C:\Users\Anamika\Python_codes> 