
import unittest

def test_remove_vowels_in_string(str1, results="", vowels=[]):
    str1 = str(input("Enter the string: "))
    print(f"Given string: {str1}")
    result= ""
    vowels = ['a','e','i','o','u']
    for letter in str1:
        if letter.lower() not in vowels:
            result += letter
    
    print(f"Remove vowels in string, {result}")

if __name__ == '__main__':
    test_remove_vowels_in_string(str1="hello world", results="", vowels=[])
    unittest.main()

    # ------------------------Program Output----------------------------------------------
    # PS C:\Users\Anamika\Python_codes> & C:/Users/Anamika/AppData/Local/Programs/Python/Python310/python.exe c:/Users/Anamika/Python_codes/Project/tests/all_tests/String_Package/test_remove_vowels_in_string.py
    # Enter the string: helloworld
    # Given string: helloworld
    # Remove vowels in string, hllwrld

    # ----------------------------------------------------------------------
    # Ran 0 tests in 0.000s

    # OK
    # PS C:\Users\Anamika\Python_codes>