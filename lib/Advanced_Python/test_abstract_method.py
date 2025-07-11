# Abstract class and Abstract Method
from abc import ABC, abstractmethod


class Vehicle(ABC):

    def __init__(self, n):
        self.no_of_tyres = n

    @abstractmethod
    # typeError: Can't instantiate abstract class Vehicle with abstract method start
    def start(self):
        pass

    #concrete method
    def display(self):
        print("Hi I am calling from Vehicle class")

#if no abstract method specified in code, then u can create a instance of object for the class.
# v = Vehicle(2)
# print(v)
# v.display()


# PS C:\Users\Anamika\Python_codes> & C:/Users/Anamika/AppData/Local/Programs/Python/Python310/python.exe c:/Users/Anamika/Python_codes/Project/tests/all_tests/Advanced_Python/test_abstract_method.py
# <__main__.Vehicle object at 0x0000022E49177D60>
# Hi I am calling from Vehicle class
# PS C:\Users\Anamika\Python_codes> & C:/Users/Anamika/AppData/Local/Programs/Python/Python310/python.exe c:/Users/Anamika/Python_codes/Project/tests/all_tests/Advanced_Python/test_abstract_method.py
# Traceback (most recent call last):
#   File "c:\Users\Anamika\Python_codes\Project\tests\all_tests\Advanced_Python\test_abstract_method.py", line 16, in <module>       
#     v = Vehicle(2)
# TypeError: Can't instantiate abstract class Vehicle with abstract method start
# PS C:\Users\Anamika\Python_codes> 