# Access Modifiers

# Using .sysmbol in python we determine the level of access for a data member of the class
# Public access modifier
# Private access modifier
# Protected access modifier

# Public Access Modifier
# Member of the class marked as public can be accessed from anywhere withour main program

# class Person():
  
#     #constructor
#     def __init__(self, name, age, gender, country):
#         # the below attributes are public and can be accessed within or outside class
#         self.name = name
#         self.age = age
#         self.gender = gender
#         self.country = country
    
#     # Public method
#     def print_person_details(self):
#         print("Name of the person ", self.name)
#         print("Age of the person ", self.age)
#         print("Gender of the person", self.gender)
#         print("Country of the person", self.country)

# # Private access modifier - Members of the class that are marked orivate are accessible from within the class only
#     def __print_person_details(self):
#         print("Name of the person ", self.name)
#         print("Age of the person ", self.age)
#         print("Gender of the person", self.gender)
#         print("Country of the person", self.country)


# #creating an instance of the Person class
# person_obj = Person("Alex", 21, "Male", "UK")
# print(person_obj)

# # Accessing the public properties or attributes using method name - print_person_details
# person_obj.print_person_details()

# # Accessing the public properties or attributes without method
# print("Name of the person is ", person_obj.name)
# print("Age of the person is ", person_obj.age)
# print("Gender of the person is ", person_obj.gender)
# print("Country of the person is ", person_obj.country)



# class PrviatePerson():
#     #setting up private variables
#     __name = None
#     __age = None
#     __gender = None
#     __country = None

#     #constructor
#     def __init__(self, name, age, gender, country):
#         # the below attributes are public and can be accessed within or outside class
#         self.__name = name
#         self.__age = age
#         self.__gender = gender
#         self.__country = country
    
#     # Private method
#     def __log_person_details(self):
#         print("Name of the person ", self.__name)
#         print("Age of the person ", self.__age)
#         print("Gender of the person", self.__gender)
#         print("Country of the person", self.__country)

#     # Public Method
#     def print_person_details(self):
#         self.__log_person_details()

# # #creating an instance of the Person class
# privateperson_obj = PrviatePerson("James", 32, "Male", "Brazil")
# print(privateperson_obj)

# # Accessing the public properties or attributes using method name - print_person_details
# privateperson_obj.print_person_details()

# Accessing the public properties or attributes without method or outside the class - Protected or not have access
# print("Name of the person is ", privateperson_obj.__name)
# print("Age of the person is ", privateperson_obj.__age)
# print("Gender of the person is ", privateperson_obj.__gender)
# print("Country of the person is ", privateperson_obj.__country)


# Protected Access Modifier
# Member which can only be accessed by the derived class of the base class in which they were defined.

class baseclass():
    #setting up protected variables
    _name = None
    _age = None
    _gender = None
    _country = None

    #constructor
    def __init__(self, name, age, gender, country):
        # the below attributes are public and can be accessed within or outside class
        self._name = name
        self._age = age
        self._gender = gender
        self._country = country

    # Protected method
    def _log_person_details(self):
        print("Name of the person ", self._name)
        print("Age of the person ", self._age)
        print("Gender of the person", self._gender)
        print("Country of the person", self._country)


class Developer(baseclass):
    def __init__(self, name, age, gender, country, salary, company, isjunior):
        baseclass.__init__(self, name, age, gender, country)
        self.salary = salary
        self.company = company
        self.isjunior = isjunior

    def print_developer_details(self):
        self._log_person_details()
        print("Developer's salary", self.salary)
        print("Developer's company", self.company)
        print("Developer's isjunior", self.isjunior)

# creating an instance of the Person class
Developer_obj = Developer("James", 32, "Male", "Brazil", 10000, "HCL", "Junior")
print(Developer_obj)

Developer_obj.print_developer_details()




# -----------------------------Program Output----------------------------------------------
# PS C:\Users\Anamika\Python_codes> & C:/Users/Anamika/AppData/Local/Programs/Python/Python310/python.exe c:/Users/Anamika/Python_codes/Project/tests/all_tests/Advanced_Python/test_access_modifier.py
# <__main__.Person object at 0x0000025EF0DABC10>
# Name of the person  Alex
# Age of the person  21
# Gender of the person Male
# Country of the person UK
# Name of the person is  Alex
# Age of the person is  21
# Gender of the person is  Male
# Country of the person is  UK

# PS C:\Users\Anamika\Python_codes> & C:/Users/Anamika/AppData/Local/Programs/Python/Python310/python.exe c:/Users/Anamika/Python_codes/Project/tests/all_tests/Advanced_Python/test_access_modifier.py
# <__main__.PrviatePerson object at 0x00000210ADDABCA0>
# Name of the person  Alex
# Age of the person  21
# Gender of the person Male
# Country of the person UK
# Traceback (most recent call last):
#   File "c:\Users\Anamika\Python_codes\Project\tests\all_tests\Advanced_Python\test_access_modifier.py", line 82, in <module>
#     print("Name of the person is ", privateperson_obj.__name)
# AttributeError: 'PrviatePerson' object has no attribute '__name'

# PS C:\Users\Anamika\Python_codes> & C:/Users/Anamika/AppData/Local/Programs/Python/Python310/python.exe c:/Users/Anamika/Python_codes/Project/tests/all_tests/Advanced_Python/test_access_modifier.py
# <__main__.PrviatePerson object at 0x0000021190D3BCA0>
# Name of the person  James
# Age of the person  32
# Gender of the person Male
# Country of the person Brazil
# Traceback (most recent call last):
#   File "c:\Users\Anamika\Python_codes\Project\tests\all_tests\Advanced_Python\test_access_modifier.py", line 85, in <module>
#     print("Name of the person is ", privateperson_obj.__name)
# AttributeError: 'PrviatePerson' object has no attribute '__name'

# -----------------------------Program Output----------------------------------------------
# PS C:\Users\Anamika\Python_codes>
# PS C:\Users\Anamika\Python_codes> & C:/Users/Anamika/AppData/Local/Programs/Python/Python310/python.exe c:/Users/Anamika/Python_codes/Project/tests/all_tests/Advanced_Python/test_access_modifier.py
# <__main__.PrviatePerson object at 0x000001EB5DCABC70>
# Name of the person  James
# Age of the person  32
# Gender of the person Male
# Country of the person Brazil
# PS C:\Users\Anamika\Python_codes>

# -----------------------------Program Output----------------------------------------------
# PS C:\Users\Anamika\Python_codes> & C:/Users/Anamika/AppData/Local/Programs/Python/Python310/python.exe c:/Users/Anamika/Python_codes/Project/tests/all_tests/Advanced_Python/test_access_modifier.py
# <__main__.Developer object at 0x000001E225F8BC70>
# Name of the person  James
# Age of the person  32
# Gender of the person Male
# Country of the person Brazil
# Developer's salary 10000
# Developer's company HCL
# Developer's isjunior Junior
# PS C:\Users\Anamika\Python_codes>

