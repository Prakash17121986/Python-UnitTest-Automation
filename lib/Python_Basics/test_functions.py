

#A function is a block of code which only runs when it is called.
#You can pass data, known as parameters, into a function.
#A function can return data as a result.

# In Python a function is defined using the def keyword
# function name followed by parameters or arguments
# logic or function code to return the value 

# Function call can return the value for the function
# A parameter is the variable listed inside the parentheses in the function definition.
# An argument is the value that is sent to the function when it is called.

# By default, a function must be called with the correct number of arguments.
# Meaning that if your function expects 2 arguments, you have to call the function with 2 arguments, not more, and not less.

# Arbitrary Arguments, *args - If you do not know how many arguments that will be passed into your function, add a * before the parameter name in the function definition.
# This way the function will receive a tuple of arguments, and can access the items accordingly
# If the number of arguments is unknown, add a * before the parameter name

# Keyword Arguments - You can also send arguments with the key = value syntax
# This way the order of the arguments does not matter

#Arbitrary Keyword Arguments, **kwargs - If you do not know how many keyword arguments that will be passed into your function, add two asterisk: ** before the parameter name in the function definition.
# This way the function will receive a dictionary of arguments, and can access the items accordingly
# If the number of keyword arguments is unknown, add a double ** before the parameter name

# Return Values - To let a function return a value, use the return statement

# function definitions cannot be empty, but if you for some reason have a function definition with no content, put in the pass statement to avoid getting an error.

'''
Passing a List as an Argument
You can send any data types of argument to a function (string, number, list, dictionary etc.), and it will be treated as the same data type inside the function.

E.g. if you send a List as an argument, it will still be a List when it reaches the function
def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)
'''

import unittest

class test_basicfunctions():

    _value = 10
    temp = 100
    print(f"class variable: _value: {_value}")
    print(f"class variable: temp: {temp}")
    var = "Hi, The below function code contains different parameter passed with argument value to function call to return the value"
    print("class string variable",var)
    def __init__(self,a,b,c):
        self.a = 10
        self.b = 20
        self.c = 30
    
    def test_greet(self, first_name, last_name):
        '''
        Default argument: two argument as string value for given parameter in function call
        # greet not taking any parameter to function call
        # print takes comments as argument to print the value
        # argument is value for given parameter in function call
        #all the parameter are required to function
        # define for a function are required so here our greet function takes two
        # #parameters if I exclude one of these arguments and save the changes you can
        '''
        self.first_name = first_name
        self.last_name = last_name
        print(f"This is default argument function method with two parameter")
        print(f"Hi {self.first_name} {self.last_name}")
        
    # first default argument
    def test_get_greeting_one_default_argument(self, name):
       '''Default argument: one argument as string value for given parameter in function call'''
       print(f"This is default argument function method with single parameter")
       
       self.name = name
       print(f"Default argument with single argument or parameter")
       print(f"Hi {self.name}")

    # first default argument, second keyword argument
    def test_addition_of_two_numbers_with_default_argument_keyword_argument(self, number, second_value=1):
        '''Default argument: one argument as string value for given parameter in function call
        # Two default argument value to the function
        # First as a default argument, second as a keyword argument to the function
        # non default argument follows default argument
        # keyword value by=1
        # all the required argument comes first
        # keyword argument is last one'''
        
        
        self.number = number
        self.second_value = second_value
        print(f"Default argument with two argument or parameter")
        print("Adding two numbers: {}, {}, results is {}".format(self.number, self.second_value, self.number + self.second_value))

        #Variable number of arguments with different data types to the function
    def test_variable_length_arguments(self, *args):
        '''
        define a function with variable no of arguments to pass as a string, list, integer, dict.
        Variable number of arguments with different data types to the function
        '''
        
        self.args = args
        print(self.args)
        
        a,b,c,d,e,f,g,h = self.args
        print(f"no of variable argument with different data types")
        print(f'{type(a)},{type(b)},{type(c)},{type(d)},{type(e)},{type(f)},{type(g)},{type(h)}')

        print(f"type: {a},{b},{c},{d},{e},{f},{g},{h}")

    def test_variable_keyword_arguments_multiplication(self, total, *numbers):
        '''
        define a function with variable no of arguments to pass as a integer
        Variable number of arguments with different data types to the function
        '''
        
        self.total = total
        self.total = 1
        print("Total value:", self.total)
        self.numbers = numbers
        print("Numbers:", self.numbers)
        for number in self.numbers:
                print("Iterate the number: ", number)
                self.total = self.total * number
        print("total numbers:", self.total)
        

    def test_variable_keyword_arguments(self, **user):
        '''
        # define a function with variable no of keyword arguments 
        # keyword arguments to a function
        # Here we can pass multiple key value pairs or multiple keyword arguments to a function
        # we are passing 3 keyword argument to this function now let's run this program
        # we have these curly braces with keys and values to form of dictnary
        # ** or asterik means pass the multiple key value pairs or multiple keyword argument to this function
        # Python will automatically package them into a dictionary so this user object here is a dictioanry now using the bracket notation we can get the values of various keys in the dictionary so we can print user square
        # unpacking the keys and values to form a dict
        # Keyword argument or to pass multiple key value pair to the function
        '''
        
        self.user = user
        return user

    def test_no_arguments(self):
        pass
    

    def test_positional_only(self, a, b, /):
        '''
        Combine Positional-Only and Keyword-Only
        You can combine the two argument types in the same function.
        Any argument before the / , are positional-only, and any argument after the *, are keyword-only.
        '''
        self.a = a
        self.b = b
   

        print(f"Positional arguments: {a + b}")


    def test_keyword_only(self, *, c, d):
        '''
        Combine Positional-Only and Keyword-Only
        You can combine the two argument types in the same function.
        Any argument before the / , are positional-only, and any argument after the *, are keyword-only.
        '''
        self.c = c
        self.d = d

        print(f"Keyword arguments: {c + d}")

    def test_my_function(self, a, b, /, *, c, d):
        '''
        Combine Positional-Only and Keyword-Only
        You can combine the two argument types in the same function.
        Any argument before the / , are positional-only, and any argument after the *, are keyword-only.
        '''
        self.a = a
        self.b = b
        self.c = c
        self.d = d

        print(f"combination of positional and keyword arguments: {a + b + c + d}")

