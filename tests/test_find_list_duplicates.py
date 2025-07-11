import unittest

def test_list_duplicate_set_method(listvalue):
    print(f'Given list: {listvalue}')
    #listvalue = ['a','b','c','d','a','b']

    # set method, output is unordered, remove the duplicates
    output = set(listvalue)
    print(f'Remove duplicates using set method, {output}')

def test_list_duplicate_append_method(listvalue):
    #listvalue =[10,2,1,3,2,5,6,7,9,1,3]
    print(f'Given list: {listvalue}')
    # list append method, output is ordered, remove the duplicates
    list1 = []
    for item in listvalue:
        if item not in list1:
            list1.append(item)

    print(f'Remove duplicates using append method, {sorted(list1)}')

def test_list_duplicate_fromkeys_method(listvalue):
    #listvalue =[10,2,1,3,2,5,6,7,9,1,3]
    print(f'Given list: {listvalue}')
    d = {}
    # dictionary method, output is ordered, remove the duplicates
    for item in listvalue:
        d[item] = None
    #print(d.keys())

    freq =  list(sorted(dict.fromkeys(listvalue).keys()))
    print(f'Remove duplicates using dict.fromkeys().keys() method, {freq}')


def test_list_duplicate_index_method(listvalue):
    print(f'Given list: {listvalue}')
    # Index method and counter check
    Found = False
    unique = []
    #listvalue =[10,2,1,3,2,5,6,7,9,1,3]
    for indx, value in enumerate(listvalue):
        if indx == listvalue.index(value):
            Found=True
            unique.append(listvalue[indx])
        #else:
            #print(f"Duplicate value: {listvalue[indx]}")


    print(f'Remove duplicates using index method, {sorted(unique)}')
           

def test_list_duplicate_hashable(listvalue):
    print(f'Given list: {listvalue}')
    hashset = set()
    for n in listvalue:
        if n in hashset:
            return True
        hashset.add(n)
  
        print(f'Remove duplicates using hashable method: {hashset}')
    return False

def test_list_duplicate_hashable_window(listvalue):
    print(f'Given list: {listvalue}')
    window = set()
    L = 0
    for R in range(len(listvalue)):
        if R - L > len(listvalue):
            window.remove(listvalue[L])
            L+=1
        if listvalue[R] in window:
            return True
        window.add(listvalue[R])
  
        print(f'Remove duplicates using window method: {window}')
    return False
    


# if __name__ == '__main__':
#     test_list_duplicate_set_method(['a','b','c','d','a','b'])
#     test_list_duplicate_append_method([10,2,1,3,2,5,6,7,9,1,3])
#     test_list_duplicate_fromkeys_method([10,2,1,3,2,5,6,7,9,1,3])
#     test_list_duplicate_index_method([10,2,1,3,2,5,6,7,9,1,3])
#     value = test_list_duplicate_hashable([10,2,1,3,2,5,6,7,9,1,3])
#     print(value)
#     test_list_duplicate_hashable_window([10,2,1,3,2,5,6,7,9,1,3])
#     unittest.main()

# PS C:\Users\Anamika\Python_codes> & C:/Users/Anamika/AppData/Local/Programs/Python/Python310/python.exe c:/Users/Anamika/Python_codes/Project/tests/all_tests/DSA/test_find_list_duplicates.py
# Given list: ['a', 'b', 'c', 'd', 'a', 'b']
# Remove duplicates using set method, {'b', 'a', 'd', 'c'}
# Given list: [10, 2, 1, 3, 2, 5, 6, 7, 9, 1, 3]
# Remove duplicates using append method, [1, 2, 3, 5, 6, 7, 9, 10]
# Given list: [10, 2, 1, 3, 2, 5, 6, 7, 9, 1, 3]
# Remove duplicates using dict.fromkeys().keys() method, [1, 2, 3, 5, 6, 7, 9, 10]
# Given list: [10, 2, 1, 3, 2, 5, 6, 7, 9, 1, 3]
# Remove duplicates using index method, [1, 2, 3, 5, 6, 7, 9, 10]
# Given list: [10, 2, 1, 3, 2, 5, 6, 7, 9, 1, 3]
# Remove duplicates using hashable method: {10}
# Remove duplicates using hashable method: {10, 2}
# Remove duplicates using hashable method: {1, 10, 2}
# Remove duplicates using hashable method: {3, 1, 10, 2}
# True
# Given list: [10, 2, 1, 3, 2, 5, 6, 7, 9, 1, 3]
# Remove duplicates using window method: {10}
# Remove duplicates using window method: {10, 2}
# Remove duplicates using window method: {1, 10, 2}
# Remove duplicates using window method: {3, 1, 10, 2}
# ----------------------------------------------------------------------
# Ran 0 tests in 0.000s

# OK
# PS C:\Users\Anamika\Python_codes> 