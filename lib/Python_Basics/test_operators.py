import unittest

# Python Operators
# Operators are used to perform operations on variables and values.
# Python divides the operators in the following groups:

# Arithmetic operators
# Assignment operators
# Comparison operators
# Logical operators
# Identity operators
# Membership operators
# Bitwise operators

class test_arithmetic_operators(unittest.TestCase):
    

    def test_arithmetic_operator(self, x, y):
        '''
        Arithmetic operators are used with numeric values to perform common mathematical operations
        '''
        #self.x = 15
        #self.y = 3
        self.x = x
        self.y = y
        print(f'Two values x, y: {x}, {y}',end="\n")
        print(f'Addition of x + y: {x+y}',end="\n")
        print(f'Subraction of x - y: {x-y}',end="\n")
        print(f'Multiplication of x * y: {x*y}',end="\n")
        print(f'Division of x / y: {x/y}',end="\n")
        print(f'Floor Division of x // y: {x//y}',end="\n")
        print(f'exponentiation of x ** y: {x**y}',end="\n")
        print(f'modulus of x + y: {x%y}',end="\n")

class test_assignment_operators(unittest.TestCase):

    def test_assignment_operator(self, x):
        '''
        Assignment operators are used to assign values to variables
        '''
        #self.x = 5
        self.x = x
        print(f'x: {x}')
        x += 3
        print(f'Addition x += 3: {x}',end="\n") 

        x -= 3
        print(f'Subraction x -= 3: {x}',end="\n") 

        x *= 3
        print(f'Multiplication x *= 3: {x}',end="\n")

        x /= 3
        print(f'Division x /= 3: {x}',end="\n") 

        x = x % 3
        print(f'Modulus x = x % 3: {x}',end="\n") 

        x //= 3
        print(f'Floor division x //= 3: {x}',end="\n") 

        x = 3
        x **= 3
        print(f'Exponentiation x **= 3: {x}',end="\n") 

        x &= 3
        print(f'And x &= 3: {x}',end="\n") 

        x |= 3
        print(f'OR x |= 3: {x}',end="\n")

        x ^= 3
        print(f'XOR x ^= 3: {x}',end="\n") 

        x >>= 3
        print(f'Zero fill right shift x >>= 3: {x}',end="\n") 

        x <<= 3
        print(f'Zero fill left shift <<= 3: {x}',end="\n")    

class test_comparision_operators(unittest.TestCase):
    
    def test_comparision_operator(self, x,y):
        '''
        Comparison operators are used to compare two values
        '''
        self.x = x
        self.y = y
        print(f'Two values x, y: {x}, {y}', end="\n")
        print(f'Equal x == y: {x == y}', end="\n") 
        print(f'Not Equal x != y: {x != y}', end="\n")
        print(f'Greater than x > y: {x > y}', end="\n")
        print(f'Less than x < y: {x < y}', end="\n")
        print(f'Greater than or equal to x >= y: {x >= y}', end="\n")
        print(f'Less than or equal to x <= y: {x <= y}', end="\n")

class test_logical_operators(unittest.TestCase):

    def test_logical_operator(self, x):
        '''
        Logical operators are used to combine conditional statements
        '''
        self.x = x
        print(f'x: {x}', end="\n")
        #Returns True if both statements are true
        print(f'x < 5 and  x < 10: {x < 5 and  x < 10}', end="\n")
        #Returns True if one of the statements is true
        print(f'x < 5 or x < 4: {x < 5 or x < 4}', end="\n")
        #Reverse the result, returns False if the result is true
        print(f'not(x < 5 and x < 10): {not(x < 5 and x < 10)}', end="\n")
        
class test_identity_operators(unittest.TestCase):

    def test_identity_operator(self, x,y):   
        '''
        Identity operators are used to compare the objects, not if they are equal, but if they are actually the same object, with the same memory location
        '''
        self.x = x
        self.y = y
        #Returns True if both variables are the same object
        x = ["apple", "banana"]
        y = ["apple", "banana"]
        z = x

        # returns True because z is the same object as x
        print("x is z",x is z, end="\n")

        # returns False because x is not the same object as y, even if they have the same content
        print("x is y",x is y, end="\n")

        # to demonstrate the difference betweeen "is" and "==": this comparison returns True because x is equal to y
        #Returns True if both variables are not the same object
        print("x == y",x == y, end="\n")
        
        # returns False because z is the same object as x
        print("x is not z",x is not z, end="\n")
        
        # returns True because x is not the same object as y, even if they have the same content
        print("x is not y",x is not y, end="\n")
        
        # to demonstrate the difference betweeen "is not" and "!=": this comparison returns False because x is equal to y
        print("x != y",x != y, end="\n")
        

