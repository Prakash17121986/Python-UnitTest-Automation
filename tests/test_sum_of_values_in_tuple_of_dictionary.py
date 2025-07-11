import unittest

class test_tuple_of_dictionary(unittest.TestCase):

    def test_tuple_of_dictionary(self, d1={}, d2={}):
            self.d1 = {}
            self.d2 = {}
            d1 = {"a":100, "b":200, "c": 300}
            d2 = {"a": 300, "b":200, "d": 400}
            print(f'Given dictionary dict1: {d1}, dict2: {d2} ')
            d3 = {}
            for key, value in d1.items():
                val1 = d1["a"] + d2["a"]
                val2 = d1["b"] + d2["b"]
                val3 = d1["c"] + d2["d"]
                d3.update({"a":val1, "b": val2, "d": val3})
            print("Sum of values of key1 & key2 from dic1 & dict2", d3)

# if __name__ == '__main__':
#     obj = test_tuple_of_dictionary()
#     obj.test_tuple_of_dictionary(d1={"a":100, "b":200, "c": 300}, d2={"a": 300, "b":200, "d": 400})
#     unittest.main()

    # -------------------------------Program Output---------------------------------------
    # PS C:\Users\Anamika\Python_codes> & C:/Users/Anamika/AppData/Local/Programs/Python/Python310/python.exe c:/Users/Anamika/Python_codes/Project/tests/all_tests/DSA/test_test_tuple_of_dictionary.py
    # Given dictionary dict1: {'a': 100, 'b': 200, 'c': 300}, dict2: {'a': 300, 'b': 200, 'd': 400} 
    # Sum of values of key1 & key2 from dic1 & dict2 {'a': 400, 'b': 400, 'd': 700}

    # ----------------------------------------------------------------------
    # Ran 0 tests in 0.000s

    # OK
    # PS C:\Users\Anamika\Python_codes> 