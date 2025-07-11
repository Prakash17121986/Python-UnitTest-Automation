#*********************************************************************
# | Single Inheriance | 

# | Baseclass or Parent class |

class Person:
    # Constructor
    def __init__(self, name, id): # name, id is Instance attribute for class Animal
        self.name = name  # Initialize the name attribute
        self.id = id # Initialize the id attribute

    # To check if this person is an employee
    def Display(self):
        print(self.name, self.id)

# | Child class |

# Child class inheriting from Person
class Emp(Person):
  
  def Print(self):
    print("Emp class called")

# | Creating an instance of Person |
emp = Person("Satyam", 102)
print(emp.Display()) 


Emp_details = Emp("Mayank", 103)

# calling parent class function
Emp_details.Display()

# Calling child class function
Emp_details.Print()

# ==================Program Output=================================
# PS C:\Users\Anamika\Python_codes> & C:/Users/Anamika/AppData/Local/Programs/Python/Python310/python.exe c:/Users/Anamika/Python_codes/Project/tests/all_tests/Advanced_Python/test_class_single_inheritance.py
# Satyam 102
# None
# Mayank 103
# Emp class called
# PS C:\Users\Anamika\Python_codes> 
# ====================================================================