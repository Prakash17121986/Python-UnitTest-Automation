import unittest

class test_handling_missing_key_in_dictionary(unittest.TestCase):

    def test_handling_missing_key_in_dictionary(self, dict1):
        self.dict1 = {}
        dict1 = {'India': 'IN', 'Australia': 'AUS', 'Brazil': 'BZ'}
        print(dict1.get('Australia', 'Not Found'))
        print(dict1.get('Canada', 'Not Found'))

# if __name__ == '__main__':
#     obj = test_handling_missing_key_in_dictionary()
#     obj.test_handling_missing_key_in_dictionary({'India': 'IN', 'Australia': 'AUS', 'Brazil': 'BZ'})
#     unittest.main()