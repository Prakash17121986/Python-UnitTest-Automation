import unittest
from tests import test_list_methods
from tests.test_list_methods import Test_ListMethods 
from HTMLTestRunner.runner import HTMLTestRunner

from io import StringIO
import sys

Test_ListMethods = Test_ListMethods([10,20,30], [4,5,6])


class Test_List_Methods(unittest.TestCase):
    
    def test_create_a_list(self):
        
        Test_ListMethods.test_createlist()
        
        
    def test_append_values_to_the_list(self):
        
        Test_ListMethods.test_append(value=40)
        
    
    def test_extend_values_to_the_list(self):
        
        Test_ListMethods.test_extend(value=[1,2,3])
 

    def test_find_the_index_of_the_value_in_list(self):
        
        Test_ListMethods.test_index(listvalue=2)
        

    def test_find_the_count_of_the_value_in_list(self):
        
        Test_ListMethods.test_count(countvalue=1)

    
    def test_insert_the_value_in_list(self):
        
        Test_ListMethods.test_insert(index=0, insertvalue=100)
    
    
    def test_remove_the_value_in_list(self):
        
        Test_ListMethods.test_remove(removevalue=1)
       
     
    def test_reverse_list(self):
        
        Test_ListMethods.test_reverse()

        
    def test_sort_list(self):
        
        Test_ListMethods.test_sort()

         
    def test_copy_deepcopy(self):
        
        Test_ListMethods.test_copy_deepcopy(list3=[], list4=[])
        
        
    def test_clear_list(self):
        
        Test_ListMethods.test_clear()

    def test_iterate_elements_using_for_loop(self):
        
        Test_ListMethods.test_iterate_elements_using_for_loop(listvalue=["apple","orange","watermelon","Bannana", "pineapple", "pomogranite", "Kiwi"])
        

def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(Test_List_Methods))
    #suite.addTest(unittest.TestLoader().loadTestsFromTestCase(ProfileEditionTest))
    #suite.addTest(unittest.TestLoader().loadTestsFromTestCase(EditAddressTest))
    #suite.addTest(unittest.TestLoader().loadTestsFromTestCase(CreatePostTest))
    runner = HTMLTestRunner(log=True, verbosity=2, output='report', title='Test report', report_name='report',
                        open_in_browser=True, description="HTMLTestReport", tested_by="Ravikirana B",
                        add_traceback=False)
    runner.run(suite)

if __name__ == '__main__':
    suite()
