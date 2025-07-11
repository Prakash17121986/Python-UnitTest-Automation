import unittest

class test_primenumber(unittest.TestCase):

    #Prime Number Program
    def test_find_primenumber(self, number, flag=False):
        self.number = number
        self.flag = False
        if number == 0 or number==1:
            print(f"Given {number} is not a prime number")
        elif number > 1:
            for i in range(2, number):
                if (number % i) == 0:
                    self.flag = True
                    break
        if self.flag:
            print(f"Given {number} is not a  prime number")
        else:
            print(f"Given {number} is a prime number")


# if __name__ == '__main__':
#     obj = test_primenumber()
#     obj.test_find_primenumber(5, flag=False)
#     unittest.main()


    # ---------------------------Program Output-------------------------------------------
    # PS C:\Users\Anamika\Python_codes> & C:/Users/Anamika/AppData/Local/Programs/Python/Python310/python.exe c:/Users/Anamika/Python_codes/Project/tests/all_tests/DSA/test_find_prime_number.py
    # Given 6 is not a  prime number

    # ----------------------------------------------------------------------
    # Ran 0 tests in 0.000s

    # OK
    # PS C:\Users\Anamika\Python_codes> & C:/Users/Anamika/AppData/Local/Programs/Python/Python310/python.exe c:/Users/Anamika/Python_codes/Project/tests/all_tests/DSA/test_find_prime_number.py
    # Given 5 is a prime number

    # ----------------------------------------------------------------------
    # Ran 0 tests in 0.000s

    # OK
    # PS C:\Users\Anamika\Python_codes>