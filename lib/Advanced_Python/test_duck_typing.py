

class Duck():

    def swim(self):
        print("I am a duck and I can swim")

    def speaks(self):
        print("Quack quack")

class Dog():

    def swim(self):
        print("I am a dog and I can swim")

    def speaks(self):
        print("woof woof")

# to display swim method and speaks method in Duck class object or Dog class Object
def display(duck):
    duck.swim()
    duck.speaks()

duck = Duck()
display(duck)


dog = Dog()
display(dog) # only called method is defined inside the class


class Person(): # No swim method defined inside this class
    def speaks(self):
        print("blah blah blab")

# p = Person() # swim method not defined inside this Person class
# display(p) 

# Not care about class object
# it will check the class method to return the value or print the value
# if method not defined it will throw an error.


# ---------------------Program Output-----------------------------------------------
# PS C:\Users\Anamika\Python_codes> & C:/Users/Anamika/AppData/Local/Programs/Python/Python310/python.exe c:/Users/Anamika/Python_codes/Project/tests/all_tests/Advanced_Python/test_duck_typing.py
# I am a duck and I can swim
# Quack quack
# PS C:\Users\Anamika\Python_codes> 

# PS C:\Users\Anamika\Python_codes> & C:/Users/Anamika/AppData/Local/Programs/Python/Python310/python.exe c:/Users/Anamika/Python_codes/Project/tests/all_tests/Advanced_Python/test_duck_typing.py
# I am a dog and I can swim
# woof woof
# PS C:\Users\Anamika\Python_codes> 

# PS C:\Users\Anamika\Python_codes> & C:/Users/Anamika/AppData/Local/Programs/Python/Python310/python.exe c:/Users/Anamika/Python_codes/Project/tests/all_tests/Advanced_Python/test_duck_typing.py
# I am a duck and I can swim
# Quack quack
# I am a dog and I can swim
# woof woof
# PS C:\Users\Anamika\Python_codes>

# Traceback (most recent call last):
#   File "c:\Users\Anamika\Python_codes\Project\tests\all_tests\Advanced_Python\test_duck_typing.py", line 40, in <module>
#     display(p)
#   File "c:\Users\Anamika\Python_codes\Project\tests\all_tests\Advanced_Python\test_duck_typing.py", line 20, in display
#     duck.swim()
# AttributeError: 'Person' object has no attribute 'swim'
# PS C:\Users\Anamika\Python_codes> 

