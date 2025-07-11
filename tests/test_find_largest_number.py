import unittest

def find_largest_number(listvalue):
    print("Given list:", listvalue)
    largest = listvalue[0]
    for value in listvalue:
        if value > largest:
            largest = value
    print(largest)


# if __name__ =='__main__':
#     find_largest_number(listvalue=[1,2,4,3,19,50])


# PS C:\Users\Anamika\Python_codes> & C:/Users/Anamika/AppData/Local/Programs/Python/Python310/python.exe c:/Users/Anamika/Python_codes/Project/tests/all_tests/DSA/test_find_largest_number.py
# Given list: [1, 2, 4, 3, 19, 50]
# 50
# PS C:\Users\Anamika\Python_codes> 