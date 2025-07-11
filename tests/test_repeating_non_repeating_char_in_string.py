import unittest

def test_string(string="hello world", count=1, newlist=[], repeatingdict={}, nonrepeatingdict={}):
        print(f"Given String: {string}")
        for word in string.split():
            print(f'{word}: {len(word)}')
        
        rev = ""
        count = 1
        newlist = []
        for letter in string:
            rev+=letter
            if count == 1:
                print({letter: count})
            
            newlist.append({letter:len(letter)})
    
        nonrepeatingdict = nonrepeatingdict
        repeatingdict = repeatingdict

        for i in newlist:
            for k, v in i.items():
                if k not in nonrepeatingdict:
                    nonrepeatingdict[k] = v
                    #print(f"Non Repeating character: {k}, {v}")
                else:
                    repeatingdict[k] = v
                    #print(f"Repeating character: {k}, {v}")

        print(f"Non Repeating character: {nonrepeatingdict}")
                
        print(f"Repeating character: {repeatingdict}")

if __name__ == '__main__':
    test_string(string="hello world", count=1, newlist=[], repeatingdict={}, nonrepeatingdict={})
    unittest.main()

    # --------------------------Program Output--------------------------------------------
    # PS C:\Users\Anamika\Python_codes> & C:/Users/Anamika/AppData/Local/Programs/Python/Python310/python.exe c:/Users/Anamika/Python_codes/Project/tests/all_tests/String_Package/test_repeating_non_repeating_char_in_string.py
    # Given String: hello world
    # hello: 5
    # world: 5
    # {'h': 1}
    # {'e': 1}
    # {'l': 1}
    # {'l': 1}
    # {'o': 1}
    # {' ': 1}
    # {'w': 1}
    # {'o': 1}
    # {'r': 1}
    # {'l': 1}
    # {'d': 1}
    # Non Repeating character: {'h': 1, 'e': 1, 'l': 1, 'o': 1, ' ': 1, 'w': 1, 'r': 1, 'd': 1}
    # Repeating character: {'l': 1, 'o': 1}

    # ----------------------------------------------------------------------
    # Ran 0 tests in 0.000s

    # OK
    # PS C:\Users\Anamika\Python_codes> 