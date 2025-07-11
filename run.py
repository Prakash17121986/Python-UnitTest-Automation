       
import unittest
import tests
from lib import test_list_methods
from lib.test_list_methods import Test_ListMethods
from tests import test_listoperations
from HTMLTestRunner.runner import HTMLTestRunner
from io import StringIO
import sys
from lib.Python_Basics import test_comments
from lib.Python_Basics import test_Indendations
#from lib.Python_Basics import test_typecasting
from lib.Python_Basics import test_variables
from lib.Python_Basics import test_numbers
from lib.Python_Basics import test_operators
from lib.Python_Basics import test_datatypes
from lib.Python_Basics import test_strings
from lib.Python_Basics import test_class_strings_methods
from lib.Python_Basics import test_class_tuple_methods
from lib.Python_Basics import test_class_list_methods
from lib.Python_Basics import test_class_set_methods
from lib.Python_Basics import test_dictionary_methods
from lib.Python_Basics import test_for_loop
from lib.Python_Basics import test_while_loop
from lib.Python_Basics.test_functions import test_basicfunctions
from lib.Python_Basics import test_comments

from tests import test_adding_values_different_keys_change
from tests import test_adding_values_for_common_keys
from tests import test_append_keys_values_inorder_dictionary
from tests.test_copy_update_of_dictionary import test_dict_copy_update
from tests import test_dict_from_keys_method
from tests.test_dict_functions import test_dict_functions 
from tests.test_dictionary_methods import test_dict_datatype
from tests import test_fibonnic_series
from tests import test_find_armstrong_number
from tests.test_find_common_keys_in_list_and_dict import test_find_common_keys_in_list_dict
from tests.test_find_common_keys_of_two_dictionary import test_find_common_keys_of_two_dictionary
from tests.test_find_diff_in_keys_of_two_dictionary import test_find_diff_in_keys_of_two_dict
from tests import test_find_even_odd
from tests.test_find_factorial_number import test_find_factorial_number
from tests import test_find_fibonnic_series_generator_method
from tests import test_find_key_associated_values_using_index 
from tests.test_find_keys_with_duplicate_values_in_dictionary import test_keys_values_exchange_in_dictionary
from tests.test_find_largest_key_in_dictionary import test_largest_key_in_dictionary
from tests import test_find_largest_number
from tests import test_find_list_duplicates
from tests.test_find_prime_number import test_primenumber
from tests import test_find_smallest_number
from tests.test_handling_missing_key_in_dictionary import test_handling_missing_key_in_dictionary 
from tests import test_if_ellif_else
from tests.test_keys_values_to_lowercase_dictionary import test_keys_values_to_lowercase
from tests import test_listoperations
from tests.test_merge_two_dictionary import test_merge_dict_method
from tests.test_split_single_dict_to_multiple_dict import test_split_single_dict_to_multiple_dict 
from tests.test_sum_of_values_in_tuple_of_dictionary import test_tuple_of_dictionary
from tests.test_swap_keys_values import test_swap_keys_values



# Object instantiation
Test_ListMethods = Test_ListMethods([10,20,30], [4,5,6])

copy_update = test_dict_copy_update()
dict_functions = test_dict_functions()
dict_datatype = test_dict_datatype()
common_keys = test_find_common_keys_in_list_dict()
common_keys_two = test_find_common_keys_of_two_dictionary()
diff_key_dict = test_find_diff_in_keys_of_two_dict()
fact = test_find_factorial_number()
k_v_exchange = test_keys_values_exchange_in_dictionary()
largest_key = test_largest_key_in_dictionary()
prime = test_primenumber()
k_v_lower = test_keys_values_to_lowercase()
merge_dict = test_merge_dict_method()
split_single_to_multiple = test_split_single_dict_to_multiple_dict()
t_dict = test_tuple_of_dictionary()
swap_k_v = test_swap_keys_values()
missing_key = test_handling_missing_key_in_dictionary()