class test_membership_operators(unittest.TestCase):

    def test_membership_operator(self, x):
        '''
        Membership operators are used to test if a sequence is presented in an object:
        '''
        self.x = x
        print('x:', x)
        #x = ["apple", "banana"]
        #print("banana" in x)
  
        #Returns True if a sequence with the specified value is present in the object
        #x in y
        print('"banana" in x',"banana" in x, end="\n")
        #Returns True if a sequence with the specified value is not present in the object
        #x not in y
        print('"pineapple" not in x', "pineapple" not in x, end="\n")

class test_bitwise_operators(unittest.TestCase):

    def test_bitwise_operator(self):
        '''
        Bitwise operators are used to compare (binary) numbers
        '''

        """
        The & operator compares each bit and set it to 1 if both are 1, otherwise it is set to 0:

        6 = 0000000000000110
        3 = 0000000000000011
        --------------------
        2 = 0000000000000010
        ====================

        Decimal numbers and their binary values:
        0 = 0000000000000000
        1 = 0000000000000001
        2 = 0000000000000010
        3 = 0000000000000011
        4 = 0000000000000100
        5 = 0000000000000101
        6 = 0000000000000110
        7 = 0000000000000111
        """
        # & - AND - Sets each bit to 1 if both bits are 1
        print("6 & 3",6 & 3, end="\n")
        

        """
        The | operator compares each bit and set it to 1 if one or both is 1, otherwise it is set to 0:

        6 = 0000000000000110
        3 = 0000000000000011
        --------------------
        7 = 0000000000000111
        ====================
        """
        # |	OR	Sets each bit to 1 if one of two bits is 1
        print("6 | 3",6 | 3, end="\n")

        """
        The ^ operator compares each bit and set it to 1 if only one is 1, otherwise (if both are 1 or both are 0) it is set to 0:

        6 = 0000000000000110
        3 = 0000000000000011
        --------------------
        5 = 0000000000000101
        ====================
        """
        # ^	XOR	Sets each bit to 1 if only one of two bits is 1
        print("6 ^ 3",6 ^ 3, end="\n")

        
        """
        The ~ operator inverts each bit (0 becomes 1 and 1 becomes 0).

        Inverted 3 becomes -4:
        3 = 0000000000000011
        -4 = 1111111111111100

        Decimal numbers and their binary values:
        4 = 0000000000000100
        3 = 0000000000000011
        2 = 0000000000000010
        1 = 0000000000000001
        0 = 0000000000000000
        -1 = 1111111111111111
        -2 = 1111111111111110
        -3 = 1111111111111101
        -4 = 1111111111111100
        """
        # ~	NOT	Inverts all the bits
        print("!3",~3, end="\n")

        
        """
        The << operator inserts the specified number of 0's (in this case 2) from the right and let the same amount of leftmost bits fall off:

        If you push 00 in from the left:
        3 = 0000000000000011
        becomes
        12 = 0000000000001100

        Decimal numbers and their binary values:
        0 = 0000000000000000
        1 = 0000000000000001
        2 = 0000000000000010
        3 = 0000000000000011
        4 = 0000000000000100
        5 = 0000000000000101
        6 = 0000000000000110
        7 = 0000000000000111
        8 = 0000000000001000
        9 = 0000000000001001
        10 = 0000000000001010
        11 = 0000000000001011
        12 = 0000000000001100
        """
        # <<	Zero fill left shift	Shift left by pushing zeros in from the right and let the leftmost bits fall off
        print("3 << 2",3 << 2, end="\n")


        """
        The >> operator moves each bit the specified number of times to the right. Empty holes at the left are filled with 0's.

        If you move each bit 2 times to the right, 8 becomes 2:
        8 = 0000000000001000
        becomes
        2 = 0000000000000010

        Decimal numbers and their binary values:
        0 = 0000000000000000
        1 = 0000000000000001
        2 = 0000000000000010
        3 = 0000000000000011
        4 = 0000000000000100
        5 = 0000000000000101
        6 = 0000000000000110
        7 = 0000000000000111
        8 = 0000000000001000
        9 = 0000000000001001
        10 = 0000000000001010
        11 = 0000000000001011
        12 = 0000000000001100
        """

        # >>	Signed right shift	Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off
        print("8 >> 2",8 >> 2, end="\n")

