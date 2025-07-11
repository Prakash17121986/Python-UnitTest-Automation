

# Access specifier in Python

# Public
# Private
# Protected
# Publicly available attributes and methods can be accessible outside of class and inside of class
# Protectd available attributes and methods can use within the class and child class also can use if it is derived
# Private available attributes and methods can use only inside the class

class Student:

    def __init__(self, name, rollno, age):
        self.name = name # public instance variable
        self._rollno = rollno # protected instance variable
        self.__age = age

    def get_age(self):
        return self.__age
    

    def set_age(self, age):
        if self.__age > 35:
            print("Invalid Age given.. Age should be less than 35")
        else:
            self.__age = age

    '''
    def __display(self):
        print(f"Hi myself {self.name} with rollno {self._rollno} from Student class")
        print("age", self.__age)

    def display_PrivateData(self):
        self.__display()

class Branch(Student):
    pass
    '''
obj = Student("Rahul",22, 20)
print(obj)
print(obj.get_age())
obj.set_age(34)
print(obj.get_age())
'''
print(dir(obj))
print(obj.name)
print(obj._rollno)
print(obj._Student__age)
obj.display_PrivateData()

def showData():
    obj1 = Branch("Rahul",22, 20)
    print(obj1)
    print(obj1.name)
    print(obj1._rollno)
    obj1.display_PrivateData()

showData()
'''
    #  PS C:\Users\Anamika\Python_codes> & C:/Users/Anamika/AppData/Local/Programs/Python/Python310/python.exe c:/Users/Anamika/Python_codes/Project/tests/all_tests/Advanced_Python/test_class_getter_setter.py
    # <__main__.Student object at 0x000002A212A9BB80>
    # 20
    # 34
    # PS C:\Users\Anamika\Python_codes> 