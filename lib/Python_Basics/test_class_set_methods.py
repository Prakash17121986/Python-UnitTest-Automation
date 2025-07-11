
import unittest

def test_set_class_methods(x, y):
    '''
    Python has a set of built-in methods that you can use on sets.
    Method	Shortcut	Description
    add()	 	Adds an element to the set
    clear()	 	Removes all the elements from the set
    copy()	 	Returns a copy of the set
    difference()	-	Returns a set containing the difference between two or more sets
    difference_update()	-=	Removes the items in this set that are also included in another, specified set
    discard()	 	Remove the specified item
    intersection()	&	Returns a set, that is the intersection of two other sets
    intersection_update()	&=	Removes the items in this set that are not present in other, specified set(s)
    isdisjoint()	 	Returns whether two sets have a intersection or not
    issubset()	<=	Returns whether another set contains this set or not
        <	Returns whether all items in this set is present in other, specified set(s)
    issuperset()	>=	Returns whether this set contains another set or not
        >	Returns whether all items in other, specified set(s) is present in this set
    pop()	 	Removes an element from the set
    remove()	 	Removes the specified element
    symmetric_difference()	^	Returns a set with the symmetric differences of two sets
    symmetric_difference_update()	^=	Inserts the symmetric differences from this set and another
    union()	|	Return a set containing the union of sets
    update()	|=	Update the set with the union of this set and others
    '''
    pass
    #print(f'__doc__: {test_set_class_methods.__doc__}')

def test_set_type(x, y):
    '''
    It returns the type of variable
    '''
    #print(f'__doc__: {test_set_type.__doc__}')

    #x = {"apple", "banana", "cherry"}
    #y = {"google", "microsoft", "apple"}

    print(f'set x: {x} type: {type(x)}')
    print(f'set y: {y}, type: {type(y)}\n')


def test_set_add(x, val='Orange'):
    '''
    Adds an element to the set
    '''
    #print(f'__doc__: {test_set_add.__doc__}')
    #x = {"apple", "banana", "cherry"}
    print(f'set x: {x}')
    
    x.add(val)

    print(f'Adding new value to set x: {x}\n')  


def test_set_copy(x):
    '''
    Returns a copy of the set
    '''
    #print(f'__doc__: {test_set_copy.__doc__}')

    #x = {"apple", "banana", "cherry"}
    print(f'set x: {x}')
    
    c = x.copy()

    print(f'copy of x: {c}')


def test_set_difference(x, y):
    '''
    Returns a set containing the difference between two or more sets
    Return a set that contains the items that only exist in set x, and not in set y
    The returned set contains items that exist only in the first set, and not in both sets.
    '''

    #print(f'__doc__: {test_set_difference.__doc__}')

    #x = {"apple", "banana", "cherry"}
    #y = {"google", "microsoft", "apple"}

    print(f'set x: {x}')
    print(f'set y: {y}')

    x = x.difference(y)
    y = y.difference(x)

    print(f'x.difference(y): {x}')
    print(f'y.difference(x): {y}')

def test_set_difference_update(x, y):
    '''
    Returns a set, that is the intersection of two other sets
    Remove the items that exist in both sets
    The difference_update() method removes the items that exist in both sets.
    you can use the -= operator
    The difference_update() method is different from the difference() method, because the difference() method returns a new set, without the unwanted items, and the difference_update() method removes the unwanted items from the original set.
    '''
    #print(f'__doc__: {test_set_difference_update.__doc__}')

    #x = {"apple", "banana", "cherry"}
    #y = {"google", "microsoft", "apple"}
    print(f'set x: {x}')
    print(f'set y: {y}')
    x.difference_update(y) 
    print(f'x.difference_update(y): {x}')
    y.difference_update(x) 
    print(f'y.difference_update(x): {y}')


