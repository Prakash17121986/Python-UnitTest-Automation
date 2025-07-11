import unittest

    # class list methods
    #==========================
    # append()	Adds an element at the end of the list
    # clear()	Removes all the elements from the list
    # copy()	Returns a copy of the list
    # count()	Returns the number of elements with the specified value
    # extend()	Add the elements of a list (or any iterable), to the end of the current list
    # index()	Returns the index of the first element with the specified value
    # insert()	Adds an element at the specified position
    # pop()	Removes the element at the specified position
    # remove()	Removes the item with the specified value
    # reverse()	Reverses the order of the list
    # sort()	Sorts the list
    # ==========================


def test_list_append(list1):
    '''
    Add an element to the value list:
    The append() method appends an element to the end of the list.
    list.append(elmnt)
    '''
    #print(f'__doc__: {test_list_append.__doc__}')

    list1 = ['apple', 'banana', 'cherry']
    print(f"List1: {list1}")
    list1.append("orange")

    print(f"List append method: {list1}\n")

    return list1


def test_list_clear(list1):
    '''
    The clear() method removes all the elements from a list.
    list.clear()   
    '''
    #print(f'__doc__: {test_list_clear.__doc__}')
    list1 = ['apple', 'banana', 'cherry']
    print(f"List1 before clear: {list1}\n")
    list1.clear()

    print(f"List after clear method: {list1}\n")

    return list1


def test_list_copy(list1):
    '''
    The copy() method returns a copy of the specified list.
    '''
    #print(f'__doc__: {test_list_copy.__doc__}')
    list1 = ['apple', 'banana', 'cherry']
    print(f"List1: {list1}")

    list2 = list1.copy()
    print(f"List2 before copy: {list2}")
    print(f"List2 after copy method: {list2}\n")

    return list2

def test_list_count(list1,value="apple"):
    '''
    The count() method returns the number of elements with the specified value.
    '''
    #print(f'__doc__: {test_list_count.__doc__}')
    list1 = ['apple', 'banana', 'cherry','apple']
    print(f"List1: {list1}")

    list1_count = list1.count(value)
    print(f"List1 count: {list1_count}\n")

    return list1_count

def test_list_extend(list1,list2):
    '''
    The extend() method adds the specified list elements (or any iterable) to the end of the current list.
    '''
    #print(f'__doc__: {test_list_extend.__doc__}')
    list1 = ['apple', 'banana', 'cherry']
    print(f"List1: {list1}")
    list2 = ['Ford', 'BMW', 'Volvo']
    print(f"List2: {list2}")
    list1.extend(list2)
    print(f"Extend of list1 with list2: {list1}\n")

    return list1


def test_list_index(list1):
    '''
    The index() method returns the position at the first occurrence of the specified value.
    '''
    #print(f'__doc__: {test_list_index.__doc__}')
    list1 = ['apple', 'banana', 'cherry']
    print(f"List1: {list1}")

    listindex = list1.index("apple")
    print(f"index of 'apple' in list1: {listindex}\n")

    return listindex

def test_list_insert(list1, index=1, value="orange"):
    '''
    The insert() method inserts the specified value at the specified position.
    '''
    #print(f'__doc__: {test_list_insert.__doc__}')

    list1 = ['apple', 'banana', 'cherry']
    print(f"List1: {list1}")
    list1.insert(1,value)

    print(f"insert of 'orange' in index1 in list1: {list1}\n")

    return list1


def test_list_pop(list1,index):
    '''
    The pop() method removes the element at the specified position.
    '''
    #print(f'__doc__: {test_list_pop.__doc__}')
    list1 = ['apple', 'banana', 'cherry']
    print(f"List1: {list1}")
    list1.pop(index)

    print(f"After pop of index 1 iin a list1: {list1}\n")
    return list1


def test_list_remove(list1,value="banana"):
    '''
    The remove() method removes the first occurrence of the element with the specified value.
    '''
    #print(f'__doc__: {test_list_remove.__doc__}')
    list1 = ['apple', 'banana', 'cherry']
    print(f"List1: {list1}")
    list1.remove(value)

    print(f"After remove 'banana' 1 iin a list1: {list1}\n")
    return list1


def test_list_reverse(list1):
    '''
    The reverse() method reverses the sorting order of the elements.
    '''
    #print(f'__doc__: {test_list_reverse.__doc__}')
    list1 = ['apple', 'banana', 'cherry']
    print(f"List1: {list1}")
    list1.reverse()

    print(f"After reverse the list1: {list1}\n")

    return list1

def test_myFunc(list1):
    length = len(list1)
    return length

