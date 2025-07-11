class test_baseclass():
    # __init__() function is a constructor method in Python 
    # It initializes the object’s state when the object is created. If the child class does not define its own __init__() method, it will automatically inherit the one from the parent class.
    #__init__ method in Emp calls super().__init__(name, id) to invoke the constructor of the Person class and initialize the inherited attributes.
    def __init__(self, title, instructor):
        self.title = title
        self.instructor = instructor

    def test_enroll_students(self,student_name):
        self.students_list = []
        self.students_list.append(student_name)
        return self.title, self.instructor, self.students_list

obj = test_baseclass("Advanced Python Programming", "Anamika")
print("obj", obj)
print(obj.test_enroll_students("Deepa"))


# 1. Single Inheritance
class Person:
    def __init__(self, name):
        self.name = name

class Employee(Person):  # Employee inherits from Person
    def __init__(self, name, salary):
        super().__init__(name)
        self.salary = salary

# 2. Multiple Inheritance
class Job:
    def __init__(self, salary):
        self.salary = salary

class EmployeePersonJob(Employee, Job):  # Inherits from both Employee and Job
    def __init__(self, name, salary):
        Employee.__init__(self, name, salary)  # Initialize Employee
        Job.__init__(self, salary)            # Initialize Job

# 3. Multilevel Inheritance
class Manager(EmployeePersonJob):  # Inherits from EmployeePersonJob
    def __init__(self, name, salary, department):
        EmployeePersonJob.__init__(self, name, salary)  # Explicitly initialize EmployeePersonJob
        self.department = department

# 4. Hierarchical Inheritance
class AssistantManager(EmployeePersonJob):  # Inherits from EmployeePersonJob
    def __init__(self, name, salary, team_size):
        EmployeePersonJob.__init__(self, name, salary)  # Explicitly initialize EmployeePersonJob
        self.team_size = team_size

# 5. Hybrid Inheritance (Multiple + Multilevel)
class SeniorManager(Manager, AssistantManager):  # Inherits from both Manager and AssistantManager
    def __init__(self, name, salary, department, team_size):
        Manager.__init__(self, name, salary, department)        # Initialize Manager
        AssistantManager.__init__(self, name, salary, team_size)  # Initialize AssistantManager

# Creating objects to show inheritance

# Single Inheritance
emp = Employee("John", 40000)
print(emp.name, emp.salary)

# Multiple Inheritance
emp2 = EmployeePersonJob("Alice", 50000)
print(emp2.name, emp2.salary)

# Multilevel Inheritance
mgr = Manager("Bob", 60000, "HR")
print(mgr.name, mgr.salary, mgr.department)

# Hierarchical Inheritance
asst_mgr = AssistantManager("Charlie", 45000, 10)
print(asst_mgr.name, asst_mgr.salary, asst_mgr.team_size)

# Hybrid Inheritance
sen_mgr = SeniorManager("David", 70000, "Finance", 20)
print(sen_mgr.name, sen_mgr.salary, sen_mgr.department, sen_mgr.team_size)


# ==================Program Output=================================
# PS C:\Users\Anamika\Python_codes> & C:/Users/Anamika/AppData/Local/Programs/Python/Python310/python.exe c:/Users/Anamika/Python_codes/Project/tests/all_tests/Advanced_Python/test_class_inheritance.py
# obj <__main__.test_baseclass object at 0x000001E73CA5BFD0>
# ('Advanced Python Programming', 'Anamika', ['Deepa'])
# John 40000
# Alice 50000
# Bob 60000 HR
# Charlie 45000 10
# David 70000 Finance 20
# PS C:\Users\Anamika\Python_codes> 