import unittest
     
def test_combine_two_dictionary_adding_values_diff_key_change(dict1, dict2):
    # replace 'Sun' key with 'Wed' key in dict1 and add the two values of key1 and key2
    print(f"dict1:  {dict1}")
    print(f"dict2: {dict2}")
    dict3 = {}
    # 'Mon' : 23+12, 'Sun' : 6+4 if key is same in dict1 & dict2
    for key1, value1 in dict1.items():
        for key2, value2 in dict2.items():
            dict1.popitem()
            dict1['Wed'] = 6
            if key1 == key2:
                dict2[key2] = dict1[key1] + dict2[key2]
                dict3.update({key2: dict2[key2]})
            else:
                pass
    print(f'dict3: {dict3}')
    # from collections import Counter
    # res = Counter(dict1) + Counter(dict2) if keys same, add two vlaues using Counter() func

# if __name__ == '__main__':
    # dict1 = {'Mon': 23, 'Tue': 11, 'Sun': 6}
    # dict2 = {'Mon': 10, 'Tue': 12, 'Wed': 4}
    # dict3= dict()
    # test_combine_two_dictionary_adding_values_diff_key_change(dict1, dict2)
    # unittest.main()
  
    # -----------------Program Output-----------------------------------------------------
    # PS C:\Users\Anamika\Python_codes> & C:/Users/Anamika/AppData/Local/Programs/Python/Python310/python.exe c:/Users/Anamika/Python_codes/Project/tests/all_tests/DSA/test_adding_values_diff_key_change.py
    # dict1:  {'Mon': 23, 'Tue': 11, 'Sun': 6}
    # dict2: {'Mon': 10, 'Tue': 12, 'Wed': 4}
    # dict3: {'Mon': 33, 'Tue': 23, 'Wed': 10}

    # ----------------------------------------------------------------------
    # Ran 0 tests in 0.000s

    # OK
    # PS C:\Users\Anamika\Python_codes> 