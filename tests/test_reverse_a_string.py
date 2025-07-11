import unittest
 
def test_reverse_a_string(str1=" "):
    str1 = str(input("Enter a string:"))
    rev = ""
    for char in str1:
        rev = char + rev
    print(rev)

if __name__ == '__main__':
    test_reverse_a_string(str1="helloworld")
    unittest.main()


    # --------------------Program Output--------------------------------------------------
    # PS C:\Users\Anamika\Python_codes> & C:/Users/Anamika/AppData/Local/Programs/Python/Python310/python.exe c:/Users/Anamika/Python_codes/Project/tests/all_tests/String_Package/test_reverse_a_string.py
    # Enter a string:helloworld
    # dlrowolleh

    # ----------------------------------------------------------------------
    # Ran 0 tests in 0.000s

    # OK
    # PS C:\Users\Anamika\Python_codes>