import unittest
# if statement expression evaluates to True, then the indented code following the statement is executed.
# If the expression evaluates to False then the indented code following the if statement is skipped and the program executes the next line of code which is indented at the same level as the elif statement.
# The Python else statement provides alternate code to execute if the expression in an if statement evaluates to False

def test_check_leap_year(year):

    if year % 4 == 0:
        return str(year) , "is Leap year"
    else:
        return str(year) , "is Not a leap year"

def test_if_else(test_value):

    print(f'test_value: {test_value}')
    if test_value > 1:
        print("This code is executed!")

    if test_value > 1000:
        print("This code is NOT executed!")

    print("Program continues at this point.")

def test_pet_type(pet_type="fish"):

    if pet_type == "dog":
        print("You have a dog.")

    elif pet_type == "cat":
        print("You have a cat.")

    elif pet_type == "fish":
    # This is performed
        print("You have a fish")

    else:
        print("Not sure!")

def test_compare_two_numbers():
    a = 33
    b = 200
    if b > a:
        print("b is greater than a")

def test_compare_equal_numbers():
    a = 33
    b = 33
    if b > a:
        print("b is greater than a")
    elif a == b:
        print("a and b are equal")

def test_compare_greater_equal_number():
    a = 200
    b = 33
    if b > a:
        print("b is greater than a")
    elif a == b:
        print("a and b are equal")
    else:
        print("a is greater than b")

def test_compare_greater_number():
    a = 200
    b = 33
    if b > a:
        print("b is greater than a")
    else:
        print("b is not greater than a")

    
    
def test_if_else_one_line_statement():
    
    #One line if statement
    a = 2
    b = 330
    if a > b: print("a is greater than b")

    #One line if else statement
    a = 2
    b = 330
    print("A") if a > b else print("B")

    a = 330
    b = 330
    print("A") if a > b else print("=") if a == b else print("B")

    a = 200
    b = 33
    c = 500
    if a > b and c > a:
        print("Both conditions are True")

    a = 200
    b = 33
    c = 500
    if a > b or a > c:
        print("At least one of the conditions is True")

    a = 33
    b = 200
    if not a > b:
        print("a is NOT greater than b")

    x = 41
    if x > 10:
        print("Above ten,")
    if x > 20:
        print("and also above 20!")
    else:
        print("but not above 20.")

    
    a = 33
    b = 200

    if b > a:
        pass

# if __name__ == '__main__':
#     year_to_check =  2018
#     returned_value = test_check_leap_year(year_to_check)
#     print(returned_value)
#     test_if_else(100)
#     test_if_else(1001)
#     test_pet_type(pet_type="fish")
#     test_pet_type(pet_type="dog")
#     test_pet_type(pet_type="cat")
#     test_compare_two_numbers()
#     test_compare_equal_numbers()
#     test_compare_greater_equal_number()
#     test_compare_greater_number()
#     test_if_else_one_line_statement()
#     

    # ----------------------Program Output
    # PS C:\Users\Anamika\Python_codes> & C:/Users/Anamika/AppData/Local/Programs/Python/Python310/python.exe c:/Users/Anamika/Python_codes/Project/tests/all_tests/DSA/test_if_ellif_else.py
    # ('2018', 'is Not a leap year')
    # test_value: 100
    # This code is executed!
    # Program continues at this point.
    # test_value: 1001
    # This code is executed!
    # This code is NOT executed!
    # Program continues at this point.
    # You have a fish
    # You have a dog.
    # You have a cat.
    # b is greater than a
    # a and b are equal
    # a is greater than b
    # b is not greater than a
    # B
    # =
    # Both conditions are True
    # At least one of the conditions is True
    # a is NOT greater than b
    # Above ten,
    # and also above 20!
    # PS C:\Users\Anamika\Python_codes> 