class Test_List_Functions(unittest.TestCase):
    
    def test_create_a_list(self):
        
        Test_ListMethods.test_createlist()
        
        
    def test_append_values_to_the_list(self):
        
        Test_ListMethods.test_append(value=40)
        
    
    def test_extend_values_to_the_list(self):
        
        Test_ListMethods.test_extend(value=[1,2,3])
 

    def test_find_the_index_of_the_value_in_list(self):
        
        Test_ListMethods.test_index(listvalue=2)
        

    def test_find_the_count_of_the_value_in_list(self):
        
        Test_ListMethods.test_count(countvalue=1)

    
    def test_insert_the_value_in_list(self):
        
        Test_ListMethods.test_insert(index=0, insertvalue=100)
    
    
    def test_remove_the_value_in_list(self):
        
        Test_ListMethods.test_remove(removevalue=1)
       
     
    def test_reverse_list(self):
        
        Test_ListMethods.test_reverse()

        
    def test_sort_list(self):
        
        Test_ListMethods.test_sort()

         
    def test_copy_deepcopy(self):
        
        Test_ListMethods.test_copy_deepcopy(list3=[], list4=[])
        
        
    def test_clear_list(self):
        
        Test_ListMethods.test_clear()

    def test_iterate_elements_using_for_loop(self):
        
        Test_ListMethods.test_iterate_elements_using_for_loop(listvalue=["apple","orange","watermelon","Bannana", "pineapple", "pomogranite", "Kiwi"])
        
    
    def test_iterate_element_with_range_func_using_for_loop(self):
    
        Test_ListMethods.test_iterate_element_with_range_func_using_for_loop(listvalue=["apple","orange","watermelon","Bannana", "pineapple", "pomogranite", "Kiwi"])
        
        
    def test_iterate_element_with_enumerate_func_using_for_loop(self):
        
        Test_ListMethods.test_iterate_element_with_enumerate_func_using_for_loop(listvalue=["apple","orange","watermelon","Bannana", "pineapple", "pomogranite", "Kiwi"])
        
        
    def test_for_loop_using_conditional_statement1(self):
        
        Test_ListMethods.test_for_loop_using_conditional_statement1(listvalue=["apple","orange","watermelon","Bannana", "pineapple", "pomogranite", "Kiwi"])
        
      
    def test_for_loop_using_conditional_statement2(self):
        
        Test_ListMethods.test_for_loop_using_conditional_statement2(listvalue=["apple","orange","watermelon","Bannana", "pineapple", "pomogranite", "Kiwi"])
        
        
    def test_for_loop_using_conditional_statement3(self):
        
        Test_ListMethods.test_for_loop_using_conditional_statement3(listvalue=["apple","orange","watermelon","Bannana", "pineapple", "pomogranite", "Kiwi"])
        
        
    def test_iterate_element_with_positive_slicing_using_for_loop(self):
        
        Test_ListMethods.test_iterate_element_with_positive_slicing_using_for_loop(listvalue=["apple","orange","watermelon","Bannana", "pineapple", "pomogranite", "Kiwi"])



