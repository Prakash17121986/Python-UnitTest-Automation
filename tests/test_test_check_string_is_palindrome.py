import unittest

def test_check_string_is_palindrome(string_value=""):
    string_value = str(input("Enter a string for palindrome check:"))
    rev = ''.join(reversed(string_value))
    rev1: slice = slice(None, None,-1)

    if string_value== rev:
        print(f"Reversed method: Given string {string_value} is palindrome")

    if string_value == string_value[::-1]:
        print(f"Slicing: Given string {string_value} is palindrome")
        
    if string_value == string_value[rev1]:
        print(f"Slice Method: Given string {string_value} is palindrome")
    else:
        print(f"Slice Method: Given string {string_value} is not palindrome")

if __name__ == '__main__':
    test_check_string_is_palindrome(string_value="HELLO WORLD")
    unittest.main()

    # ----------------------Program Output------------------------------------------------

    # PS C:\Users\Anamika\Python_codes> & C:/Users/Anamika/AppData/Local/Programs/Python/Python310/python.exe c:/Users/Anamika/Python_codes/Project/tests/all_tests/String_Package/test_test_check_string_is_palindrome.py
    # Enter a string for palindrome check:Hello world
    # Slice Method: Given string Hello world is not palindrome

    # ----------------------------------------------------------------------
    # Ran 0 tests in 0.000s

    # OK
    # PS C:\Users\Anamika\Python_codes> & C:/Users/Anamika/AppData/Local/Programs/Python/Python310/python.exe c:/Users/Anamika/Python_codes/Project/tests/all_tests/String_Package/test_test_check_string_is_palindrome.py
    # Enter a string for palindrome check:MADAM
    # Reversed method: Given string MADAM is palindrome
    # Slicing: Given string MADAM is palindrome
    # Slice Method: Given string MADAM is palindrome

    # ----------------------------------------------------------------------
    # Ran 0 tests in 0.000s

    # OK
    # PS C:\Users\Anamika\Python_codes> 