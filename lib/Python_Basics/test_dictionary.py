import unittest

def test_dictionary():

    '''
    # Dictionary is built-in data type that stores data in key-value pairs
    # Mutable data structure - adding, modify or update and delete
    # Ordered
    # use curly braces {} to enclose thier contents or dict() to create a dictionary
    # Key must be immutable(unchangeable) - string, numbers or tuples
    # Values can be any data type
    # dictionaries not allowed duplicates keys and it has unique keys
    # 
    '''
    # create and display the dictionary

    #create a dictionary
    student_marks = {"Sara": 99, "Aneesa": 68, "Emmanuel": 72, "Tom": 50, "Candice": 72}

    # display the dictionary
    print(f'create a dictionary using curly braces, {student_marks}')

    #create a dictionary using dict() method
    new_dict = {}
    new_dict.update({"Sara": 99, "Aneesa": 68, "Emmanuel": 72, "Tom": 50, "Candice": 72})
    print(f'create a dictionary using dict(), {new_dict}')

    # type of variable
    print(f'type, {new_dict, student_marks}')

    # copy of dictionary
    new_copy = student_marks.copy()
    print(f'copy of dictionary, {new_copy}')

    # Accessing values using keywithin the dictionary
    print('Accessing values: {student_marks["Sara"]}')

    #Get a value from its key:
    print(f'Get a value from its key, {student_marks.get("Aneesa")}')
    
    #View all keys in the dictionary:
    print(f'View all keys in the dictionary, {student_marks.keys()}')
    
    #View all values in the dictionary
    print(f'View all values in the dictionary, {student_marks.keys()}')
    
    # Get a list of all values in the dictionary
    print(f'Get a list of all values in the dictionary, {list(student_marks.keys())}')

    # Adding items to a dictionary
    #Add a single key/value pair to the dictionary
    student_marks["Paxton"] = 76
    print(f'Add a single key/value pair to the dictionary student_marks["Paxton"] = 76 in the dictionary, {student_marks}')

    #Add multiple key/value pairs to the dictionary
    student_marks.update({"Devi": 80, "Fabiola": 55})
    print(f'Add multiple key/value pairs to the dictionary, {student_marks}')

    #Removing items from a dictionary
    # Pop (remove and store as a variable) a key/value pair from the dictionary
    aneesa_mark = student_marks.pop("Aneesa")
    print(f'Pop (remove and store as a variable) a key/value pair from the dictionary in the dictionary, {student_marks}')

    #Delete a key/value pair from the dictionary
    del student_marks["Sara"]
    print(f'Delete a key/value pair from the dictionary, {student_marks}')

    #Get the length of the dictionary
    print(f'Get the length of the dictionary, {len(student_marks)}')

    #Clear the whole dictionary (delete all key/value pairs)
    student_marks.clear()
    print(f'Clear the whole dictionary (delete all key/value pairs), {student_marks}')

    student_marks = {"Sara": 99, "Aneesa": 68, "Emmanuel": 72, "Tom": 50, "Candice": 72}
    #Create a new variable using to store the marks
    marks_only = list(student_marks.values())
    print(f'Create a new variable using to store the marks, {marks_only}')

    #Create a new variable using to store the students
    student_names = list(student_marks.keys())
    print(f'Create a new variable using to store the marks, {student_names}')

    #iterate key, values through for loop
    for key, value in student_marks.items():
        print(key, value)

def test_nesteddictionary():

    myfamily = {
    "child1" : {
        "name" : "Email",
        "year" : 2004
    },
    "child2" : {
        "name" : "Tobias",
        "year" : 2007
    },
    "child3" : {
        "name" : "Linus",
        "year" : 2011
    }
    }
                    
                   
   
    print(f'Accessing items in nested dictionary, {myfamily["child1"]["name"]}')
    print(f'Accessing items in nested dictionary, {myfamily["child1"]["year"]}')

    print(f'Accessing items in nested dictionary, {myfamily["child2"]["name"]}')
    print(f'Accessing items in nested dictionary, {myfamily["child2"]["year"]}')

    print(f'Accessing items in nested dictionary, {myfamily["child3"]["name"]}')
    print(f'Accessing items in nested dictionary, {myfamily["child3"]["year"]}')

    # lppo through nested dictionary
    for x, obj in myfamily.items():
        print(x)

    for y in obj:
        print(y + ":", obj[y])