def test_set_intersection(x, y):
    '''
    & - Removes the items in this set that are also included in another, specified set
    Return a set that contains the items that exist in both set x, and set y
    you can use the & operator instead
    '''
    #print(f'__doc__: {test_set_intersection.__doc__}')

    #x = {"apple", "banana", "cherry"}
    #y = {"google", "microsoft", "apple"}

    print(f'set x: {x}')
    print(f'set y: {y}')

    z = x.intersection(y) 
    
    print(f'x.intersection(y): {z}')


def test_set_intersection_update(x, y):
    '''
    & - Removes the items in this set that are also included in another, specified set
    Remove the items that is not present in both x and y
    you can use the &= operator 
    The intersection_update() method removes the items that is not present in both sets (or in all sets if the comparison is done between more than two sets).
    The intersection_update() method is different from the intersection() method, because the intersection() method returns a new set, without the unwanted items, and the intersection_update() method removes the unwanted items from the original set.
    set &= set1 & set2
    '''
    #print(f'__doc__: {test_set_intersection.__doc__}')

    #x = {"apple", "banana", "cherry"}
    #y = {"google", "microsoft", "apple"}

    print(f'set x: {x}')
    print(f'set y: {y}')

    z = x.intersection(y) 
    print(f'x.intersection(y): {z}')


def test_set_isdisjoint(x, y):
    '''
    Returns whether two sets have a intersection or not
    Return True if no items in set x is present in set y
    The isdisjoint() method returns True if none of the items are present in both sets, otherwise it returns False.
    '''
    #print(f'__doc__: {test_set_isdisjoint.__doc__}')

    #x = {"apple", "banana", "cherry"}
    #y = {"google", "microsoft", "apple"}
    print(f'set x: {x}')
    print(f'set y: {y}')

    z = x.isdisjoint(y) 
    print(f'x.isdisjoint(y): z: {z}')

def test_set_issubset(x, y):
    '''
    <=	Returns whether another set contains this set or not
    <	Returns whether all items in this set is present in other, specified set(s)
    '''

    #print(f'__doc__: {test_set_issubset.__doc__}')

    #x = {"apple", "banana", "cherry"}
    #y = {"google", "microsoft", "apple"}
    print(f'set x: {x}')
    print(f'set y: {y}')

    z = x.issubset(y) 
    print(f'x.issubset(y) : z: {z}')


def test_set_issuperset(x, y):
    '''
    >=	Returns whether this set contains another set or not
    >	Returns whether all items in other, specified set(s) is present in this set
    '''

    #print(f'__doc__: {test_set_issuperset.__doc__}')
    #x = {"apple", "banana", "cherry"}
    #y = {"google", "microsoft", "apple"}
    print(f'set x: {x}')
    print(f'set y: {y}')

    z = x.issuperset(y)
    print(f'x.issuperset(y): {z}')


def test_set_pop(x, y):
    '''
    Removes an element from the set	
    '''
    #x = {"apple", "banana", "cherry"}
    #y = {"google", "microsoft", "apple"}

    print(f'set x: {x}')
    print(f'set y: {y}')
    
    #print(f'__doc__: {test_set_pop.__doc__}')
    x = {"apple", "banana", "cherry"}

    print(f'set x: {x}')
    print('x.pop()  :', x.pop())


def test_set_symmetric_difference(x, y):
    '''
    Returns a set with the symmetric differences of two sets
    Return a set that contains all items from both sets, except items that are present in both sets:
    you can use the ^ operator 
    The returned set contains a mix of items that are not present in both sets.
    The symmetric_difference() method returns a set that contains all items from both set, but not the items that are present in both sets.	
    '''

    #print(f'__doc__: {test_set_symmetric_difference.__doc__}')
    #x = {"apple", "banana", "cherry"}
    #y = {"google", "microsoft", "apple"}

    print(f'set x: {x}')
    print(f'set y: {y}')

    z = x.symmetric_difference(y)
    print(f'x.symmetric_difference(y): {z}')

    z = x ^ y
    print(f'symmetric_difference : z = x^y: {z}')