class Test_UserDefinedFunctions(unittest.TestCase):
   
    def test_copy_update_of_dictionary(self):
        copy_update.test_copy_update_of_dictionary({1: 'a', 2: 'b'},{2: 'c', 4: 'd'})
        
    def test_Multiplication_of_number(self):
        dict_functions.test_Multiplication_of_number(d={})
        
    def test_sum_of_all_numbers(self):
        dict_functions.test_sum_of_all_numbers(sum=0, my_dict = {'data1':100,'data2':-54,'data3':247})
        
    def test_list_of_keys_by_value_method(self):
        dict_functions.test_list_of_keys_by_value_method(reverse={}, my_dict={'A':1,'B':3,'C':3,'D':4,'E':1,'F':3})
    
    def test_filtering_keys_are_even(self):
        dict_functions.test_filtering_keys_are_even(newDict={}, my_dict={7 : 'sami',8: 'jana',9: 'rami',10: 'rana',11 : 'reem', 12 : 'salma'}, sorted_value = {})
        
    def test_dict_after_dropping_empty_items(self):  
        dict_functions.test_dict_after_dropping_empty_items({'c1': 'Red', 'c2': 'Green', 'c3':None})
    
    def test_dict_filter_function(self):
        dict_functions.test_dict_filter_function({'1': 75, '2': 80, '3': 65,'4': 90})
    
    def test_dict_print_function(self):
        dict_functions.test_dict_print_function()
        
    def test_dictionary_methods(self):
        dict_datatype.test_dict_methods({'a':1,'b':2,'c':3,'d':4,'a':1}, thisdict={})
        
    def test_find_common_keys_in_list_and_dict(self):
        common_keys.test_find_common_keys_listdict({1:'a', 2:'b', 3:'c', 4:'d'},[1,2,3])
        
    def test_find_common_keys_of_two_dictionary_set(self):
        common_keys_two.test_find_common_keys_of_two_dictionary_set({2: 'a', 2: 'b', 3: 'c'},{2: 'c', 4: 'd', 3: 'c'})
    
    def test_find_common_keys_of_two_dictionary_set_items(self):
        common_keys_two.test_find_common_keys_of_two_dictionary_set_items({'a': 1, 'b': 2, 'c': 3, 'd': 4},{'t1': 1, 'b': 2, 'e': 5, 'c': 3})
        
    def test_find_common_keys_of_two_dictionary_list_comphrension(self):
        common_keys_two.test_find_common_keys_of_two_dictionary_list_comphrension({'ab': 11, 'bc': 21, 'cd': 13, 'de': 41},{'cd': 33, 'ad': 14, 'de': 51, 'fa': 16})
        
    def test_find_diff_in_keys_of_two_dictionary(self):
        diff_key_dict.test_find_difference_in_keys_of_two_dictionary({'1': 'Mon', '2': 'Tue', '3': 'Wed'},{'3': 'Wed', '4': 'Thur', '5': 'Fri'})

    def test_find_factorial_number(self):
        fact.test_factorial(5, 1)
        
    def test_find_keys_with_duplicate_values_in_dictionary(self):
        k_v_exchange.test_find_keys_with_duplicate_values_in_dictionary({'Sun': 5, 'Mon': 3, 'Tue': 5, 'Wed': 3})
        
    def test_find_largest_key_in_dictionary(self):
        largest_key.test_largest_key_in_dictionary(4, {12: 10, 22: 12, 18 : 4, 8: 20, 14: 9, 9: 13}, [], [])
    
    def test_find_prime_number(self):
        prime.test_find_primenumber(5, flag=False)
    
    def test_keys_values_to_lowercase_dictionary(self):
        k_v_lower.test_keys_values_to_lowercase_dictionary({'Foo': 'Hello', 'Bar': 'World'})
        
    def test_merge_two_dictionary(self):
        merge_dict.test_merge_two_dictionary({1: 'a', 2: 'b'},{2: 'c', 4: 'd'})
        
    def test_split_single_dict_to_multiple_dict(self):
        split_single_to_multiple.test_split_single_dict_to_multiple_dict({1:'a', 2:'b', 3:'c', 4:'d'}, 2)
        
    def test_sum_of_values_in_tuple_of_dictionary(self):
        t_dict.test_tuple_of_dictionary(d1={"a":100, "b":200, "c": 300}, d2={"a": 300, "b":200, "d": 400})
        
    def test_swap_keys_values(self):
        swap_k_v.test_swap_keys_values_in_dictionary({1:'One', 2:'Two', 3:'Three'})
        
    def test_handling_missing_key_in_dictionary(self):
        missing_key.test_handling_missing_key_in_dictionary({'India': 'IN', 'Australia': 'AUS', 'Brazil': 'BZ'})
        
    def test_adding_values_different_keys_change(self):
        dict1 = {'Mon': 23, 'Tue': 11, 'Sun': 6}
        dict2 = {'Mon': 10, 'Tue': 12, 'Wed': 4}
        dict3= dict()
        test_adding_values_different_keys_change.test_combine_two_dictionary_adding_values_diff_key_change(dict1, dict2)
        
    def test_adding_values_for_common_keys(self):
        test_adding_values_for_common_keys.test_combine_two_dictionary_adding_values_for_common_keys({'Mon': 23, 'Tue': 11, 'Sun': 6},{'Wed': 10, 'Mon': 12, 'Sun': 4})
        
    def test_append_keys_values_inorder_dictionary(self):
        test_append_keys_values_inorder_dictionary.test_append_keys_values_inorder_dictionary({1:'a', 2:'b', 3:'c', 4:'d'})
    
    def test_dict_from_keys_method(self):
        test_dict_from_keys_method.test_dict_from_keys(b = 0, a = ('key1', 'key2', 'key3'), c= None)
        
    def test_fibonnic_series(self):
        test_fibonnic_series.test_fibonnic_series(10)
        
    def test_find_armstrong_number(self):
        test_find_armstrong_number.test_armstrong(153, temp=int, sum_value=0)
        
    def test_find_even_odd(self):
        test_find_even_odd.test_even_odd(30)
        
        even, odd = test_find_even_odd.test_list_comhrension_method(30)
        print(f'even numbers using list comphrension method: {even}')
        print(f'odd numbers using list comphrension method: {odd}')
        
        test_find_even_odd.test_list_comhrension_method1(20)
        
        even_num, odd_num = test_find_even_odd.test_list_comprehension_filter([1,2,3,4,5,6,7,8])
        print(f'even numbers using list comphrension method: {even_num}')
        print(f'odd numbers using list comphrension method: {odd_num}')
        
        test_find_even_odd.test_for_loop_even_odd([1,2,3,4,5,6,7,8])
        
        test_find_even_odd.test_while_loop_even_odd([1,2,3,4,5,6,7,8])
        
        test_find_even_odd.test_list_counter_method([1,2,3,4,5,6,7,8])
        
        test_find_even_odd.test_list_collections_counter_method([1,2,3,4,5,6,7,8])
        
        test_find_even_odd.test_list_filter_lambda_method(30)
        
    def test_find_fibonnic_series_generator_method(self):
        for num in test_find_fibonnic_series_generator_method.fibonacci():
            if num > 50:
                break
            print(num)
        
    def test_find_key_associated_values_using_index(self):
        test_find_key_associated_values_using_index.test_key_associated_values_using_index({'One': 100, 'Two': 200, 'Three': 300})
        
    def test_find_largest_number(self):
        test_find_largest_number.find_largest_number(listvalue=[1,2,4,3,19,50])
        
    def test_find_list_duplicates(self):
        test_find_list_duplicates.test_list_duplicate_set_method(['a','b','c','d','a','b'])
        test_find_list_duplicates.test_list_duplicate_append_method([10,2,1,3,2,5,6,7,9,1,3])
        test_find_list_duplicates.test_list_duplicate_fromkeys_method([10,2,1,3,2,5,6,7,9,1,3])
        test_find_list_duplicates.test_list_duplicate_index_method([10,2,1,3,2,5,6,7,9,1,3])
        value = test_find_list_duplicates.test_list_duplicate_hashable([10,2,1,3,2,5,6,7,9,1,3])
        print(value)
        test_find_list_duplicates.test_list_duplicate_hashable_window([10,2,1,3,2,5,6,7,9,1,3])
        
    def test_find_smallest_number(self):
        test_find_smallest_number.find_smallest_number(listvalue=[1,2,4,3,19,50])
    
        
    def test_if_ellif_else(self):
        year_to_check =  2018
        returned_value = test_if_ellif_else.test_check_leap_year(year_to_check)
        print(returned_value)
        test_if_ellif_else.test_if_else(100)
        test_if_ellif_else.test_if_else(1001)
        test_if_ellif_else.test_pet_type(pet_type="fish")
        test_if_ellif_else.test_pet_type(pet_type="dog")
        test_if_ellif_else.test_pet_type(pet_type="cat")
        test_if_ellif_else.test_compare_two_numbers()
        test_if_ellif_else.test_compare_equal_numbers()
        test_if_ellif_else.test_compare_greater_equal_number()
        test_if_ellif_else.test_compare_greater_number()
        test_if_ellif_else.test_if_else_one_line_statement()
 
