import unittest

class MyClass:
    '''
    Python is an object oriented programming language.
    Almost everything in Python is an object, with its properties and methods.
    To create a class, use the keyword class:
    In Python, __init__ is a special method, also known as a constructor,
    that's automatically called when a new instance (object) of a class is created,
    allowing you to initialize the object's attributes.
    '''

    def __init__(self, arg1, arg2):  # 'self' refers to the instance
        self.arg1 = 100
        self.arg2 = (1,2,3,4)
        

    def add(self, a, b):
        self.a = a
        self.b = b
        self.c = self.a + self.b
        print(self.c)

class Person:
    def __init__(self, name, age):
        self.name = "Prakash"
        self.age = 35

    def multiply(self, d, e):
        self.d = d
        self.e = e
        self.f = self.d * self.e
        print(self.f)

class Dog:
    def __init__(self, name, breed):
        self.name = "Bulldog"
        self.breed = "British"

# child class, inherit the class methods from another class
class Child(MyClass, Person, Dog):
    def __init__(self, a1, b1):
        self.a1 = 10
        self.b1 = 20

    def divide(self, a2, b2):
        self.a2 = a2
        self.b2 = b2
        self.c2 = self.a2 / self.b2
        print(self.c2)


if __name__ == '__main__':
    p0 = MyClass("John", [1,2,3,4]) # Creates a p0 object, object instatation, constructor method to pass the values to the argument
    print(f"('__doc__': {p0.__doc__})")
    print(f"(arg1: {p0.arg1}")
    print(f"(arg2: {p0.arg2}")
    super().__init__()
    p0.add(10,20)

    p1 = Person("John", 36) # Creates a p1 object, object instatation, constructor method to pass the values to the argument
    print(f"('Age': {p1.age}")
    print(f"('name': {p1.name}")
    p1.multiply(10,20)

    p2 = Dog("Buddy", "Golden Retriever")  # Creates a p2 object, object instatation, constructor method to pass the values to the argument
    print(f"('name': {p2.name}")  # Output: Buddy
    print(f"('breed': {p2.breed}")  # Output: Golden Retriever

    p3 = Child(10,20)
    print("Accessing through childclass")
    print(p3.a1, p3.b1)
    p3.divide(200,20)
    print(f"(arg1: {p3.arg1}")
    print(f"(arg2: {p3.arg2}")
    #print(f"('Age': {p3.age}")
    #print(f"('name': {p3.name}")
    #print(f"('name': {p3.name}")  # Output: Buddy
    #print(f"('breed': {p3.breed}")  # Output: Golden Retriever
    #print(f"Add", {p1.multiply(10,20)})

    unittest.main()