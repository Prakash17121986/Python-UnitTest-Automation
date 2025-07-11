import unittest



def test_tuple_methods():
    
    '''
    Python has two built-in methods that you can use on tuples.
    Method	Description
    count()	Returns the number of times a specified value occurs in a tuple
    index()	Searches the tuple for a specified value and returns the position of where it was found
    '''
    pass
    #print(f'__doc__: {test_tuple_methods.__doc__}')

def test_find_the_count_in_a_tuple(tup, value):
    '''   
    Find the index in a tuple
    '''
    print(f'__doc__: {test_find_the_count_in_a_tuple.__doc__}')
    #thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
    print(f'tuple: {tup}')
    value = 5
    count = tup.count(value)
    print(f'Find the index in a tuple: {count}')

    return count

def test_find_the_index_in_a_tuple(tup):
    '''   
    Find the index in a tuple
    '''
    print(f'__doc__: {test_find_the_index_in_a_tuple.__doc__}')
    #thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
    print(f'tuple: {tup}')
    index = tup.index(8)
    print(f'Find the index in a tuple: {index}')
    
    return index

def test_length_of_a_tuple(tup): 
    '''   
    Find the length of tuple
    '''
    print(f'__doc__: {test_length_of_a_tuple.__doc__}')
    #tup = (1,2,3)
    print(f'tuple1: {tup}')
    length = len(tup)
    print(f'Find the length of tuple1: {length}')
    return length


def test_concatenate_two_tuple(tup1, tup2):
    '''
    concatenate two tuples
    '''
    print(f'__doc__: {test_concatenate_two_tuple.__doc__}')
    #tupl = (1,2,3)
    #tup2 = (4,5,6)
    print(f'tuple1: {tup1}')
    print(f'tuple2: {tup2}')
    result = tup1 + tup2
    print(f'concatenation of tuple1, tuple2: {result}')
    return result

def test_accessing_element_in_a_tuple(tup, index):
    '''
    Accessing an element a tuple
    '''
    print(f'__doc__: {test_accessing_element_in_a_tuple.__doc__}')
    #tup = ('hello', (1,2,3,4), {'a':1})
    print(f'tuple: {tup}')
    print(f'Accessing an element 0: {tup[0]}')
    print(f'Accessing an element 1: {tup[1]}')
    print(f'Accessing an element 2: {tup[2]}')
    return tup[index]

def test_count_the_occurance_in_a_tuple(tup, value):
    '''
    count the occurance of aan element in a tuple
    '''
    print(f'__doc__: {test_count_the_occurance_in_a_tuple.__doc__}')
    #tup = (1,2,3,4,1,2,3,3)
    value = 3
    duplicate = tup.count(value)
    print(f'tuple: {tup}')
    print(f'Find the count of {value}: {duplicate}')
    return duplicate

def test_element_exist_or_not_in_a_tuple(tup):
    '''
    check if an element exist or not in a tuple
    '''
    print(f'__doc__: {test_element_exist_or_not_in_a_tuple.__doc__}')
    tup = ('hello, helloworld')
    print(f'tuple: {tup}')
    string=tup[1]
    print(string in tup)

def test_convert_tuple_to_string(tup):
    '''
    convert tuple to a string
    '''
    print(f'__doc__: {test_convert_tuple_to_string.__doc__}')
    #tup = (1,2,3,4)
    print(f'tuple: {tup}')
    string_output = str(tup)
    print(f'convert tuple to a string : {string_output}')
    return string_output

def test_remove_the_duplicates_in_a_tuple(tup):
    '''
    Remove the duplicates in a tuple
    '''
    print(f'__doc__: {test_remove_the_duplicates_in_a_tuple.__doc__}')
    #tup = (1,2,3,4,1,2,3,5)
    print(f'tuple: {tup}')
    duplicate = set(tup)
    print(f'After remove duplicates in a tuple : {duplicate}')

def test_find_the_index_of_an_element_in_a_tuple(tup,value):
    '''
    to find the index of an element in a tuple
    '''
    print(f'__doc__: {test_find_the_index_of_an_element_in_a_tuple.__doc__}')
    #tup = (1,2,3)
    index_output = tup.index(value)
    print(f'find an element 2  of index in a tuple: {index_output}')
    return index_output