# Object instantiation
arithmetic = test_operators.test_arithmetic_operators()
assignment = test_operators.test_assignment_operators()
comparision = test_operators.test_comparision_operators()
logical = test_operators.test_logical_operators()   
identity = test_operators.test_identity_operators()
membership = test_operators.test_membership_operators()  
bitwise = test_operators.test_bitwise_operators()
operator_precedence = test_operators.test_operator_procedence()
for_loop = test_for_loop.test_for_loop()
test_loop = test_while_loop.test_while_loop()
func = test_basicfunctions(10,20,30)

class Test_Operators(unittest.TestCase):
    
    def test_arithmetic_operator(self):
        arithmetic.test_arithmetic_operator(15,3)
    
    def test_assignment_operator(self):
        assignment.test_assignment_operator(5)
        
    def test_comparision_operator(self):  
        comparision.test_comparision_operator(3,5)
        
    def test_logical_operator(self):  
        logical.test_logical_operator(4)
       
    def test_identity_operator(self):  
        identity.test_identity_operator(["apple", "banana"],["apple", "banana"])
        
    def test_membership_operator(self):   
        membership.test_membership_operator(["apple", "banana"])
    
    def test_bitwise_operator(self):
        bitwise.test_bitwise_operator()
        
    def test_test_operator_procedence(self):   
        operator_precedence.test_operator_procedence()
        
class Test_Comments(unittest.TestCase):
    
    def test_comments(self):
        test_comments.test_comments()

class Test_indentation(unittest.TestCase):
    def test_indentation(self):
        test_Indendations.test_indentation()

class Test_variables(unittest.TestCase):
    def test_variables(self):
        test_variables.test_variablenames()
        test_variables.test_createvariables()
       
# class Test_typecasting(unittest.TestCase):
#     def test_typecasting():
#         test_typecasting.test_typecasting()
    
class Test_numbers(unittest.TestCase):
    def test_numbers(self):
        test_numbers.test_integers()
        test_numbers.test_float()
        test_numbers.test_complex()
        
    
class Test_data_types(unittest.TestCase):
    
    def test_datatypes_func(self):
        test_datatypes.test_datatypes_func()
        
    def test_datatypes_bytes(self):
        test_datatypes.test_datatypes_bytes()
        
    def test_datatypes_list(self):
        test_datatypes.test_datatypes_list()
        
    def test_datatypes_string(self):
        test_datatypes.test_datatypes_string()
        
    def test_datatypes_complex(self):
        test_datatypes.test_datatypes_complex()
        
    def test_datatypes_set(self):
        test_datatypes.test_datatypes_set()
        
    def test_datatypes_range(self):
        test_datatypes.test_datatypes_range()
        
    def test_datatypes_dictionary(self):
        test_datatypes.test_datatypes_dictionary()
        
    def test_datatypes_tuple(self):
        test_datatypes.test_datatypes_tuple()
        
    def test_datatypes_frozenset(self):
        test_datatypes.test_datatypes_frozenset()
        
    def test_datatypes_bool(self):
        test_datatypes.test_datatypes_bool()
        
    def test_datatypes_bytearray(self):
        test_datatypes.test_datatypes_bytearray()
        
    def test_datatypes_memoryview(self):
        test_datatypes.test_datatypes_memoryview()
        
    def test_datatypes_none(self):
        test_datatypes.test_datatypes_none()

class Test_string_functions(unittest.TestCase):
    
    def test_single_quote_strings(self):
        test_strings.test_single_quote_string(string_value = 'Hello, World!')
        
    def test_double_quote_string(self): 
        test_strings.test_double_quote_string(string_value = "Hello, World!")
        
    def test_three_quote_string(self):
        test_strings.test_three_quote_string(string_value = "Hello world")
        
    def test_string_char_read(self):
        test_strings.test_string_char_read(string_value = "Hello, World!")
        
    def test_string_length(self):
        test_strings.test_string_length(string_value = "Hello, World!")
        
    def test_string_loop(self):
        test_strings.test_string_loop(string_value = "Hello, World!")
        
    def test_check_string(self):
        test_strings.test_check_string(string_value = "Hello, World!")
        
    def test_check_if_not_in_string(self):
        test_strings.test_check_if_not_in_string(string_value = "Hello, World!")
        
    def test_concatenate_strings(self):
        test_strings.test_concatenate_strings(string_value1="hello", string_value2="world")
        
    def test_string_format(self):
        test_strings.test_string_format()
        
    def test_escape_character_in_strings(self):
        test_strings.test_escape_character_in_strings(string_value="hello")
        
    def test_slicing(self):
        test_strings.test_slicing(string_value="hello")
        
    def test_modify_strings(self):
        test_strings.test_modify_strings(string_value="hello world ")
        
