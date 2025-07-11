
import unittest

#Fibonnic series Program
def test_fibonnic_series(number):
    a,b = 0,1
    while a<number:
        print(a)
        a, b = a+b, a

# if __name__ == '__main__':
#     test_fibonnic_series(10)
#     unittest.main()


    # -----------------Program Output----------------------------
    # PS C:\Users\Anamika\Python_codes> & C:/Users/Anamika/AppData/Local/Programs/Python/Python310/python.exe c:/Users/Anamika/Python_codes/Project/tests/all_tests/DSA/test_fibonnic_series.py
    # 0
    # 1
    # 1
    # 2
    # 3
    # 5
    # 8

    # ----------------------------------------------------------------------
    # Ran 0 tests in 0.000s

    # OK
    # PS C:\Users\Anamika\Python_codes> 