def test_list_to_tuple(list1):
    '''
    To convert list to tuple
    '''
    print(f'__doc__: {test_list_to_tuple.__doc__}')
    #list1 = [1,2,3,4,5]
    print(f'list1: {list1}')
    tup = tuple(list1)
    print(f'tuple: {tup}')
    return tup

def test_iterate_through_for_loop_in_a_tuple(tup):
    '''
    iterate through a tuple using a loop
    '''
    print(f'__doc__: {test_iterate_through_for_loop_in_a_tuple.__doc__}')
    #tup = (10,20,30,40,50)
    print(f'tup: {tup}')
    for element in tup:
        print(f'iterate through for loop in a tuple :{element}')

def test_minimum_and_maximum_element_single_tuple(tup):
    '''
    To find the minimum and maximum element in a tuple
    '''
    print(f'__doc__: {test_minimum_and_maximum_element_single_tuple.__doc__}')
    #tup = (10,20,30,40,50,1,100)
    print(f'tup: {tup}')
    min_value = min(tup)
    max_value = max(tup)
    print(f'Minimum value in tuple10: {min_value}')
    print(f'Maximum value in tuple10: {min_value}')
    return min_value, max_value

def test_tuple_of_strings_to_single_tuple(tup):
    '''
    convert a tuple of strings to a single string
    '''
    print(f'__doc__: {test_tuple_of_strings_to_single_tuple.__doc__}')
    #tup = ('h','e','l','l','o')
    print(f'tup: {tup}')
    string_output = ''.join(tup)
    print(f'tuple after string conversion: {string_output}')
    return string_output
    

def test_common_elements_in_tuple(tup1, tup2):
    '''
    Find the common elements between two tuple
    '''
    print(f'__doc__: {test_common_elements_in_tuple.__doc__}')
    #tup1 = (10,200,40)
    print(f'tuple: {tup1}')
    #tup2 = (10,200,30,40)
    print(f'tuple1: {tup1}')
    print(f'tuple2: {tup2}')
    common_elements = tuple(x for x in tup1 if x in tup2)
    print(f'common element in tuple1 and tuple2 : {common_elements}')
    return common_elements

def test_sorted_tuple(tup):
    '''
    Find the sorted output of all elements in a tuple
    '''
    print(f'__doc__: {test_sorted_tuple.__doc__}')
    #sort a tuple of integers
    #tup = (1,2,4,8,3)
    print(f'tuple: {tup}')
    sorted_tuple = sorted(tup)
    print(f'sorted tuple: {sorted_tuple}')
    return sorted_tuple

def test_sum_of_all_items_in_tuple(tup):
    '''
    Find the sum of all elements in a tuple
    '''
    print(f'__doc__: {test_sum_of_all_items_in_tuple.__doc__}')
    #tup = (1,2,3,4)
    print(f'tuple: {tup}')
    total= sum(tup)
    print(f'sum of total value in a tuple: {total}')
    return total
  
def test_merge_two_tuples_remove_duplicates(tup1, tup2):
    '''
    Merge two tuples and remove duplicates
    '''
    print(f'__doc__: {test_merge_two_tuples_remove_duplicates.__doc__}')
    #tup1 = (1,2,3,4,8,9)
    #tup2 = (1,2,3,4,5,6)
    print(f'tuple1: {tup1}')
    print(f'tuple2: {tup2}')
    merged_output = tuple(set(tup1).union(tup2))
    print(f'Merge two tuples and remove duplicates: {merged_output}')
    return merged_output

def test_first_last_element(tup):
    '''
    Find the first and last element in a tuple
    '''
    print(f'__doc__: {test_first_last_element.__doc__}')
    #tup = (1,2,3,4,8,9)
    first_element = tup[0]
    last_element = tup[-1]
    print(f'tuple: {tup}')
    print(f'first element: {first_element}, last element: {last_element}')
    return first_element, last_element

def test_tuple_of_integers_to_a_tuple_of_strings(tup):
    '''
    convert a tuple of integers to a tuple of strings
    '''
    print(f'__doc__: {test_tuple_of_integers_to_a_tuple_of_strings.__doc__}')
    #tup = (1,2,3,4,5)
    print(f'tuple: {tup}')
    string_output = tuple(str(tup))
    print(f'convert a tuple of integers to a tuple of strings: {string_output}')
    # tuple(str(x) for x in tup)
    return string_output

