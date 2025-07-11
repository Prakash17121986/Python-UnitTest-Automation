import unittest

def test_comments():
    """
    Multiline Comments - Python does not really have a syntax for multiline comments.
    To add a multiline comment you could insert a # for each line.
    This is a comment written in more than just one line
    Comments can be used to explain Python code.
    Comments can be used to make the code more readable.
    Comments can be used to prevent execution when testing code.
    Comments starts with a #, and Python will ignore them
    """
    print(f'__doc__: {test_comments.__doc__}')
    #  Python Comments, Creating a Comment
    
    #This is a comment
    print("This is a comment")
    
    # string
    print("Hello, World!")
    print("Cheers, Mate!")

    comments = '''
    a 10
    b 30
    c Hello
    d {'Age': 20, 'Name': 'Anamika'}
    e ['Apple', 'Orange', ' Banana']
    f 1.5
    <class 'int'>
    <class 'int'>
    <class 'str'>
    <class 'dict'>
    <class 'list'>
    <class 'float'>
    Hello, World!
    Five is greater than two!
    Hello, World!
    Hello, World!
    Cheers, Mate!
    Hello, World!
    '''
    #print(f'comments: {comments}')

if __name__ == '__main__':
    test_comments()
    unittest.main()

    # -------------------------Program Output------------------------------------------------

    # PS C:\Users\Anamika\Python_codes\myenv\tests\Python_Basics> python .\test_comments.py
    # __doc__: 
    #     Multiline Comments - Python does not really have a syntax for multiline comments.
    #     To add a multiline comment you could insert a # for each line.
    #     This is a comment written in more than just one line
    #     Comments can be used to explain Python code.
    #     Comments can be used to make the code more readable.
    #     Comments can be used to prevent execution when testing code.
    #     Comments starts with a #, and Python will ignore them
        
    # Hello, World!
    # Hello, World!
    # Cheers, Mate!
    # Hello, World!
    # comments:
    #     a 10
    #     b 30
    #     c Hello
    #     d {'Age': 20, 'Name': 'Anamika'}
    #     e ['Apple', 'Orange', ' Banana']
    #     f 1.5
    #     <class 'int'>
    #     <class 'int'>
    #     <class 'str'>
    #     <class 'dict'>
    #     <class 'list'>
    #     <class 'float'>
    #     Hello, World!
    #     Five is greater than two!
    #     Hello, World!
    #     Hello, World!
    #     Cheers, Mate!
    #     Hello, World!


    # ----------------------------------------------------------------------
    # Ran 0 tests in 0.000s

    # OK
    # PS C:\Users\Anamika\Python_codes\myenv\tests\Python_Basics> 