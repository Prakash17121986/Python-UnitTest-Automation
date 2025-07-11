import unittest

def test_combine_two_dictionary_adding_values_for_common_keys(dict1,dict2):
    # Find the common key in both dict1 and dict2 and add both the values of dict1 and dict2 and return the common key with added values and other keys and values
    # for loop and | operator
    dict1 = {'Mon': 23, 'Tue': 11, 'Sun': 6}
    dict2 = {'Wed': 10, 'Mon': 12, 'Sun': 4}
    print(f'dict1: {dict1}')
    print(f'dict2: {dict2}')
    for key in dict2:
        if key in dict1:
            dict2[key] = dict1[key] + dict2[key]
        else:
            pass
    print(f'Adding values in dict2: {dict2}')
    res = dict1 | dict2
    print(res)

# if __name__ == '__main__':
    # test_combine_two_dictionary_adding_values_for_common_keys({'Mon': 23, 'Tue': 11, 'Sun': 6},{'Wed': 10, 'Mon': 12, 'Sun': 4})
    # unittest.main()

    # ------------Program Output-------------------------------------------
    # PS C:\Users\Anamika\Python_codes> & C:/Users/Anamika/AppData/Local/Programs/Python/Python310/python.exe c:/Users/Anamika/Python_codes/Project/tests/all_tests/DSA/test_adding_values_for_common_keys.py
    # dict1: {'Mon': 23, 'Tue': 11, 'Sun': 6}
    # dict2: {'Wed': 10, 'Mon': 12, 'Sun': 4}
    # Adding values in dict2: {'Wed': 10, 'Mon': 35, 'Sun': 10}
    # {'Mon': 35, 'Tue': 11, 'Sun': 10, 'Wed': 10}
    # ----------------------------------------------------------------------
    # Ran 0 tests in 0.000s

    # OK
    # PS C:\Users\Anamika\Python_codes>