if __name__ == '__main__':
    obj = test_basicfunctions(10,20,30)
    obj.test_greet("Anamika", "Prakash")
    obj.test_get_greeting_one_default_argument(name="Anamika")
    obj.test_addition_of_two_numbers_with_default_argument_keyword_argument(10, second_value=1)
    obj.test_variable_length_arguments("hello", None, 10, 4.5,(1,2,3), [1,2,5], {'a':1,'b':2},{'A','B'})
    obj.test_variable_keyword_arguments_multiplication(1, [1,2,3,4,5])
    value = obj.test_variable_keyword_arguments(c = 7, d = 8, e= 'hello')
    print(f"variable arguments: {value}")
    obj.test_no_arguments()
    obj.test_positional_only(10,5)
    obj.test_keyword_only(c = 7, d = 8)
    obj.test_my_function(5, 6, c = 7, d = 8)
    unittest.main()


    #-------------------Program Output---------------------------------------------------
    # PS C:\Users\Anamika\Python_codes> & C:/Users/Anamika/AppData/Local/Programs/Python/Python310/python.exe c:/Users/Anamika/Python_codes/Project/tests/all_tests/Python_Basics/test_functions.py
    # class variable: _value: 10
    # class variable: temp: 100
    # class string variable Hi, The below function code contains different parameter passed with argument value to function call to return the value
    # This is default argument function method with two parameter
    # Hi Anamika Prakash
    # This is default argument function method with single parameter
    # Default argument with single argument or parameter
    # Hi Anamika
    # Default argument with two argument or parameter
    # Adding two numbers: 10, 1, results is 11
    # ('hello', None, 10, 4.5, (1, 2, 3), [1, 2, 5], {'a': 1, 'b': 2}, {'A', 'B'})
    # no of variable argument with different data types
    # <class 'str'>,<class 'NoneType'>,<class 'int'>,<class 'float'>,<class 'tuple'>,<class 'list'>,<class 'dict'>,<class 'set'>
    # type: hello,None,10,4.5,(1, 2, 3),[1, 2, 5],{'a': 1, 'b': 2},{'A', 'B'}
    # Total value: 1
    # Numbers: ([1, 2, 3, 4, 5],)
    # Iterate the number:  [1, 2, 3, 4, 5]
    # total numbers: [1, 2, 3, 4, 5]
    # variable arguments: {'c': 7, 'd': 8, 'e': 'hello'}
    # Positional arguments: 15
    # Keyword arguments: 15
    # combination of positional and keyword arguments: 26
    # ----------------------------------------------------------------------
    # Ran 0 tests in 0.000s

    # OK
    # PS C:\Users\Anamika\Python_codes> 
