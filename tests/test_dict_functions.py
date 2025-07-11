
import unittest

class test_dict_functions(unittest.TestCase):
    
    def test_Multiplication_of_number(self, d={}):
        self.d  = d
        n=2
        d = dict()
        print(f"dict: {d}")
        for x in range(1,n+1):
            d[x]=x*x
            print("Multiplication of number 1 to 5", d) 

    #Write a Python program to sum all the items in a dictionary.
    def test_sum_of_all_numbers(self, sum=0, my_dict={}):
        my_dict = {'data1':100,'data2':-54,'data3':247}
        print(f"dict: {my_dict}")
        sum=0
        for i in my_dict:
            sum+=my_dict[i]
            print("sum of all number 1 to 5", sum)

    def test_list_of_keys_by_value_method(self, reverse={}, my_dict={}):
        self.my_dict = my_dict
        self.reverse = reverse
        my_dict = {'A':1,'B':3,'C':3,'D':4,'E':1,'F':3}
        print(f"dict: {my_dict}")
        reverse = {}
        for key, value in my_dict.items():
            if value in reverse:
                reverse[value].append(key) # list of keys in list by using value method, val: [key1, key2]
            else:
                reverse[value] = [key]
        print("list of keys in list by using value method, val: [key1, key2]",reverse)
        return reverse

    def test_filtering_keys_are_even(self, newDict={}, my_dict={}, sorted_value = {}):
            '''
            dictOfNames = {7 : 'sami',8: 'jana',9: 'rami',10: 'rana',11 : 'reem', 12 : 'salma'}
            Suppose we want to filter above dictionary by keeping only elements
            whose keys are even. For that we can just iterate over all the items of
            dictionary and add elements with even key to an another dictionary
            '''
            self.newDict = {}
            self.mydict = {}
            print(f"dict: {my_dict}")
            self.sorted_value = {}
            newDict = dict()
            sorted_value = {key:value for (key,value) in my_dict.items() if key % 2 == 0}
            print("Sorted value", sorted_value)
            for (key, value) in my_dict.items():
                if key % 2 == 0:
                    newDict[key] = value
            print("filtering keys are even",newDict)
            return newDict

    def test_dict_after_dropping_empty_items(self, dict1):
            self.dict1 = dict1
            # Write a Python program to drop empty Items from a given Dictionary.
            dict1 = {'c1': 'Red', 'c2': 'Green', 'c3':None}
            print(f"dict: {dict1}")
            dict1 = {key:value for (key, value) in dict1.items() if value is not None}
            print("New Dictionary after dropping empty items", dict1)

    def test_dict_filter_function(self, marks={}):
            # Write a Python program to filter a dictionary based on marks greater than 70.
            self.marks = marks
            marks = {'1': 75, '2': 80, '3': 65,'4': 90}
            print(f"dict: {marks}")
 
            print("Marks greater than 70:")
            result = {key:value for (key, value) in marks.items() if value > 70}
            print("Marks greater than 70:", result)

    def test_dict_print_function(self):
            age = 23
            name = "Tim"
            print("Hello world", end=" | ")
            print("I am", name)
            print(f"My name is", {name}, "My age is", {age}, sep=",")


# if __name__ == '__main__':
#     obj = test_diff_dict_functions()
#     obj.test_dict_functions1(n=2, d={})
#     obj.test_dict_functions2(sum=0, my_dict = {'data1':100,'data2':-54,'data3':247})
#     obj.test_dict_functions3(reverse={}, my_dict={'A':1,'B':3,'C':3,'D':4,'E':1,'F':3})
#     obj.test_dict_functions4(newDict={}, my_dict={7 : 'sami',8: 'jana',9: 'rami',10: 'rana',11 : 'reem', 12 : 'salma'}, sorted_value = {})
#     obj.test_dict_functions5({'c1': 'Red', 'c2': 'Green', 'c3':None})
#     obj.test_dict_functions6({'1': 75, '2': 80, '3': 65,'4': 90})
#     obj.test_dict_functions7()
#     unittest.main()

    # ------------------------Program Output----------------------------------------------
    # PS C:\Users\Anamika\Python_codes> & C:/Users/Anamika/AppData/Local/Programs/Python/Python310/python.exe c:/Users/Anamika/Python_codes/Project/tests/all_tests/DSA/test_different_dict_functions.py
    # dict: {}
    # Multiplication of number 1 to 5 {1: 1}
    # Multiplication of number 1 to 5 {1: 1, 2: 4}
    # dict: {'data1': 100, 'data2': -54, 'data3': 247}
    # sum of all number 1 to 5 100
    # sum of all number 1 to 5 46
    # sum of all number 1 to 5 293
    # dict: {'A': 1, 'B': 3, 'C': 3, 'D': 4, 'E': 1, 'F': 3}
    # list of keys in list by using value method, val: [key1, key2] {1: ['A', 'E'], 3: ['B', 'C', 'F'], 4: ['D']}
    # dict: {7: 'sami', 8: 'jana', 9: 'rami', 10: 'rana', 11: 'reem', 12: 'salma'}
    # Sorted value {8: 'jana', 10: 'rana', 12: 'salma'}
    # filtering keys are even {8: 'jana', 10: 'rana', 12: 'salma'}
    # dict: {'c1': 'Red', 'c2': 'Green', 'c3': None}
    # New Dictionary after dropping empty items {'c1': 'Red', 'c2': 'Green'}
    # dict: {'1': 75, '2': 80, '3': 65, '4': 90}
    # Marks greater than 70:
    # Marks greater than 70: {'1': 75, '2': 80, '4': 90}
    # Hello world | I am Tim
    # My name is,{'Tim'},My age is,{23}

    # ----------------------------------------------------------------------
    # Ran 0 tests in 0.000s

    # OK
    # PS C:\Users\Anamika\Python_codes> 