def test_tuple_even_odd(tup):
    '''
    Even or odd function using a tuple
    '''
    print(f'__doc__: {test_tuple_even_odd.__doc__}')
    #count the number of even or odd in a tuple
    #tup = (1,2,3,4,5,6,7,8,9,10)
    print(f'tuple: {tup}')
    even_count = sum(1 for x in range(len(tup)) if x%2 ==0)
    odd_count = sum(1 for x in range(len(tup)) if x%2 !=0)
    print(f'even_count{even_count}, odd_count: {odd_count}')
    return even_count, odd_count

    #find the product of all elements in a tuple

def test_get_product_of_all_items_in_a_tuple(tup):
    '''
    sum of all items in a tuple
    '''
    print(f'__doc__: {test_get_product_of_all_items_in_a_tuple.__doc__}')
    #tup = (10,20,30)
    print(f'tuple: {tup}')
    product = 1
    for value in tup:
        product*=value
    print(f'Product - sum of total value in a tuple: {product}')
    return product

    #split a tuple into equal parts

    # find the frequncy of each element in a tuple
def test_frequency_of_items_in_a_tuple(tup):
    '''
    Find the frequency of items in a tuple
    '''
    print(f'__doc__: {test_frequency_of_items_in_a_tuple.__doc__}')
    #tup (1,1,2,3,2,4,5,6,4)
    print(f'tuple: {tup}')
    dict_frequency = {}
    count = 0
    for element in tup:
        dict_frequency[element] = dict_frequency.get(element, 0) + 1
        print(f'Frequency of items in a tuple: {dict_frequency}')

    return dict_frequency

def test_remove_the_duplicate_in_a_tuple(tup,value):
    '''
    Remove an element from a tuple
    '''
    print(f'__doc__: {test_remove_the_duplicate_in_a_tuple.__doc__}')
    #tup = (1,2,3,4,5,3)
    print(f'tuple: {tup}')
    remove = tuple(x for x in tup if x!=value)
    print(f'removing element 200 from a tuple13 : {remove}')
    return tuple(x for x in tup if x!=value)
    
def test_tuple_difference(tup1, tup2):
    '''
    find the difference between two tuples
    '''
    print(f'__doc__: {test_tuple_difference.__doc__}')
    #difference = set.difference(tup1, tup2)
    print(f'tuple1: {tup1}, tuple2: {tup2}')
    difference = tuple(x for x in tup1 if x not in tup2)
    print(f'difference between tuple1 and tuple2 : {difference}')


    
def test_second_largest_value_in_a_tuple(tup):
    '''
    find the second largest element in a tuple
    '''
    print(f'__doc__: {test_second_largest_value_in_a_tuple.__doc__}')
    #difference = set.difference(tup1, tup2)
    print(f'tuple: {tup}')
    sorted_tuple =  sorted(tup)
    second_largest_value = sorted_tuple[-2]
    print(f'second largest value in a tuple : {second_largest_value}')



def test_tuple_is_a_subset_of_another_tuple(sub, main):
    '''
    check if a tuple is a subset of another tuple
    '''
    print(f'__doc__: {test_tuple_is_a_subset_of_another_tuple.__doc__}')
    print(f'main: {main}')
    print(f'sub: {sub}')
    output = tuple(x in main for x in sub)
    print(f'check if a tuple is a subset of another tuple : {output}')

def text_split_tuple_into_equal_parts(tup, n):
    '''
    split a tuple into equal parts
    '''
    n = 2
    tup = (1,2,3,4,5,6)
    avg = len(tup)//2
    print(f'__doc__: {text_split_tuple_into_equal_parts.__doc__}')
    print(f'tuple: {tuple}')
    split_result = []
    for value in range(0, len(tup), avg):
        split_result.append(tup[value:value+avg])
    print(f'split a tuple into equal parts : {tuple(split_result)}')
    
