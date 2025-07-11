import unittest

def find_smallest_number(listvalue):
    print("Given list:", listvalue)
    smallest = listvalue[0]
    for value in listvalue:
        if value < smallest:
            smallest = value
    print(smallest)


# if __name__ =='__main__':
#     find_smallest_number(listvalue=[1,2,4,3,19,50])

# ===============Program Output========================
# PS C:\Users\Anamika\Python_codes> & C:/Users/Anamika/AppData/Local/Programs/Python/Python310/python.exe c:/Users/Anamika/Python_codes/Project/tests/all_tests/Python_Basics/test_find_smallest_number.py
# Given list: [1, 2, 4, 3, 19, 50]
# 1
# PS C:\Users\Anamika\Python_codes> 