def test_list_sort(list1):
    '''
    The sort() method sorts the list ascending by default.
    list.sort(reverse=True|False, key=myFunc)
    reverse - Optional. reverse=True will sort the list descending. Default is reverse=False
    key - Optional. A function to specify the sorting criteria(s)
    '''
    #print(f'__doc__: {test_list_sort.__doc__}')
    list1 = ['Ford', 'BMW', 'Volvo']
    print(f"List1 before sort: {list1}")
    #list2 = list1.sort() # modifies the original list and returns None
    list2 = sorted(list1)
    #list3 = list1.sort(key=test_myFunc)
    #list4 = list1.sort(reverse=True, key=test_myFunc)
    print(f"After sort the list: {list2}")

    return list2


if __name__ == '__main__':
    test_list_append(list1=['apple', 'banana', 'cherry'])
    test_list_clear(list1=['apple', 'banana', 'cherry'])
    test_list_copy(list1=['apple', 'banana', 'cherry'])
    test_list_count(list1=['apple', 'banana', 'cherry'],value="apple")
    test_list_extend(list1=['apple', 'banana', 'cherry'],list2=['Ford', 'BMW', 'Volvo'])
    test_list_index(list1=['apple', 'banana', 'cherry'])
    test_list_insert(list1=['apple', 'banana', 'cherry'],index=1, value="orange")
    test_list_pop(list1=['apple', 'banana', 'cherry'],index=1)
    test_list_remove(list1=['apple', 'banana', 'cherry'],value="banana")
    test_list_reverse(list1=['apple', 'banana', 'cherry'])
    test_list_sort(list1=['Ford', 'BMW', 'Volvo'])
    unittest.main()

    # ----------------------------Program output-------------------------------
    # PS C:\Users\Anamika\Python_codes\myenv\tests\Python_Basics> python .\test_class_list_methods.py
    # __doc__: 
    #     Add an element to the value list:
    #     The append() method appends an element to the end of the list.
    #     list.append(elmnt)
        
    # List1: ['apple', 'banana', 'cherry']
    # List append method: ['apple', 'banana', 'cherry', 'orange']

    # __doc__:
    #     The clear() method removes all the elements from a list.
    #     list.clear()

    # List1 before clear: ['apple', 'banana', 'cherry']

    # List after clear method: []

    # __doc__:
    #     The copy() method returns a copy of the specified list.

    # List1: ['apple', 'banana', 'cherry']
    # List2 before copy: ['apple', 'banana', 'cherry']
    # List2 after copy method: ['apple', 'banana', 'cherry']

    # __doc__:
    #     The count() method returns the number of elements with the specified value.

    # List1: ['apple', 'banana', 'cherry', 'apple']
    # List1 count: 2

    # __doc__:
    #     The extend() method adds the specified list elements (or any iterable) to the end of the current list.

    # List1: ['apple', 'banana', 'cherry']
    # List2: ['Ford', 'BMW', 'Volvo']
    # Extend of list1 with list2: ['apple', 'banana', 'cherry', 'Ford', 'BMW', 'Volvo']

    # __doc__:
    #     The index() method returns the position at the first occurrence of the specified value.

    # List1: ['apple', 'banana', 'cherry']
    # index of 'apple' in list1: 0

    # __doc__:
    #     The insert() method inserts the specified value at the specified position.

    # List1: ['apple', 'banana', 'cherry']
    # insert of 'orange' in index1 in list1: ['apple', 'orange', 'banana', 'cherry']

    # __doc__:
    #     The pop() method removes the element at the specified position.

    # List1: ['apple', 'banana', 'cherry']
    # After pop of index 1 iin a list1: ['apple', 'cherry']

    # __doc__:
    #     The remove() method removes the first occurrence of the element with the specified value.

    # List1: ['apple', 'banana', 'cherry']
    # After remove 'banana' 1 iin a list1: ['apple', 'cherry']

    # __doc__:
    #     The reverse() method reverses the sorting order of the elements.

    # List1: ['apple', 'banana', 'cherry']
    # After reverse the list1: ['cherry', 'banana', 'apple']

    # __doc__:
    #     The sort() method sorts the list ascending by default.
    #     list.sort(reverse=True|False, key=myFunc)
    #     reverse - Optional. reverse=True will sort the list descending. Default is reverse=False
    #     key - Optional. A function to specify the sorting criteria(s)

    # List1 before sort: ['Ford', 'BMW', 'Volvo']
    # After sort the list: ['BMW', 'Ford', 'Volvo']

    # ----------------------------------------------------------------------
    # Ran 0 tests in 0.000s

    # OK
    # PS C:\Users\Anamika\Python_codes\myenv\tests\Python_Basics> 