if __name__ == '__main__':
    #test_tuple_methods()
    test_find_the_count_in_a_tuple(tup=(1, 3, 7, 8, 7, 5, 4, 6, 8, 5), value=5)
    test_find_the_index_in_a_tuple(tup=(1, 3, 7, 8, 7, 5, 4, 6, 8, 5))
    test_length_of_a_tuple(tup=(1, 3, 7, 8, 7, 5, 4, 6, 8, 5))
    test_concatenate_two_tuple(tup1=(1,2,3), tup2=(4,5,6))
    test_accessing_element_in_a_tuple(tup=(1,2,3,4,5), index=1)
    test_count_the_occurance_in_a_tuple(tup=(1,2,3,4,5,1,2,2), value=2)
    test_element_exist_or_not_in_a_tuple(tup=('hello, helloworld'))
    test_convert_tuple_to_string(tup=(1,2,3,4,5))
    test_remove_the_duplicates_in_a_tuple(tup=(1,2,3,1,2,3,4,5))
    test_find_the_index_of_an_element_in_a_tuple(tup=(1,2,3,4,5),value=3)
    test_list_to_tuple(list1=[1,2,3,4,5])
    test_iterate_through_for_loop_in_a_tuple(tup=(10,20,30,40,50))
    test_minimum_and_maximum_element_single_tuple(tup=(10,20,30,40,50))
    test_tuple_of_strings_to_single_tuple(tup=('h','e','l','l','o'))
    test_common_elements_in_tuple(tup1=(1,2,3,4), tup2=(1,2,3))
    test_sorted_tuple(tup=(10,1,3,2,100,10,40,60))
    test_sum_of_all_items_in_tuple(tup=(1,2,3,4,5))
    test_merge_two_tuples_remove_duplicates((1,2,3,4,5,6), (1,2,3,4))
    test_first_last_element(tup=(10,20,30,40,50))
    test_tuple_of_integers_to_a_tuple_of_strings(tup=(1,2,3,4,5))
    test_tuple_even_odd(tup=(1,2,3,4,5,6,7,8,9,10))
    test_get_product_of_all_items_in_a_tuple(tup=(1,2,3,4,5))
    test_frequency_of_items_in_a_tuple(tup=(1,2,3,1,2,3,4,5))
    test_remove_the_duplicate_in_a_tuple(tup=(1,2,3,4,5,3), value=3)
    test_tuple_difference(tup1=(1,2,3,4,5), tup2=(1,2,3))
    test_second_largest_value_in_a_tuple(tup=(20,10,3,4,5,6,7))
    text_split_tuple_into_equal_parts(tup=(1,2,3,4,5,6), n=2)
    unittest.main()

# -------------------Program Output---------------------------------------------
# PS C:\Users\Anamika\Python_codes\myenv\tests\Python_Basics> python .\test_class_tuple_methods.py
# __doc__: 
#     Python has two built-in methods that you can use on tuples.
#     Method      Description
#     count()     Returns the number of times a specified value occurs in a tuple
#     index()     Searches the tuple for a specified value and returns the position of where it was found
    
# __doc__:    
#     Find the index in a tuple
    
# tuple: (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
# Find the index in a tuple: 2
# __doc__:
#     Find the index in a tuple

# tuple: (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
# Find the index in a tuple: 3
# __doc__:
#     Find the length of tuple

# tuple1: (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
# Find the length of tuple1: 10
# __doc__:
#     concatenate two tuples

# tuple1: (1, 2, 3)
# tuple2: (4, 5, 6)
# concatenation of tuple1, tuple2: (1, 2, 3, 4, 5, 6)
# __doc__:
#     Accessing an element a tuple

# tuple: (1, 2, 3, 4, 5)
# Accessing an element 0: 1
# Accessing an element 1: 2
# Accessing an element 2: 3
# __doc__:
#     count the occurance of aan element in a tuple

# tuple: (1, 2, 3, 4, 5, 1, 2, 2)
# Find the count of 3: 1
# __doc__:
#     check if an element exist or not in a tuple

# tuple: hello, helloworld
# True
# __doc__:
#     convert tuple to a string

# tuple: (1, 2, 3, 4, 5)
# convert tuple to a string : (1, 2, 3, 4, 5)
# __doc__:
#     Remove the duplicates in a tuple