def test_set_symmetric_difference_update(x, y):
    '''
    ^=	Inserts the symmetric differences from this set and another
    '''

    #print(f'__doc__: {test_set_symmetric_difference.__doc__}')
    #x = {"apple", "banana", "cherry"}
    #y = {"google", "microsoft", "apple"}

    print(f'set x: {x}')
    print(f'set y: {y}')

    z = x.symmetric_difference_update(y) 
    print(f'x.symmetric_difference_update(y)  : {z}')


def test_set_union(x, y):
    '''
    |	Return a set containing the union of sets
    '''
    #print(f'__doc__: {test_set_union.__doc__}')
    #x = {"apple", "banana", "cherry"}
    #y = {"google", "microsoft", "apple"}

    print(f'set x: {x}')
    print(f'set y: {y}')

    z = x.union(y) 

    print(f'set union: {z}')

def test_set_remove(fruits, value):
    '''
    |	Return a set containing the union of sets
    '''
    #print(f'__doc__: {test_set_remove.__doc__}')
    #fruits = {"apple", "banana", "cherry"}
    print(f'fruits  : {fruits}')

    fruits.remove(value)

    print(f'fruits after remove banana  : {fruits}')

def test_set_length(x, y):
    '''
    Return a length of sets
    '''
    #print(f'__doc__: {test_set_length.__doc__}')
    #x = {"apple", "banana", "cherry"}
    #y = {"google", "microsoft", "apple"}

    print(f'set x: {x}')
    print(f'set y: {y}')

    print(f'len(x) : {x.__len__()}') 
    print(f'len(y) : {y.__len__()}') 


def test_set_clear(fruits):
    '''
    Remove all elements from the fruits set
    '''
    #print(f'__doc__: {test_set_clear.__doc__}')

    #fruits = {"apple", "banana", "cherry"}
    print(f'fruits: {fruits}')
    fruits.clear()

    print(f'fruits: {fruits}')


def test_set_discard(fruits, value):
    '''
    The discard() method removes the specified item from the set.
    This method is different from the remove() method, because the remove() method will raise an error if the specified item does not exist, and the discard() method will not.
    '''
    #print(f'__doc__: {test_set_discard.__doc__}')
    #fruits = {"apple", "banana", "cherry"}
    fruits.discard(value)
    print(fruits)

def test_set_update(x,y):
    '''
    The update() method updates the current set, by adding items from another set (or any other iterable).
    If an item is present in both sets, only one appearance of this item will be present in the updated set.
    you can use the |= operator instead
    Update the set with the union of this set and others
    set |= set1 | set2
    '''
    #print(f'__doc__: {test_set_update.__doc__}')
    #x = {"apple", "banana", "cherry"}
    #y = {"google", "microsoft", "apple"}
    print(f'set x: {x}')
    print(f'set y: {y}') 
    x.update(y)
    print(f'After set update  : {x}')

def test_frozenset():
    '''
    The frozenset() function is an immutable implementation of a set object. 
    After its creation, the elements can’t be changed, added, or removed and thus, it is given the name frozenset(). 
    This function is hashable and it can be used as a key in a dictionary.
    '''
    #print(f'__doc__: {test_frozenset.__doc__}')
    odd = frozenset([1, 3, 5])
    even = frozenset([2, 4, 6])

    print("odd.union(even)",odd.union(even))
    print("odd.intersection(even)",odd.intersection(even))
    print("odd.issubset(even)",odd.issubset(even))