class Test_string_methods(unittest.TestCase):
    
    def test_string_isdigit(self):
        test_class_strings_methods.test_string_isdigit("12345")
    
    def test_string_expandtabs(self):
        test_class_strings_methods.test_string_expandtabs("H\te\tl\tl\to", 4)
        
    def test_string_find(self):    
        test_class_strings_methods.test_string_find("Hello, welcome to my world.", 5, 10)
        
    def test_string_format(self):
        test_class_strings_methods.test_string_format("For only {price:.2f} dollars!")
       
    def test_string_index(self):
        test_class_strings_methods.test_string_index("Hello, welcome to my world.")
        
    def test_string_islower(self):   
        test_class_strings_methods.test_string_islower("hello world!")
    
    def test_string_isupper(self): 
        test_class_strings_methods.test_string_isupper("hello world!")
        
    def test_string_swapcase(self):
        test_class_strings_methods.test_string_swapcase("Hello My Name Is PETER")
        
    def test_string_join(self):
        test_class_strings_methods.test_string_join(("John", "Peter", "Vicky"), {"name": "John", "country": "Norway"})
        
    def test_string_split(self):
        test_class_strings_methods.test_string_split("hello, my name is Peter, I am 26 years old")
        
    def test_string_splitlines(self):
        test_class_strings_methods.test_string_splitlines("Thank you for the music\nWelcome to the jungle")
    
    def test_string_startswith(self):
        test_class_strings_methods.test_string_startswith("Hello, welcome to my world.")
        
    def test_string_endswith(self):
        test_class_strings_methods.test_string_endswith("Hello, welcome to my world.")
        
    def test_string_strip(self):
        test_class_strings_methods.test_string_strip(",,,,,rrttgg.....banana....rrr")
        
    def test_string_partition(self):
        test_class_strings_methods.test_string_partition("I could eat bananas all day")
     
    def test_string_capitalize(self):
        test_class_strings_methods.test_string_capitalize("hello, and welcome to my world.")
        
    def test_string_casefold(self):    
        test_class_strings_methods.test_string_casefold("Hello, And Welcome To My World!")
        
    def test_string_replace(self):
        test_class_strings_methods.test_string_replace("Hello, And Welcome To My World!")
      
    def test_string_slicing(self):
        test_class_strings_methods.test_string_slicing("Hello, World!")
        
    def test_string_encode_function(self):
        test_class_strings_methods.test_string_encode_function("My name is Ståle")
        
    def test_string_count(self):
        test_class_strings_methods.test_string_count("I love apples, apple are my favorite fruit")
        
    def test_string_center(self):  
        test_class_strings_methods.test_string_center("banana")
       
    def test_string_isidentifier(self):
        test_class_strings_methods.test_string_isidentifier("I love apples, apple are my favorite fruit")
        
    def test_string_maketrans_translate(self):
        test_class_strings_methods.test_string_maketrans_translate("Hello Sam!")
     
    def test_string_title(self):
        test_class_strings_methods.test_string_title("Welcome to my 2nd world")
    
    def test_string_zfill(self):
        test_class_strings_methods.test_string_zfill("12345")
      
    def test_string_alpha(self):
        test_class_strings_methods.test_string_alpha("Company12")
        
    def test_string_isalpha(self):
        test_class_strings_methods.test_string_isalpha("CompanyX")
       
    def test_string_isascii(self):
        test_class_strings_methods.test_string_isascii("Company123")
        
    def test_string_isdecimal(self):
        test_class_strings_methods.test_string_isdecimal("123")
        
    def test_string_isnumeric(self):   
        test_class_strings_methods.test_string_isnumeric("565543")
        
    def test_string_isprintable(self): 
        test_class_strings_methods.test_string_isprintable("Hello!\nAre you #1?")
    
    def test_string_isspace(self): 
        test_class_strings_methods.test_string_isspace("  ")
        
    def test_string_istitle(self): 
        test_class_strings_methods.test_string_istitle("Hello, And Welcome To My World!")
        
    def test_string_ljust(self): 
        test_class_strings_methods.test_string_ljust("Hello, And Welcome To My World!",20)
        
    def test_string_rjust(self):
        test_class_strings_methods.test_string_rjust("Hello, And Welcome To My World!",20)
    
    def test_string_lstrip(self):
        test_class_strings_methods.test_string_lstrip("Hello, And Welcome To My World!")
    
    def test_string_rfind(self):
        test_class_strings_methods.test_string_rfind("Hello, And Welcome To My World!", 'Welcome')
        
    def test_string_rindex(self):
        test_class_strings_methods.test_string_rindex("Hello, And Welcome To My World!", 'Welcome')
        
    def test_string_rpartition(self):
        test_class_strings_methods.test_string_rpartition("Hello, And Welcome To My World!",'Welcome')
        
    def test_string_rsplit(self):
        test_class_strings_methods.test_string_rsplit("Hello, And Welcome To My World!",'Welcome')
        
    def test_string_rstrip(self):   
        test_class_strings_methods.test_string_rstrip("Hello, And Welcome To My World!")

