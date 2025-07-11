import unittest

class test_find_common_keys_of_two_dictionary():   

    def test_find_common_keys_of_two_dictionary_set(self, dict1, dict2):
        self.dict1 = {}
        self.dict2 = {}
        dict_1 = {2: 'a', 2: 'b', 3: 'c'}
        dict_2 = {2: 'c', 4: 'd', 3: 'c'}
        print(f'dict1: {dict1}')
        print(f'dict2: {dict2}')
        dict_3 = dict_1.keys() & dict_2.keys()
        print(f'find_common_keys_of_dict1 & dict2 dictionary: {dict_3}')

    def test_find_common_keys_of_two_dictionary_set_items(self, dict1, dict2):
        self.dict1 = {}
        self.dict2 = {}
        dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
        dict2 = {'t1': 1, 'b': 2, 'e': 5, 'c': 3}
        print(f'dict1: {dict1}')
        print(f'dict2: {dict2}')
        for key, value in set(dict1.items() & dict2.items()):
            print("%s, %s is present in both dict1 and dict2"%(key, value))

        dict1.clear()
        dict2.clear()
        print(f'after clear dict1: {dict1}, dict2: {dict2}')
    
    def test_find_common_keys_of_two_dictionary_list_comphrension(self, dict1, dict2):
        self.dict1 = {}
        self.dict2 = {}
        dict1 = {'ab': 11, 'bc': 21, 'cd': 13, 'de': 41}
        dict2 = {'cd': 33, 'ad': 14, 'de': 51, 'fa': 16}
        
        print("find_common_keys_of_dict1 & dict2 dictionary using list comphrehension method:")
        print(dict({key:dict1[key] for key in dict1 if key in dict2}))
       

# if __name__ == '__main__':
    # obj = test_find_common_keys_of_two_dictionary()
    # obj.test_find_common_keys_of_two_dictionary_set({2: 'a', 2: 'b', 3: 'c'},{2: 'c', 4: 'd', 3: 'c'})
    # obj.test_find_common_keys_of_two_dictionary_set_items({'a': 1, 'b': 2, 'c': 3, 'd': 4},{'t1': 1, 'b': 2, 'e': 5, 'c': 3})
    # obj.test_find_common_keys_of_two_dictionary_list_comphrension({'ab': 11, 'bc': 21, 'cd': 13, 'de': 41},{'cd': 33, 'ad': 14, 'de': 51, 'fa': 16})
    # unittest.main()
    
    # ------------------------Program Output----------------------------------------------
    # PS C:\Users\Anamika\Python_codes> & C:/Users/Anamika/AppData/Local/Programs/Python/Python310/python.exe c:/Users/Anamika/Python_codes/Project/tests/all_tests/DSA/test_find_common_keys_of_two_dictionary.py
    # dict1: {2: 'b', 3: 'c'}
    # dict2: {2: 'c', 4: 'd', 3: 'c'}
    # find_common_keys_of_dict1 & dict2 dictionary: {2, 3}
    # dict1: {'a': 1, 'b': 2, 'c': 3, 'd': 4}
    # dict2: {'t1': 1, 'b': 2, 'e': 5, 'c': 3}
    # b, 2 is present in both dict1 and dict2
    # c, 3 is present in both dict1 and dict2
    # after clear dict1: {}, dict2: {}
    # find_common_keys_of_dict1 & dict2 dictionary using list comphrehension method:
    # {'cd': 13, 'de': 41}

    # ----------------------------------------------------------------------
    # Ran 0 tests in 0.000s

    # OK
    # PS C:\Users\Anamika\Python_codes> 