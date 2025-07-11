

# Access specifier in Python

# Public
# Private
# Protected
# Publicly available attributes and methods can be accessible outside of class and inside of class
# Protectd available attributes and methods can use within the class and child class also can use if it is derived
# Private available attributes and methods can use only inside the class

class Student:

    def __init__(self, name, rollno, age):
        self.name = name
        self._rollno = rollno
        self.__age = age

    def __display(self):
        print(f"Hi myself {self.name} with rollno {self._rollno} from Student class")
        print("age", self.__age)

    def display_PrivateData(self):
        self.__display()

class Branch(Student):
    pass

obj = Student("Rahul",22, 20)
print(obj)
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

    # PS C:\Users\Anamika\Python_codes> & C:/Users/Anamika/AppData/Local/Programs/Python/Python310/python.exe c:/Users/Anamika/Python_codes/Project/tests/all_tests/Advanced_Python/test_access_specifier.py
    # <__main__.Student object at 0x0000020C2EDDBCD0>
    # ['_Student__age', '_Student__display', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_rollno', 'display_PrivateData', 'name']
    # Rahul
    # 22
    # 20
    # Hi myself Rahul with rollno 22 from Student class
    # age 20
    # <__main__.Branch object at 0x0000020C2EDDBAC0>
    # Rahul
    # 22
    # Hi myself Rahul with rollno 22 from Student class
    # age 20
    # PS C:\Users\Anamika\Python_codes> 