class test_operator_procedence(unittest.TestCase):

    def test_operator_procedence(self):
        '''
        Operator precedence describes the order in which operations are performed
        '''
        #Parentheses has the highest precedence, meaning that expressions inside parentheses must be evaluated first
        
        """
        Parenthesis have the highest precedence, and need to be evaluated first.
        The calculation above reads 9 - 9 = 0
        """
        print("(6 + 3) - (6 + 3)",(6 + 3) - (6 + 3), end="\n")

        #Multiplication * has higher precedence than addition +
        print("100 + 5 * 3",100 + 5 * 3, end="\n")


        """
        Exponentiation has higher precedence than subtraction, and needs to be evaluated first.
        The calculation above reads 100 - 27 = 73
        """
        print("100 - 3 ** 3",100 - 3 ** 3, end="\n")

        """
        Bitwise NOT has higher precedence than addition, and needs to be evaluated first.
        The calculation above reads 100 + -4 = 96
        """

        print("100 + ~3",100 + ~3, end="\n")

        """
        Multiplication has higher precedence than addition, and needs to be evaluated first.
        The calculation above reads 100 + 15 = 115
        """

        print("100 + 5 * 3",100 + 5 * 3, end="\n")

        """
        Subtraction has a lower precedence than multiplication, and we need to calculate the multiplication first.
        The calculation above reads 100 - 15 = 85
        """

        print("100 - 5 * 3",100 - 5 * 3, end="\n")

    
        """
        Bitwise right shift has a lower precedence than subtraction, and we need to calculate the subtraction first.
        The calculation above reads 8 >> 2 = 2

        More explanation:
        The >> operator moves each bit the specified number of times to the right. Empty holes at the left are filled with 0's.

        If you move each bit 2 times to the right, 8 becomes 2:
        8 = 0000000000001000
        becomes
        2 = 0000000000000010

        Decimal numbers and their binary values:
        0 = 0000000000000000
        1 = 0000000000000001
        2 = 0000000000000010
        3 = 0000000000000011
        4 = 0000000000000100
        5 = 0000000000000101
        6 = 0000000000000110
        7 = 0000000000000111
        8 = 0000000000001000
        9 = 0000000000001001
        10 = 0000000000001010
        11 = 0000000000001011
        12 = 0000000000001100
        """

        print("8 >> 4 - 2",8 >> 4 - 2, end="\n")

        """
        Bitwise AND has a lower precedence than addition, and we need to calculate the addition first.
        The calculation above reads 6 & 3 = 2

        More explanation:
        The & operator compares each bit and set it to 1 if both are 1, otherwise it is set to 0:

        6 = 0000000000000110
        3 = 0000000000000011
        --------------------
        2 = 0000000000000010
        ====================

        Decimal numbers and their binary values:
        0 = 0000000000000000
        1 = 0000000000000001
        2 = 0000000000000010
        3 = 0000000000000011
        4 = 0000000000000100
        5 = 0000000000000101
        6 = 0000000000000110
        7 = 0000000000000111
        """

        print("6 & 2 + 1",6 & 2 + 1, end="\n")


        """
        Bitwise XOR has a lower precedence than addition, and we need to calculate the addition first.
        The calculation above reads 6 ^ 3 = 5

        More explanation:
        The ^ operator compares each bit and set it to 1 if only one is 1, otherwise (if both are 1 or both are 0) it is set to 0:

        6 = 0000000000000110
        3 = 0000000000000011
        --------------------
        5 = 0000000000000101
        ====================

        Decimal numbers and their binary values:
        0 = 0000000000000000
        1 = 0000000000000001
        2 = 0000000000000010
        3 = 0000000000000011
        4 = 0000000000000100
        5 = 0000000000000101
        6 = 0000000000000110
        7 = 0000000000000111
        """

        print("6 ^ 2 + 1",6 ^ 2 + 1, end="\n")

        """
        Bitwise OR has a lower precedence than addition, and we need to calculate the addition first.
        The calculation above reads 6 | 3 = 7

        More explanation:
        The | operator compares each bit and set it to 1 if one or both is 1, otherwise it is set to 0:

        6 = 0000000000000110
        3 = 0000000000000011
        --------------------
        7 = 0000000000000111
        ====================

        Decimal numbers and their binary values:
        0 = 0000000000000000
        1 = 0000000000000001
        2 = 0000000000000010
        3 = 0000000000000011
        4 = 0000000000000100
        5 = 0000000000000101
        6 = 0000000000000110
        7 = 0000000000000111
        """

        print("6 | 2 + 1", 6 | 2 + 1, end="\n")

        

        """
        The "like" comparison has a lower precedence than addition, and we need to calculate the addition first.
        The calculation above reads 5 == 5 = True
        """

        print("5 == 4 + 1",5 == 4 + 1, end="\n")

        """
        The logical NOT operator has a lower precedence than "like" comparison, and we need to calculate the comparison first.
        The calculation above reads: not True = False
        """

        print("not 5 == 5",not 5 == 5, end="\n")

    
        """
        The and operator has a higher precedence than or, and we need to calculate the and expression first.
        The calculation above reads: 1 or 3 = 1
        """

        print("1 or 2 and 3",1 or 2 and 3, end="\n")

        

        """
        The or operator has a lower precedence than addition, and we need to calculate the addition first.
        The calculation above reads: 4 or 15 or 8 = 4
        """

        print("4 or 5 + 10 or 8", 4 or 5 + 10 or 8, end="\n")


