
class Demo:
    # Method Overloading
    # method have same name and different no of arguments
    def add(self, a, b):
        return a+b
 
    # different no of arguments with same method name
    # Method overriding not supported in Python
    #def add(self, a, b, c):
        #return a+b+c
    def add(self, a, b, c=40):
        return a+b+c
    
    def add(self, *args):
        total = 0
        for i in args:
            total = total + i
        return total

class Father:
    # Method Overriding
    # no of arguments same
    # no of same method name
    # method have same name and same no of arguments
    def sleep(self):
        print("Sleeps from 10:00 PM to 5:00 AM")
    
    def eat(self):
        print("Eating")

class Son(Father):
    def sleep(self):
        print("Sleeps from 2:00 AM to 10:00 AM")
        super().sleep()



d = Demo()
print(d.add(2,3))
#print(d.add(10,20,30))
print(d.add(10,20,30))

print(d.add(3,4,5,67,7,8))

Ram = Son()
Ram.sleep()

# --------------Program output--------------------------------
# PS C:\Users\Anamika\Python_codes> & C:/Users/Anamika/AppData/Local/Programs/Python/Python310/python.exe c:/Users/Anamika/Python_codes/Project/tests/all_tests/Advanced_Python/test_method_overloading_overriding.py
# 30
# PS C:\Users\Anamika\Python_codes> 
# PS C:\Users\Anamika\Python_codes> & C:/Users/Anamika/AppData/Local/Programs/Python/Python310/python.exe c:/Users/Anamika/Python_codes/Project/tests/all_tests/Advanced_Python/test_method_overloading_overriding.py
# 45
# 60
# PS C:\Users\Anamika\Python_codes> 
# PS C:\Users\Anamika\Python_codes> & C:/Users/Anamika/AppData/Local/Programs/Python/Python310/python.exe c:/Users/Anamika/Python_codes/Project/tests/all_tests/Advanced_Python/test_method_overloading_overriding.py
# 5
# 60
# 94
# PS C:\Users\Anamika\Python_codes> 
# PS C:\Users\Anamika\Python_codes> & C:/Users/Anamika/AppData/Local/Programs/Python/Python310/python.exe c:/Users/Anamika/Python_codes/Project/tests/all_tests/Advanced_Python/test_method_overloading_overriding.py
# 5
# 60
# 94
# Sleeps from 2:00 AM to 10:00 AM
# Sleeps from 10:00 PM to 5:00 AM
# PS C:\Users\Anamika\Python_codes> 