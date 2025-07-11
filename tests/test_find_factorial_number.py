
import unittest

class test_find_factorial_number(unittest.TestCase):

    #Factorial Program
    def test_factorial(self, num, fact):
        self.num = num
        #num = iint(input("Enter a number:"))
        self.fact = 1
        if num<0:
            print("Sorry, factorial does not exit")
        elif num==0:
            print("The factorial of 0 or 1")  
        else:
            for i in range(1, num+1):
                fact = fact * i
                print("The factorial of", num, "is", fact)

# if __name__ == '__main__':
#     obj = test_find_factorial_number()
#     obj.test_factorial(5, 1)
#     unittest.main()

    # -------------------------program Output---------------------------------------------
    # PS C:\Users\Anamika\Python_codes> & C:/Users/Anamika/AppData/Local/Programs/Python/Python310/python.exe c:/Users/Anamika/Python_codes/Project/tests/all_tests/DSA/test_find_factorial_number.py
    # The factorial of 5 is 1
    # The factorial of 5 is 2
    # The factorial of 5 is 6
    # The factorial of 5 is 24
    # The factorial of 5 is 120

    # ----------------------------------------------------------------------
    # Ran 0 tests in 0.000s

    # OK
    # PS C:\Users\Anamika\Python_codes> 