class Test_tuple_methods(unittest.TestCase):
    
    def test_find_the_count_in_a_tuple(self):
        test_class_tuple_methods.test_find_the_count_in_a_tuple(tup=(1, 3, 7, 8, 7, 5, 4, 6, 8, 5), value=5)
        
    def test_find_the_index_in_a_tuple(self):
        test_class_tuple_methods.test_find_the_index_in_a_tuple(tup=(1, 3, 7, 8, 7, 5, 4, 6, 8, 5))
        
class Test_tuple_functions(unittest.TestCase):
    
    def test_class_tuple_methods(self):
        test_class_tuple_methods.test_tuple_methods()
        
    def test_length_of_a_tuple(self):
        test_class_tuple_methods.test_length_of_a_tuple(tup=(1, 3, 7, 8, 7, 5, 4, 6, 8, 5))
        
    def test_concatenate_two_tuple(self):
        test_class_tuple_methods.test_concatenate_two_tuple(tup1=(1,2,3), tup2=(4,5,6))
        
    def test_accessing_element_in_a_tuple(self):
        test_class_tuple_methods.test_accessing_element_in_a_tuple(tup=(1,2,3,4,5), index=1)
        
    def test_count_the_occurance_in_a_tuple(self):
        test_class_tuple_methods.test_count_the_occurance_in_a_tuple(tup=(1,2,3,4,5,1,2,2), value=2)
        
    def test_element_exist_or_not_in_a_tuple(self):
        test_class_tuple_methods.test_element_exist_or_not_in_a_tuple(tup=('hello, helloworld'))
        
    def test_convert_tuple_to_string(self):
        test_class_tuple_methods.test_convert_tuple_to_string(tup=(1,2,3,4,5))
        
    def test_remove_the_duplicates_in_a_tuple(self):
        test_class_tuple_methods.test_remove_the_duplicates_in_a_tuple(tup=(1,2,3,1,2,3,4,5))
        
    def test_find_the_index_of_an_element_in_a_tuple(self):
        test_class_tuple_methods.test_find_the_index_of_an_element_in_a_tuple(tup=(1,2,3,4,5),value=3)
        
    def test_list_to_tuple(self):
        test_class_tuple_methods.test_list_to_tuple(list1=[1,2,3,4,5])
        
    def test_iterate_through_for_loop_in_a_tuple(self):
        test_class_tuple_methods.test_iterate_through_for_loop_in_a_tuple(tup=(10,20,30,40,50))
        
    def test_minimum_and_maximum_element_single_tuple(self):
        test_class_tuple_methods.test_minimum_and_maximum_element_single_tuple(tup=(10,20,30,40,50))
        
    def test_tuple_of_strings_to_single_tuple(self):
        test_class_tuple_methods.test_tuple_of_strings_to_single_tuple(tup=('h','e','l','l','o'))
        
    def test_common_elements_in_tuple(self):
        test_class_tuple_methods.test_common_elements_in_tuple(tup1=(1,2,3,4), tup2=(1,2,3))
        
    def test_sorted_tuple(self):
        test_class_tuple_methods.test_sorted_tuple(tup=(10,1,3,2,100,10,40,60))
        
    def test_sum_of_all_items_in_tuple(self):
        test_class_tuple_methods.test_sum_of_all_items_in_tuple(tup=(1,2,3,4,5))
        
    def test_merge_two_tuples_remove_duplicates(self):
        test_class_tuple_methods.test_merge_two_tuples_remove_duplicates((1,2,3,4,5,6), (1,2,3,4))
        
    def test_first_last_element(self):
        test_class_tuple_methods.test_first_last_element(tup=(10,20,30,40,50))
        
    def test_tuple_of_integers_to_a_tuple_of_strings(self):
        test_class_tuple_methods.test_tuple_of_integers_to_a_tuple_of_strings(tup=(1,2,3,4,5))
        
    def test_tuple_even_odd(self):
        test_class_tuple_methods.test_tuple_even_odd(tup=(1,2,3,4,5,6,7,8,9,10))
        
    def test_get_product_of_all_items_in_a_tuple(self):
        test_class_tuple_methods.test_get_product_of_all_items_in_a_tuple(tup=(1,2,3,4,5))
        
    def test_frequency_of_items_in_a_tuple(self):
        test_class_tuple_methods.test_frequency_of_items_in_a_tuple(tup=(1,2,3,1,2,3,4,5))
        
    def test_remove_the_duplicate_in_a_tuple(self):
        test_class_tuple_methods.test_remove_the_duplicate_in_a_tuple(tup=(1,2,3,4,5,3), value=3)
        
    def test_tuple_difference(self):
        test_class_tuple_methods.test_tuple_difference(tup1=(1,2,3,4,5), tup2=(1,2,3))
        
    def test_second_largest_value_in_a_tuple(self):
        test_class_tuple_methods.test_second_largest_value_in_a_tuple(tup=(20,10,3,4,5,6,7))
        
    def text_split_tuple_into_equal_parts(self):
        test_class_tuple_methods.text_split_tuple_into_equal_parts(tup=(1,2,3,4,5,6), n=2)