if __name__ == '__main__':
    test_dictionary()
    test_nesteddictionary()
    unittest.main()

    # -----------------------------------Program Output-----------------------------------
    # PS C:\Users\Anamika\Python_codes> & C:/Users/Anamika/AppData/Local/Programs/Python/Python310/python.exe c:/Users/Anamika/Python_codes/Project/tests/all_tests/Python_Basics/test_dict.py
    # create a dictionary using curly braces, {'Sara': 99, 'Aneesa': 68, 'Emmanuel': 72, 'Tom': 50, 'Candice': 72}
    # create a dictionary using dict(), {'Sara': 99, 'Aneesa': 68, 'Emmanuel': 72, 'Tom': 50, 'Candice': 72}
    # type, ({'Sara': 99, 'Aneesa': 68, 'Emmanuel': 72, 'Tom': 50, 'Candice': 72}, {'Sara': 99, 'Aneesa': 68, 'Emmanuel': 72, 'Tom': 50, 'Candice': 72})
    # copy of dictionary, {'Sara': 99, 'Aneesa': 68, 'Emmanuel': 72, 'Tom': 50, 'Candice': 72}     
    # Accessing values: {student_marks["Sara"]}
    # Get a value from its key, 68
    # View all keys in the dictionary, dict_keys(['Sara', 'Aneesa', 'Emmanuel', 'Tom', 'Candice']) 
    # View all values in the dictionary, dict_keys(['Sara', 'Aneesa', 'Emmanuel', 'Tom', 'Candice'])
    # Get a list of all values in the dictionary, ['Sara', 'Aneesa', 'Emmanuel', 'Tom', 'Candice'] 
    # Add a single key/value pair to the dictionary student_marks["Paxton"] = 76 in the dictionary, {'Sara': 99, 'Aneesa': 68, 'Emmanuel': 72, 'Tom': 50, 'Candice': 72, 'Paxton': 76}
    # Add multiple key/value pairs to the dictionary, {'Sara': 99, 'Aneesa': 68, 'Emmanuel': 72, 'Tom': 50, 'Candice': 72, 'Paxton': 76, 'Devi': 80, 'Fabiola': 55}
    # Pop (remove and store as a variable) a key/value pair from the dictionary in the dictionary, {'Sara': 99, 'Emmanuel': 72, 'Tom': 50, 'Candice': 72, 'Paxton': 76, 'Devi': 80, 'Fabiola': 55}
    # Delete a key/value pair from the dictionary, {'Emmanuel': 72, 'Tom': 50, 'Candice': 72, 'Paxton': 76, 'Devi': 80, 'Fabiola': 55}
    # Get the length of the dictionary, 6
    # Clear the whole dictionary (delete all key/value pairs), {}
    # Create a new variable using to store the marks, [99, 68, 72, 50, 72]
    # Create a new variable using to store the marks, ['Sara', 'Aneesa', 'Emmanuel', 'Tom', 'Candice']
    # Sara 99
    # Aneesa 68
    # Emmanuel 72
    # Tom 50
    # Candice 72
    # Accessing items in nested dictionary, Email
    # Accessing items in nested dictionary, 2004
    # Accessing items in nested dictionary, Tobias
    # Accessing items in nested dictionary, 2007
    # Accessing items in nested dictionary, Linus
    # Accessing items in nested dictionary, 2011
    # child1
    # child2
    # child3
    # name: Linus
    # year: 2011

    # ----------------------------------------------------------------------
    # Ran 0 tests in 0.000s

    # OK
    # PS C:\Users\Anamika\Python_codes> 