
import unittest

def test_armstrong(num, temp=int, sum_value=0):
    #num = int(input("Enter a number:"))
    sum_value = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        sum_value = sum_value + (digit ** 3)
        temp = temp // 10
    if num == sum_value:
        print(num, "is a armstrong number")
    else:
        print(num, "is not a armstrong number")

# if __name__ == '__main__':
#     test_armstrong(153, temp=int, sum_value=0)
#     unittest.main()


    # ---------------------------Program Output-------------------------------------------
    # PS C:\Users\Anamika\Python_codes> & C:/Users/Anamika/AppData/Local/Programs/Python/Python310/python.exe c:/Users/Anamika/Python_codes/Project/tests/all_tests/DSA/test_find_armstrong_number.py
    # 154 is not a armstrong number

    # ----------------------------------------------------------------------
    # Ran 0 tests in 0.000s

    # OK
    # PS C:\Users\Anamika\Python_codes> & C:/Users/Anamika/AppData/Local/Programs/Python/Python310/python.exe c:/Users/Anamika/Python_codes/Project/tests/all_tests/DSA/test_find_armstrong_number.py
    # 153 is a armstrong number

    # ----------------------------------------------------------------------
    # Ran 0 tests in 0.000s

    # OK
    # PS C:\Users\Anamika\Python_codes> 