class Test_list_methods(unittest.TestCase):
    
    def test_list_append(self):
        test_class_list_methods.test_list_append(list1=['apple', 'banana', 'cherry'])
        
    def test_list_clear(self):
        test_class_list_methods.test_list_clear(list1=['apple', 'banana', 'cherry'])
        
    def test_list_copy(self):
        test_class_list_methods.test_list_copy(list1=['apple', 'banana', 'cherry'])
        
    def test_list_count(self):
        test_class_list_methods.test_list_count(list1=['apple', 'banana', 'cherry'],value="apple")
        
    def test_list_extend(self):
        test_class_list_methods.test_list_extend(list1=['apple', 'banana', 'cherry'],list2=['Ford', 'BMW', 'Volvo'])
        
    def test_list_index(self):
        test_class_list_methods.test_list_index(list1=['apple', 'banana', 'cherry'])
    
    def test_list_insert(self):
        test_class_list_methods.test_list_insert(list1=['apple', 'banana', 'cherry'],index=1, value="orange")
        
    def test_list_pop(self):
        test_class_list_methods.test_list_pop(list1=['apple', 'banana', 'cherry'],index=1)
    
    def test_list_remove(self):
        test_class_list_methods.test_list_remove(list1=['apple', 'banana', 'cherry'],value="banana")
    
    def test_list_reverse(self):
        test_class_list_methods.test_list_reverse(list1=['apple', 'banana', 'cherry'])
        
    def test_list_sort(self):
        test_class_list_methods.test_list_sort(list1=['Ford', 'BMW', 'Volvo'])
    
class Test_set_methods(unittest.TestCase):
    
    def test_set_type(self):
        test_class_set_methods.test_set_type({"apple", "banana", "cherry"},{"google", "microsoft", "apple"})
        
    def test_set_add(self):
        test_class_set_methods.test_set_add({"apple", "banana", "cherry"}, val='Orange')
        
    def test_set_copy(self):
        test_class_set_methods.test_set_copy({"apple", "banana", "cherry"})
        
    def test_set_difference(self):
        test_class_set_methods.test_set_difference({"apple", "banana", "cherry"},{"google", "microsoft", "apple"})
        
    def test_set_difference_update(self):
        test_class_set_methods.test_set_difference_update({"apple", "banana", "cherry"},{"google", "microsoft", "apple"})
        
    def test_set_intersection(self):
        test_class_set_methods.test_set_intersection({"apple", "banana", "cherry"},{"google", "microsoft", "apple"})
        
    def test_set_intersection_update(self):
        test_class_set_methods.test_set_intersection_update({"apple", "banana", "cherry"},{"google", "microsoft", "apple"})
        
    def test_set_isdisjoint(self):
        test_class_set_methods.test_set_isdisjoint({"apple", "banana", "cherry"},{"google", "microsoft", "apple"})
        
    def test_set_issubset(self):
        test_class_set_methods.test_set_issubset({"apple", "banana", "cherry"},{"google", "microsoft", "apple"})
        
    def test_set_issuperset(self):
        test_class_set_methods.test_set_issuperset({"apple", "banana", "cherry"},{"google", "microsoft", "apple"})
        
    def test_set_pop(self):
        test_class_set_methods.test_set_pop({"apple", "banana", "cherry"},{"google", "microsoft", "apple"})
        
    def test_set_symmetric_difference(self):
        test_class_set_methods.test_set_symmetric_difference({"apple", "banana", "cherry"},{"google", "microsoft", "apple"})
        
    def test_set_symmetric_difference_update(self):
        test_class_set_methods.test_set_symmetric_difference_update({"apple", "banana", "cherry"},{"google", "microsoft", "apple"})
        
    def test_set_union(self):
        test_class_set_methods.test_set_union({"apple", "banana", "cherry"},{"google", "microsoft", "apple"})
        
    def test_set_remove(self):
        test_class_set_methods.test_set_remove({"apple", "banana", "cherry"}, value="banana")
        
    def test_set_length(self):
        test_class_set_methods.test_set_length({"apple", "banana", "cherry"},{"google", "microsoft", "apple"})
        
    def test_set_clear(self):
        test_class_set_methods.test_set_clear({"apple", "banana", "cherry"})
        
    def test_set_discard(self):
        test_class_set_methods.test_set_discard({"apple", "banana", "cherry"},value="banana")
        
    def test_set_update(self):
        test_class_set_methods.test_set_update({"apple", "banana", "cherry"},{"google", "microsoft", "apple"})
        
    def test_frozenset(self):
        test_class_set_methods.test_frozenset()
        