if __name__ == '__main__':
    test_set_type({"apple", "banana", "cherry"},{"google", "microsoft", "apple"})
    test_set_add({"apple", "banana", "cherry"}, val='Orange')
    test_set_copy({"apple", "banana", "cherry"})
    test_set_difference({"apple", "banana", "cherry"},{"google", "microsoft", "apple"})
    test_set_difference_update({"apple", "banana", "cherry"},{"google", "microsoft", "apple"})
    test_set_intersection({"apple", "banana", "cherry"},{"google", "microsoft", "apple"})
    test_set_intersection_update({"apple", "banana", "cherry"},{"google", "microsoft", "apple"})
    test_set_isdisjoint({"apple", "banana", "cherry"},{"google", "microsoft", "apple"})
    test_set_issubset({"apple", "banana", "cherry"},{"google", "microsoft", "apple"})
    test_set_issuperset({"apple", "banana", "cherry"},{"google", "microsoft", "apple"})
    test_set_pop({"apple", "banana", "cherry"},{"google", "microsoft", "apple"})
    test_set_symmetric_difference({"apple", "banana", "cherry"},{"google", "microsoft", "apple"})
    test_set_symmetric_difference_update({"apple", "banana", "cherry"},{"google", "microsoft", "apple"})
    test_set_union({"apple", "banana", "cherry"},{"google", "microsoft", "apple"})
    test_set_remove({"apple", "banana", "cherry"}, value="banana")
    test_set_length({"apple", "banana", "cherry"},{"google", "microsoft", "apple"})
    test_set_clear({"apple", "banana", "cherry"})
    test_set_discard({"apple", "banana", "cherry"},value="banana")
    test_set_update({"apple", "banana", "cherry"},{"google", "microsoft", "apple"})
    test_frozenset()
    unittest.main()
    #---------------------Program Output------------------------------------------
    #PS C:\Users\Anamika\Python_codes> & C:/Users/Anamika/AppData/Local/Programs/Python/Python310/python.exe c:/Users/Anamika/Python_codes/Project/tests/all_tests/Python_Basics/test_class_set_methods.py
    # __doc__: 
    #     It returns the type of variable
        
    # set x: {'apple', 'banana', 'cherry'} type: <class 'set'>
    # set y: {'apple', 'microsoft', 'google'}, type: <class 'set'>

    # __doc__: 
    #     Adds an element to the set
        
    # set x: {'apple', 'banana', 'cherry'}
    # Adding new value to set x: {'apple', 'banana', 'cherry', 'Orange'}

    # __doc__: 
    #     Returns a copy of the set
        
    # set x: {'apple', 'banana', 'cherry'}
    # copy of x: {'apple', 'banana', 'cherry'}
    # __doc__: 
    #     Returns a set containing the difference between two or more sets
    #     Return a set that contains the items that only exist in set x, and not in set y
    #     The returned set contains items that exist only in the first set, and not in both sets.

    # set x: {'apple', 'banana', 'cherry'}
    # set y: {'apple', 'microsoft', 'google'}
    # x.difference(y): {'cherry', 'banana'}
    # y.difference(x): {'apple', 'microsoft', 'google'}
    # __doc__:
    #     Returns a set, that is the intersection of two other sets
    #     Remove the items that exist in both sets
    #     The difference_update() method removes the items that exist in both sets.
    #     you can use the -= operator
    #     The difference_update() method is different from the difference() method, because the difference() method returns a new set, without the unwanted items, and the difference_update() method removes the unwanted items from the original set.

    # set x: {'apple', 'banana', 'cherry'}
    # set y: {'apple', 'microsoft', 'google'}
    # x.difference_update(y): {'banana', 'cherry'}
    # y.difference_update(x): {'apple', 'microsoft', 'google'}
    # __doc__:
    #     & - Removes the items in this set that are also included in another, specified set
    #     Return a set that contains the items that exist in both set x, and set y
    #     you can use the & operator instead

    # set x: {'apple', 'banana', 'cherry'}
    # set y: {'apple', 'microsoft', 'google'}
    # x.intersection(y): {'apple'}
    # __doc__:
    #     & - Removes the items in this set that are also included in another, specified set
    #     Return a set that contains the items that exist in both set x, and set y
    #     you can use the & operator instead

    # set x: {'apple', 'banana', 'cherry'}
    # set y: {'apple', 'microsoft', 'google'}
    # x.intersection(y): {'apple'}
    # __doc__:
    #     Returns whether two sets have a intersection or not
    #     Return True if no items in set x is present in set y
    #     The isdisjoint() method returns True if none of the items are present in both sets, otherwise it returns False.

    # set x: {'apple', 'banana', 'cherry'}
    # set y: {'apple', 'microsoft', 'google'}
    # x.isdisjoint(y): z: False
    # __doc__:
    #     <=  Returns whether another set contains this set or not
    #     <   Returns whether all items in this set is present in other, specified set(s)

    # set x: {'apple', 'banana', 'cherry'}
    # set y: {'apple', 'microsoft', 'google'}
    # x.issubset(y) : z: False
    # __doc__:
    #     >=  Returns whether this set contains another set or not
    #     >   Returns whether all items in other, specified set(s) is present in this set

    # set x: {'apple', 'banana', 'cherry'}
    # set y: {'apple', 'microsoft', 'google'}
    # x.issuperset(y): False
    # set x: {'apple', 'banana', 'cherry'}
    # set y: {'apple', 'microsoft', 'google'}
    # __doc__:
    #     Removes an element from the set

    # set x: {'apple', 'banana', 'cherry'}
    # x.pop()  : apple
    # __doc__:
    #     Returns a set with the symmetric differences of two sets
    #     Return a set that contains all items from both sets, except items that are present in both sets:
    #     you can use the ^ operator
    #     The returned set contains a mix of items that are not present in both sets.
    #     The symmetric_difference() method returns a set that contains all items from both set, but not the items that are present in both sets.

    # set x: {'apple', 'banana', 'cherry'}
    # set y: {'apple', 'microsoft', 'google'}
    # x.symmetric_difference(y): {'cherry', 'banana', 'microsoft', 'google'}
    # symmetric_difference : z = x^y: {'cherry', 'banana', 'microsoft', 'google'}
    # __doc__:
    #     Returns a set with the symmetric differences of two sets
    #     Return a set that contains all items from both sets, except items that are present in both sets:
    #     you can use the ^ operator
    #     The returned set contains a mix of items that are not present in both sets.
    #     The symmetric_difference() method returns a set that contains all items from both set, but not the items that are present in both sets.

    # set x: {'apple', 'banana', 'cherry'}
    # set y: {'apple', 'microsoft', 'google'}
    # x.symmetric_difference_update(y)  : None
    # __doc__:
    #     |   Return a set containing the union of sets

    # set x: {'apple', 'banana', 'cherry'}
    # set y: {'apple', 'microsoft', 'google'}
    # set union: {'apple', 'cherry', 'banana', 'microsoft', 'google'}
    # __doc__:
    #     |   Return a set containing the union of sets

    # fruits  : {'apple', 'banana', 'cherry'}
    # fruits after remove banana  : {'apple', 'cherry'}
    # __doc__:
    #     Return a length of sets

    # set x: {'apple', 'banana', 'cherry'}
    # set y: {'apple', 'microsoft', 'google'}
    # len(x) : 3
    # len(y) : 3
    # __doc__:
    #     Remove all elements from the fruits set

    # fruits: {'apple', 'banana', 'cherry'}
    # fruits: set()
    # __doc__:
    #     The discard() method removes the specified item from the set.
    #     This method is different from the remove() method, because the remove() method will raise an error if the specified item does not exist, and the discard() method will not.

    # {'apple', 'cherry'}
    # __doc__:
    #     The update() method updates the current set, by adding items from another set (or any other iterable).
    #     If an item is present in both sets, only one appearance of this item will be present in the updated set.
    #     you can use the |= operator instead
    #     Update the set with the union of this set and others
    #     set |= set1 | set2

    # set x: {'apple', 'banana', 'cherry'}
    # set y: {'apple', 'microsoft', 'google'}
    # After set update  : {'apple', 'cherry', 'banana', 'microsoft', 'google'}
    # __doc__:
    #     The frozenset() function is an immutable implementation of a set object.
    #     After its creation, the elements can’t be changed, added, or removed and thus, it is given the name frozenset().
    #     This function is hashable and it can be used as a key in a dictionary.

    # odd.union(even) frozenset({1, 2, 3, 4, 5, 6})
    # odd.intersection(even) frozenset()
    # odd.issubset(even) False

    # ----------------------------------------------------------------------
    # Ran 0 tests in 0.000s

    # OK
    # PS C:\Users\Anamika\Python_codes> 