# tuple: (1, 2, 3, 1, 2, 3, 4, 5)
# After remove duplicates in a tuple : {1, 2, 3, 4, 5}
# __doc__:
#     to find the index of an element in a tuple

# find an element 2  of index in a tuple: 2
# __doc__:
#     To convert list to tuple

# list1: [1, 2, 3, 4, 5]
# tuple: (1, 2, 3, 4, 5)
# __doc__:
#     iterate through a tuple using a loop

# tup: (10, 20, 30, 40, 50)
# iterate through for loop in a tuple :10
# iterate through for loop in a tuple :20
# iterate through for loop in a tuple :30
# iterate through for loop in a tuple :40
# iterate through for loop in a tuple :50
# __doc__:
#     To find the minimum and maximum element in a tuple

# tup: (10, 20, 30, 40, 50)
# Minimum value in tuple10: 10
# Maximum value in tuple10: 10
# __doc__:
#     convert a tuple of strings to a single string

# tup: ('h', 'e', 'l', 'l', 'o')
# tuple after string conversion: hello
# __doc__:
#     Find the common elements between two tuple

# tuple: (1, 2, 3, 4)
# tuple1: (1, 2, 3, 4)
# tuple2: (1, 2, 3)
# common element in tuple1 and tuple2 : (1, 2, 3)
# __doc__:
#     Find the sorted output of all elements in a tuple

# tuple: (10, 1, 3, 2, 100, 10, 40, 60)
# sorted tuple: [1, 2, 3, 10, 10, 40, 60, 100]
# __doc__:
#     Find the sum of all elements in a tuple

# tuple: (1, 2, 3, 4, 5)
# sum of total value in a tuple: 15
# __doc__:
#     Merge two tuples and remove duplicates

# tuple1: (1, 2, 3, 4, 5, 6)
# tuple2: (1, 2, 3, 4)
# Merge two tuples and remove duplicates: (1, 2, 3, 4, 5, 6)
# __doc__:
#     Find the first and last element in a tuple

# tuple: (10, 20, 30, 40, 50)
# first element: 10, last element: 50
# __doc__:
#     convert a tuple of integers to a tuple of strings

# tuple: (1, 2, 3, 4, 5)
# convert a tuple of integers to a tuple of strings: ('(', '1', ',', ' ', '2', ',', ' ', '3', ',', ' ', '4', ',', ' ', '5', ')')
# __doc__:
#     Even or odd function using a tuple

# tuple: (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# even_count5, odd_count: 5
# __doc__:
#     sum of all items in a tuple

# tuple: (1, 2, 3, 4, 5)
# Product - sum of total value in a tuple: 120
# __doc__:
#     Find the frequency of items in a tuple

# tuple: (1, 2, 3, 1, 2, 3, 4, 5)
# Frequency of items in a tuple: {1: 1}
# Frequency of items in a tuple: {1: 1, 2: 1}
# Frequency of items in a tuple: {1: 1, 2: 1, 3: 1}
# Frequency of items in a tuple: {1: 2, 2: 1, 3: 1}
# Frequency of items in a tuple: {1: 2, 2: 2, 3: 1}
# Frequency of items in a tuple: {1: 2, 2: 2, 3: 2}
# Frequency of items in a tuple: {1: 2, 2: 2, 3: 2, 4: 1}
# Frequency of items in a tuple: {1: 2, 2: 2, 3: 2, 4: 1, 5: 1}
# __doc__:
#     Remove an element from a tuple

# tuple: (1, 2, 3, 4, 5, 3)
# removing element 200 from a tuple13 : (1, 2, 4, 5)
# __doc__:
#     find the difference between two tuples

# tuple1: (1, 2, 3, 4, 5), tuple2: (1, 2, 3)
# difference between tuple1 and tuple2 : (4, 5)
# __doc__:
#     find the second largest element in a tuple

# tuple: (20, 10, 3, 4, 5, 6, 7)
# second largest value in a tuple : 10
# __doc__:
#     split a tuple into equal parts

# tuple: <class 'tuple'>
# split a tuple into equal parts : ((1, 2, 3), (4, 5, 6))

# ----------------------------------------------------------------------
# Ran 0 tests in 0.000s

# OK
# PS C:\Users\Anamika\Python_codes\myenv\tests\Python_Basics> 






