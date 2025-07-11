import unittest
"""
Attributes
----------
    # Name, class, subjects, marks, etc., of student
    # Name, designation, department, salary, etc., of employee
    # Invoice number, customer, product code and name, price and quantity, etc., in an invoice
    # Registration number, owner, company, brand, horsepower, speed, etc., of car
    # Each attribute will have a value associated with it. Attribute is equivalent to data.

Behavior
--------
    # Processing attributes associated with an object.
    # Compute percentage of student's marks
    # Calculate incentives payable to employee
    # Apply GST to invoice value
    # Measure speed of car

The most important feature of object-oriented approach is defining attributes and their functionality as a single unit called class.
It serves as a blueprint for all objects having similar attributes and behavior.

In OOP, class defines what are the attributes its object has, and how is its behavior.
Object, on the other hand, is an instance of the class.

Principles of OOPs Concepts
---------------------------
    # Object-oriented programming paradigm is characterized by the following principles −
    # Class
    # Object
    # Abstraction
    # Encapsulation
    # Inheritance
    # Polymorphism

class
# a set of attributes that characterize any object of the class
# The attributes are data members (class variables and instance variables) and methods, accessed via dot notation.

object
# An object refers to an instance of a certain class.
# An object comprises both data members (class variables and instance variables) and methods.
# Each object has its own attributes and methods, which are defined by its class.

        self.args = args
        self.processor = processor
        self.motherboard = motherboard
        self.memory = memory
        self.keyboard = keyboard
        self.mouse = mouse
        self.hba_card = hba_card
        self.case = case
        self.cpu_fan = cpu_fan
        self.usb_drive = usb_drive
        self.hdd_drive = hdd_drive
        self.ssd_drive = ssd_drive
        self.nvme_drive = nvme_drive
        self.backplane_board = backplane_board
        self.nic_card = nic_card
        self.cpld_version = cpld_version
        self.bios_version = bios_version
        self.raid = raid_version
        self.idrac_version = idrac_version

"""

# defining a class
class Smartphone(unittest.TestCase):
    'class documentation string'
    # class_suite - It consists of all the components statements defining class members, data attributes and functions.
    # The class has a documentation string, which can be accessed via ClassName.__doc__

    # constructor
    def __init__(self, device, brand):
        self.device = device
        self.brand = brand

    # method of class
    def description(self):
        return f"{self.device} of {self.brand} supports Android 14 version"

# # creating subject of the class
# phone_obj = Smartphone("Smartphone", "Samsung")
# print(phone_obj)
# print(phone_obj.description())

# if __name__=='__main__':
#     # creating subject of the class
#     phone_obj = Smartphone("Smartphone", "Samsung")
#     #print("phone_obj", phone_obj)
#     #print(phone_obj)
#     print("object is created for Class SmartPhone")
#     print("SmartPhone Instance Method called")
#     print("Device", phone_obj.device)
#     print("Brand", phone_obj.brand)
#     print(phone_obj.description())

# ---------------Output ---------------------------
# C:\Users\Anamika\PycharmProjects\PythonProject\.venv\Scripts\python.exe C:\Users\Anamika\PycharmProjects\PythonProject\Python_Project\Advanced_Python\test_class.py
# <__main__.Smartphone object at 0x000001C7F3CCF350>
# Smartphone of Samsung supports Android 14 version
#
# Process finished with exit code 0
# ----------------- ---------------------------

class Employee(unittest.TestCase):
    'Common base class for all employees'
    empCount = 0
    __secretCount = 0
    # class constructor or initialization method that python calls when you create a new instance of this class
    def __init__(self, name, salary):
        # first argument to each method is self
        self.name = name
        self.salary = salary
        Employee.empCount+=1

    def displayCount(self):
        print("Total Employee %d"%(Employee.empCount))

    def displayEmployee(self):
        print("Name: ", self.name, ", Salary:", self.salary)

    def __del__(self):
        class_name = self.__class__.__name__
        print(class_name, "destroyed")

# if __name__=='__main__':
#     # Object instantiation
#     emp1 = Employee("Zara", 2000)
#     emp2 = Employee("Manni", 5000)
#     #Accessing method
#     print("Name & Salary for Employee1", emp1.displayEmployee())
#     # it returns the value of name and salary  attribute
#     print("Name & Salary for Employee1", emp2.displayEmployee())
#     print("Total Employee %d" % Employee.empCount)
# #     emp1.age = 7
# #     emp2.age = 8
# #     del emp1.age
# #     print(getattr(emp1, 'name'))#− to access the attribute of object.
# #     print(hasattr(emp1,'name')) #− to check if an attribute exists or not.
# #     print(setattr(emp1,'City', 'Chennai')) #− to set an attribute. If attribute does not exist, then it would be created.
# #     print(delattr(emp1, 'name')) #− to delete an attribute.
#     print ("Employee.__doc__:", Employee.__doc__)
#     print ("Employee.__name__:", Employee.__name__)
#     print ("Employee.__module__:", Employee.__module__)
#     print ("Employee.__module__:", emp1.__secretCount)
    
    
