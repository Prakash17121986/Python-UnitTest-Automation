import unittest

class test_for_loop(unittest.TestCase):

    def test_string(self,string_value):
        self.string_value = string_value
        print("string_value:", string_value)
        print("Using for loop to iterate the string_value")
        for i in string_value:
            print(i)

    def test_list(self, list_value):
        self.list_value = list_value
        print("list_value:", list_value)
        print("Using for loop to iterate the list_value")
        for i in range(len(list_value)):
            print(i)

    def test_tuple(self,tuple_value):
        self.tuple_value = tuple_value
        print("tuple_value:", tuple_value)
        print("Using for loop to iterate the tuple_value")
        for i in tuple_value:
            print(i)

    def test_dict(self,dict1):
        self.dict1 = dict1
        print("dict1:", dict1)
        print("Using for loop to iterate the dict1_value")
        for k, v in dict1.items():
            print(k, v)   

    def test_set(self,set1):
        self.set1 = set1
        print("set1:", set1)
        print("Using for loop to iterate the set1_value")
        for i in set1:
            print(i) 

if __name__ =='__main__':
    obj= test_for_loop()
    obj.test_string("helloworld")
    obj.test_list([1,4,2,3,5,6,7,9,8,100])
    obj.test_tuple((1,3,2,4,'hello'))
    obj.test_dict({'a':1,'b':2,'c':3,'d':4})
    obj.test_set({'a','b','c'})
    unittest.main()


    # ------------------Python Output----------------------------------------------------
    # PS C:\Users\Anamika\Python_codes> & C:/Users/Anamika/AppData/Local/Programs/Python/Python310/python.exe c:/Users/Anamika/Python_codes/Project/tests/all_tests/Python_Basics/test_for_loop.py
    # string_value: helloworld
    # Using for loop to iterate the string_value
    # h
    # e
    # l
    # l
    # o
    # w
    # o
    # r
    # l
    # d
    # list_value: [1, 4, 2, 3, 5, 6, 7, 9, 8, 100]
    # Using for loop to iterate the list_value
    # 0
    # 1
    # 2
    # 3
    # 4
    # 5
    # 6
    # 7
    # 8
    # 9
    # tuple_value: (1, 3, 2, 4, 'hello')
    # Using for loop to iterate the tuple_value
    # 1
    # 3
    # 2
    # 4
    # hello
    # dict1: {'a': 1, 'b': 2, 'c': 3, 'd': 4}
    # Using for loop to iterate the dict1_value
    # a 1
    # b 2
    # c 3
    # d 4
    # set1: {'a', 'b', 'c'}
    # Using for loop to iterate the set1_value
    # a
    # b
    # c

    # ----------------------------------------------------------------------
    # Ran 0 tests in 0.000s

    # OK
    # PS C:\Users\Anamika\Python_codes> 