if __name__ == '__main__':
    obj1 = test_arithmetic_operators()
    obj1.test_arithmetic_operator(15,3)
    obj2 = test_assignment_operators()
    obj2.test_assignment_operator(5)
    obj3 = test_comparision_operators()
    obj3.test_comparision_operator(3,5)
    obj4 = test_logical_operators()
    obj4.test_logical_operator(4)
    obj5 = test_identity_operators()
    obj5.test_identity_operator(["apple", "banana"],["apple", "banana"])   
    obj6 = test_membership_operators()
    obj6.test_membership_operator(["apple", "banana"])
    obj7 = test_bitwise_operators()
    obj7.test_bitwise_operator()
    obj8 = test_operator_procedence()
    obj8.test_operator_procedence()
    unittest.main()


    # ----------------------Program Output------------------------------------------------
    # PS C:\Users\Anamika\Python_codes> & C:/Users/Anamika/AppData/Local/Programs/Python/Python310/python.exe c:/Users/Anamika/Python_codes/Project/tests/all_tests/Python_Basics/test_operators.py
    # Two values x, y: 15, 3
    # Addition of x + y: 18
    # Subraction of x - y: 12
    # Multiplication of x * y: 45
    # Division of x / y: 5.0
    # Floor Division of x // y: 5
    # exponentiation of x ** y: 3375
    # modulus of x + y: 0
    # x: 5
    # Addition x += 3: 8
    # Subraction x -= 3: 5
    # Multiplication x *= 3: 15
    # Division x /= 3: 5.0
    # Modulus x = x % 3: 2.0
    # Floor division x //= 3: 0.0
    # Exponentiation x **= 3: 27
    # And x &= 3: 3
    # OR x |= 3: 3
    # XOR x ^= 3: 0
    # Zero fill right shift x >>= 3: 0
    # Zero fill left shift <<= 3: 0
    # Two values x, y: 3, 5
    # Equal x == y: False
    # Not Equal x != y: True
    # Greater than x > y: False
    # Less than x < y: True
    # Greater than or equal to x >= y: False
    # Less than or equal to x <= y: True
    # x: 4
    # x < 5 and  x < 10: True
    # x < 5 or x < 4: True
    # not(x < 5 and x < 10): False
    # x is z True
    # x is y False
    # x == y True
    # x is not z False
    # x is not y True
    # x != y False
    # True
    # True
    # 2
    # 7
    # 5
    # -4
    # 12
    # 2
    # (6 + 3) - (6 + 3) 0
    # 100 + 5 * 3 115
    # 100 - 3 ** 3 73
    # 100 + ~3 96
    # 100 + 5 * 3 115
    # 100 - 5 * 3 85
    # 8 >> 4 - 2 2
    # 6 & 2 + 1 2
    # 6 ^ 2 + 1 5
    # 6 | 2 + 1 7
    # 5 == 4 + 1 True
    # not 5 == 5 False
    # 1 or 2 and 3 1
    # 4 or 5 + 10 or 8 4

    # ----------------------------------------------------------------------
    # Ran 0 tests in 0.000s

    # OK
    # PS C:\Users\Anamika\Python_codes> 