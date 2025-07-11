
list1 = [1,0,-1]
print(len(list1))

print(list1)

print(list1.__class__)

print(type(list1))

'''
__init__(self, ...): This is the constructor method, called when an object of the class is created. It initializes the object's attributes.
__str__(self): Returns a string representation of the object, intended for human readability.
__repr__(self): Returns a string representation of the object, ideally one that can be used to recreate the object.
__len__(self): Returns the length of the object, if applicable.
__getitem__(self, key): Enables indexing and allows accessing elements using [] notation.
__setitem__(self, key, value): Enables assignment to indexed elements using [] notation.
__delitem__(self, key): Enables deletion of indexed elements using del statement and [] notation.
__call__(self, ...): Allows an object to be called like a function.
Arithmetic Operators: Methods like __add__(self, other) (for +), __sub__(self, other) (for -), __mul__(self, other) (for *), etc., overload arithmetic operators.
Comparison Operators: Methods like __eq__(self, other) (for ==), __ne__(self, other) (for !=), __lt__(self, other) (for <), etc., overload comparison operators.
__enter__(self) and __exit__(self, exc_type, exc_val, exc_tb): Used for context management with the with statement.
__getattr__(self, name): Called when an attribute lookup fails.
__setattr__(self, name, value): Called when an attribute assignment is attempted.
__delattr__(self, name): Called when an attribute deletion is attempted.
'''

class Author:
    # dunder method, instance variable
    def __init__(self, name, book_name, pages) -> None:
        self.name = name
        self.book_name = book_name
        self.pages = pages

    def __len__(self):
        return self.pages
    
    # dunder method is used in operator overloading
    def __str__(self):
        return f"{self.book_name} by {self.name}"
    
    def __call__(self, *args, **kwargs):
        print("hi")

    def __getitem__(self, index):
        print(self.name, self.book_name, self.pages)

    def __del__(self):
        print("Author object has been deleted")

d = Author("Jenny", "The ocean world", 300)
print(len(d))
print(d)
d()