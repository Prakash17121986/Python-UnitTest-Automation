
# Operators: +, -, /. //, *, **, %, 
# Operator Overloading - Beyond its capabilities
# operator is overloaded beyond its capabilities
# Result is changing based on data type mentioned for operand 1 and operand 2
# __add__, __init__

result = "hello" + "world"
print(result)

result = 1 + 2
print(result)

result = [1,2,3] + [4,5,6]
print(result)

result = len({'a':1}) + len({'b':2})
print(result)

result = 3.5 + 5.5
print(result)

result = 3.5 * 5.5
print(result)

result = 5 * 5
print(result)

# special methods
print(int.__add__(1,2))
print(str.__add__('a','b'))

class ComplexNumber():

    def __init__(self, r, i):
        self.real = r
        self.imaginary = i

    # special method to overload the value for real and complex number
    def __add__(self, other):
        return f"{self.real+other.real} + {self.imaginary+other.imaginary}i"
        #return str(self.real+other.real) + "+" + (self.imaginary.other.imaginary)

class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # greater than
    def __gt__(self, other):
        if self.age > other.age:
            return True
        else:
            return False
    
    # less than
    def __lt__(self, other):
        if self.age > other.age:
            return True
        else:
            return False
        

c1=ComplexNumber(1,2)
c2=ComplexNumber(4,5)
print(c1+c2)

p1 = Person("Ram", 35)
p2 = Person("Shyam", 23)

if p1 > p2:
    print(f"{p1.name} will pay the bill")
else:
    print(f"{p2.name} will pay the bill")

# ---------------------Program Output-----------------------------------------------
# PS C:\Users\Anamika\Python_codes> & C:/Users/Anamika/AppData/Local/Programs/Python/Python310/python.exe c:/Users/Anamika/Python_codes/Project/tests/all_tests/Advanced_Python/test_operator_overloading.py
# helloworld
# 3
# [1, 2, 3, 4, 5, 6]
# 2
# 9.0
# 19.25
# 25
# 3
# ab
# 5 + 7i
# Ram will pay the bill
# PS C:\Users\Anamika\Python_codes> 