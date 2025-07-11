import unittest

class test_keys_values_to_lowercase(unittest.TestCase):

    # convert Python dictonary keys/values to lowercase
    def test_keys_values_to_lowercase_dictionary(self, dict1={}):
        self.dict1 = dict1
        dict1 = {'Foo': 'Hello', 'Bar': 'World'} # set have keys is upper
        print(f'Given dictionary: {dict1}')
        new_dict = dict((k.lower(), v.lower()) for k, v in dict1.items())
        print(f'Given dictionary with lowercase: {dict1}')
        #{'foo': 'hello', 'bar': 'world'}

# if __name__ == '__main__':
#     obj = test_keys_values_to_lowercase()
#     obj.test_keys_values_to_lowercase_dictionary({'Foo': 'Hello', 'Bar': 'World'})
#     unittest.main()


    # -------------------------Program Output---------------------------------------------
    # PS C:\Users\Anamika\Python_codes> & C:/Users/Anamika/AppData/Local/Programs/Python/Python310/python.exe c:/Users/Anamika/Python_codes/Project/tests/all_tests/DSA/test_keys_values_to_lowercase_dictionary.py
    # Given dictionary: {'Foo': 'Hello', 'Bar': 'World'}
    # Given dictionary with lowercase: {'Foo': 'Hello', 'Bar': 'World'}

    # ----------------------------------------------------------------------
    # Ran 0 tests in 0.000s

    # OK
    # PS C:\Users\Anamika\Python_codes> 