class Test_dictionary_methods(unittest.TestCase):
    
    def test_create_dictionary(self):
        test_dictionary_methods.test_create_dictionary()
        
    def test_length_dictionary(self):
        test_dictionary_methods.test_length_dictionary()
        
    def test_dictionary_with_different_datatypes(self):
        test_dictionary_methods.test_dictionary_with_different_datatypes()
        
    def test_dictionary_constructor_method(self):
        test_dictionary_methods.test_dictionary_constructor_method()
        
    def test_dictionary_accessing_elements(self):
        test_dictionary_methods.test_dictionary_accessing_elements()
        
    def test_dictionary_get(self):
        test_dictionary_methods.test_dictionary_get()
        
    def test_dictionary_keys(self):
        test_dictionary_methods.test_dictionary_keys()
        
    def test_dictionary_add_new_item(self):
        test_dictionary_methods.test_dictionary_add_new_item()
        
    def test_dictionary_values(self):
        test_dictionary_methods.test_dictionary_values()
        
    def test_dictionary_items(self):
        test_dictionary_methods.test_dictionary_items()
        
    def test_dictionary_key_exists(self):
        test_dictionary_methods.test_dictionary_key_exists()
        
    def test_dictionary_update(self):
        test_dictionary_methods.test_dictionary_update()
        
    def test_dictionary_pop(self):
        test_dictionary_methods.test_dictionary_pop()
        
    def test_dictionary_del(self):
        test_dictionary_methods.test_dictionary_del()
        
    def test_dictionary_clear(self):
        test_dictionary_methods.test_dictionary_clear()
        
    def test_dictionary_forloop(self):
        test_dictionary_methods.test_dictionary_forloop()
        
    def test_dictionary_copy(self):
        test_dictionary_methods.test_dictionary_copy()
        
    def test_nested_dictionary(self):
        test_dictionary_methods.test_nested_dictionary()
        
    def test_nested_dictionary_forloop(self):
        test_dictionary_methods.test_nested_dictionary_forloop()
        
    def test_dictionary_fromkeys(self):
        test_dictionary_methods.test_dictionary_fromkeys()
        
    def test_dictionary_popitem(self):
        test_dictionary_methods.test_dictionary_popitem()
   
class Test_for_loop(unittest.TestCase):
    
    def test_string(self):
        for_loop.test_string("helloworld")
        
    def test_list(self):
        for_loop.test_list([1,4,2,3,5,6,7,9,8,100])
        
    def test_tuple(self):
        for_loop.test_tuple((1,3,2,4,'hello'))
        
    def test_dict(self):
        for_loop.test_dict({'a':1,'b':2,'c':3,'d':4})
        
    def test_set(self):
        for_loop.test_set({'a','b','c'})

class Test_while_loop(unittest.TestCase):
    
    def test_while_loop_break(self):
        test_loop.test_while_loop_break(1)
        
    def test_while_loop_continue(self):
        test_loop.test_while_loop_continue(1)
        
    def test_while_loop_else(self):
        test_loop.test_while_loop_else(1)
 
class Test_Functions(unittest.TestCase):
    
    def test_func_with_positional_argument(self):
        func.test_greet("Anamika", "Prakash")
        
    def test_func_with_default_argument(self):
        func.test_get_greeting_one_default_argument(name="Anamika")
        
    def test_func_with_posiitonal_default_argument(self):
        func.test_addition_of_two_numbers_with_default_argument_keyword_argument(10, second_value=1)
        
    def test_func_with_variable_no_of_positional_arguments(self):
        func.test_variable_length_arguments("hello", None, 10, 4.5,(1,2,3), [1,2,5], {'a':1,'b':2},{'A','B'})
        
    def test_func_with_variable_no_of_keyword_arguments(self):  
        func.test_variable_keyword_arguments_multiplication(1, [1,2,3,4,5])
        
    def test_func_with_variable_no_of_keyword_arguments1(self):
        value = func.test_variable_keyword_arguments(c = 7, d = 8, e= 'hello')
        print(f"variable arguments: {value}")
     
    def test_func_with_no_arguments(self):
        func.test_no_arguments()
    
    def test_func_with_only_positional_arguments(self):
        func.test_positional_only(10,5)
        
    def test_func_with_only_keyword_arguments(self):
        func.test_keyword_only(c = 7, d = 8)
        
    def test_func_with_positional_arguments(self):
        func.test_my_function(5, 6, c = 7, d = 8)
        

       
        
style = """
    .heading {
    margin-top: 0ex;
    margin-bottom: 1ex;
    border-style:ridge;
    color:white;
    #background-color:#999900;
    background-color:#1E90FF;
    font-weight:bold;
    }
"""
script = """
    Your script
"""
def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(Test_Comments))
    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(Test_indentation))
    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(Test_variables))
    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(Test_numbers))
    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(Test_Operators))
    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(Test_data_types))
    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(Test_string_functions))
    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(Test_string_methods))
    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(Test_tuple_functions))
    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(Test_tuple_methods))
    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(Test_list_methods))
    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(Test_List_Functions))
    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(Test_set_methods))
    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(Test_dictionary_methods))
    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(Test_for_loop))
    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(Test_while_loop))
    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(Test_Functions))
    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(Test_UserDefinedFunctions))
    
    #suite.addTest(unittest.TestLoader().loadTestsFromTestCase(EditAddressTest))
    #suite.addTest(unittest.TestLoader().loadTestsFromTestCase(CreatePostTest))
    runner = HTMLTestRunner(log=True, verbosity=2, output='report', title='Python Automation UnitTest Test report', report_name='report',
                        open_in_browser=True, description="Python UnitTest Automation", tested_by="Prakash Perumal",
                        add_traceback=False,script=script,style=style)
    runner.run(suite)

if __name__ == '__main__':
    suite()