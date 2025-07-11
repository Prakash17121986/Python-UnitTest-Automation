#Inbuilt-modules
import unittest
import copy


class Test_ListMethods(unittest.TestCase):
    
    # class variable
    msg = "Class List Methods"
    
    def test_class_msg(cls):
        return (cls.msg)
    
    # Parameterized constructor 
    def __init__(self, list1, list2):
        """
        A constructor is a special method used to initialize the state of an object when it is created.
        It is automatically called whenever a new object (instance) of a class is created.
        
        The primary purpose of the __init__ method is to initialize the attributes (data members) of the object.
        It can be default value or we can passed value as arguments during object creation.
        
        self is first parameter for this __init__ method
        
        Two types of constructor
        
        1. Default constructor - This type does not take any parameters other than self
        
        2. Parameterized constructor -This type accepts additional parameters besides self
        
        """
        self.list1 = list1 # instance variable
        self.list2 = list2 # instance variable

    # Instance Method
    def test_createlist(self):
        """
        This method to create a new list.

        Parameters:
            self: 
                    First Parameter  - self is first parameter for this instance method and no other parameters.
                    You can use self.variablename(instance variable) in any of class instance method once you declared the variable in constructor
                  
        Returns:
            list: it returns a new empty list using list().
        """
        print("""A list is a mutable, ordered collection of elements.
                Mutable means that you can change the elements of a list after it is created.
                Lists are defined using square brackets [] or list()""")
        self.list1 = list()
        print(f"Create a list: {self.list1}")
        
        
        if self.list1 == []:
            print("List created successfully using list() constructor method")
        else:
            print("List not created using list() constructor method")
        
    def test_append(self, value):
        """
        This method is to append the new value to the exisitng list.

        Parameters:
            self: 
                    First Parameter  - self is first parameter for this instance method 
                    second parameter - self.appendvalue(instance variable) second parameter for this instance method 
                  
        Returns:
            list: it returns a list with appended value.
        """
        
        print("Before append the list:", self.list1)
        
        self.value = value
        self.list1.append(value)
        
        print("After Append the list:", self.list1)
        
        if self.value in self.list1:
            print(f"{self.value} is appended successfully")
            print(f"{self.value} is exist in list")
        else:
            print(f"{self.value} is not appended successfully")
            

    def test_extend(self, value):
        """
        This method is to extend the new value to the exisitng list.

        Parameters:
            self: 
                    First Parameter  - self is first parameter for this instance method
                    second parameter - self.extendvalue(instance variable) second parameter for this instance method
                  
        Returns:
            list: it returns a list with extended value.
        """
        print(f"Before extend the list: {self.list1}")
        
        self.value = value
        self.list1.extend(value)
        
        print(f"After Extend the list: {self.list1}")
        
        for i in self.value:
            if i in self.list1:
                print(f"{i} is exist in list")
            else:
                print(f"{i} does not exist in list")
        
        
    def test_index(self, listvalue):
        """
        This method is going to return the index value for the given value in the list.

        Parameters:
            self: 
                    First Parameter  - self is first parameter for this instance method
                    second parameter - self.listvalue(instance variable) second parameter for this instance method
                  
        Returns:
            list: it returns a index value for the given value in the list.
        """
        print(f"list1: {self.list1}")
        
        self.listvalue = listvalue
        
        value = self.list1.index(listvalue)
    
        print(f"index: {value}, listvalue: {self.listvalue}")
        
        if value == 1:
            print(f"Index value: {value} for value: {listvalue}")
        else:
            print(f"index: {value} value is incorrect")
            
        
    def test_count(self, countvalue):
        """
        This method is going to return the count value for the given value in the list.

        Parameters:
            self: 
                    First Parameter  - self is first parameter for this instance method
                    second parameter - self.countvalue(instance variable) second parameter for this instance method
                  
        Returns:
            list: it returns a count value for the given value in the list.
        """
        
        print(f"list1: {self.list1}")
        
        self.countvalue = countvalue
        
        value = self.list1.count(self.countvalue)
        
        print(f"Count: {value}, value: {self.countvalue}")
        
        if value == 1:
            print(f"count: {value} value: {self.countvalue}")
        else:
            print(f"count: {value} value is incorrect")
            
    
    def test_insert(self,index, insertvalue):
        """
        This method is going to insert the new value for the given index in the list.

        Parameters:
            self: 
                    First Parameter  - self is first parameter for this instance method
                    second parameter - self.insertvalue(instance variable) second parameter for this instance method
                  
        Returns:
            list: it returns a list with insert value 100 and along with other values.
        """

        print(f"Before insert the value in list1: {self.list1}")
        
        self.insertvalue = insertvalue
        self.index = index
        self.list1.insert(index, insertvalue)
        print(f"After insert the value {self.value} in index value {self.index}")
        
        if self.insertvalue in self.list1:
            print(f"index: {self.index}, insertvalue: {self.insertvalue}, list1: {self.list1}")
        else:
            print(f"{self.insertvalue} does not exist in list")
        
#  
    def test_remove(self, removevalue):
        """
        This method is going to remove the specified value in the list.

        Parameters:
            self: 
                    First Parameter  - self is first parameter for this instance method
                    second parameter - self.removevalue(instance variable) second parameter for this instance method
                  
        Returns:
            list: it returns a list after removing the specified value.
        """
        print(f"Before remove the value in list1: {self.list1}")
        
        self.removevalue=removevalue
        
        self.list1.remove(removevalue)
        
    
        if self.removevalue not in self.list1:
              print(f"After remove the value {self.removevalue} from the list1: {self.list1}")
        else:
            print(f"Value {self.removevalue} not removed successfully from the list: {self.list1}")
        
        
    def test_reverse(self):
        """
        This method is going to reverse all the items in the list.

        Parameters:
            self: 
                    First Parameter  - self is first parameter for this instance method
                                      
        Returns:
            list: it returns a list of item in a reversed order
        """
        print(f"Before reverse the list1: {self.list1}")
        
        self.list1.reverse()
        
        if self.list1:
            print(f"After reverse the list1: {self.list1}")
        else:
            print(f"All items not reversed properly in list: {self.list1}")
        
    def test_sort(self):
        """
        This method is going to sort all the items in the list.

        Parameters:
            self: 
                    First Parameter  - self is first parameter for this instance method
                                      
        Returns:All items not reversed properly in list
            list: it returns a sorted list
        """
        print(f"Before sort the list1: {self.list1}")
        
        self.list1.sort()
    
        if self.list1:
            print(f"After sort the list1: {self.list1}")
        else:
            print(f"All items not sort properly in list: {self.list1}")
            
    
    def test_copy_deepcopy(self,list3,list4):
        """
        This method is going to copy the other list.

        Parameters:
            self: 
                    First Parameter  - self is first parameter for this instance method
                    second parameter - self.list3(instance variable) second parameter for this instance method
                    third parameter - self.list4(instance variable) second parameter for this instance method
                                      
        Returns:
            list: it returns a copied list
        """
        self.list1 = [1,2,3]
        self.list2 = []
        self.list3 = list3
        self.list4 = []
        
        print(f"list1: {self.list1}")
        print(f"list2: {self.list2}")
        print(f"list3: {self.list3}")
        print(f"list4: {self.list4}")
        
        # shallow copy, list1!=list3, Both address are different
        self.list2 = self.list1.copy()
        print(f"After copy list2: {self.list2}")
        self.list2.insert(0,10)
        
        print(f"After shallowcopy list2: {self.list2}")
        
        # copy object - list1==list3, Both address are same
        self.list3 = self.list1
        print(f"After copy list3: {self.list3}")
        
        print(f"id of list1: {id(self.list1)}")
        print(f"id of list2: {id(self.list2)}")
        print(f"id of list3: {id(self.list3)}")
        
        # deepcopy and deepcopy object, list1!=list4, Both address are different
        self.list4 = copy.deepcopy(self.list1)
        print(f"After deepcopy of list1: {self.list4}")
        self.list4.insert(0,100)
        
        print(f"After depcopy list4: {self.list4}")
        
        if self.list1!=self.list2:
            print(f"Both list1 and list2 ID's or reference Address not same: {id(self.list1)!=id(self.list2)}")
        
        if self.list1==self.list3:
            print(f"Both list1 and list3 ID's or reference Address same: {id(self.list1) == id(self.list3)}")
            
        if self.list1!=self.list4:
            print(f"Both list1 and list4 ID's or reference Address not same: {id(self.list1)!=id(self.list4)}")
        
    def test_clear(self):
        """
        This method is going to clear all the items in a list.

        Parameters:
            self: 
                    First Parameter  - self is first parameter for this instance method
                                      
        Returns:
            list: it returns a list after clear all the items
        """
        print(f"Before clear the list1: {self.list1}")
        
        self.list1.clear()
        
        if self.list1:
            print(f"After clear the list1: {self.list1}")
        else:
            print(f"All items not cleared properly in list: {self.list1}")
            
    def test_iterate_elements_using_for_loop(self, listvalue):
        """
        This method is to iterate the elements one by one in a list.

        Parameters:
            self: 
                    First Parameter  - self is first parameter for this instance method
                    second parameter - self.listvalue(instance variable) second parameter for this instance method
                                      
        Returns:
            list: Iterate element one by one in a list or sequence.
        """
        self.listvalue = listvalue
        
        print(f"listvalue: {self.listvalue}")
        
        print(f"Length of list: {len(self.listvalue)}")
        
        print(f"dir of list: {dir(self.listvalue)}")
        
        print(f"Positive Slicing: {self.listvalue[2:]}")
        
        print(f"Negative Slicing: {self.listvalue[::-1]}")
        
        # Iterate the elements in a sequence or list
        for item in self.listvalue:
            print(f"Accessing each item: {item}")
            
    def test_iterate_element_with_range_func_using_for_loop(self, listvalue):
        """
        This method is to iterate the elements one by one in a list using for loop.

        Parameters:
            self: 
                    First Parameter  - self is first parameter for this instance method
                    second parameter - self.listvalue(instance variable) second parameter for this instance method
                                      
        Returns:
            list: Iterate element one by one in a list or sequence.
        """
        self.listvalue = listvalue
        
        print(f"listvalue: {self.listvalue}")
        # using range and length function
        for num in range(len(self.listvalue)):
            print("Accessing element using range and length:", self.listvalue[num])
    
    def test_iterate_element_with_enumerate_func_using_for_loop(self, listvalue):
        """
        This method is to iterate the elements one by one in a list with enumerate function using for loop.

        Parameters:
            self: 
                    First Parameter  - self is first parameter for this instance method
                    second parameter - self.listvalue(instance variable) second parameter for this instance method
                                      
        Returns:
            list: Iterate element one by one in a list or sequence.
        """
        self.listvalue = listvalue
        
        print(f"listvalue: {self.listvalue}")
        # Enumerate function
        for indx, num in enumerate(self.listvalue):
            print("Accessing element using enumerate function:", indx, num)
            
    def test_for_loop_using_conditional_statement1(self, listvalue):
        """
        This method is to iterate the elements one by one in a list with enumerate function using for loop.

        Parameters:
            self: 
                    First Parameter  - self is first parameter for this instance method
                    second parameter - self.listvalue(instance variable) second parameter for this instance method
                                      
        Returns:
            list: Iterate element one by one in a list or sequence.
        """
        self.listvalue = listvalue
        
        print(f"listvalue: {self.listvalue}")
        # conditional statements
        for indx, value in enumerate(self.listvalue):
            if indx==0:
                pass
            print("Accessing element if indx == 0", indx, value)
    
    def test_for_loop_using_conditional_statement2(self, listvalue):
        """
        This method is to iterate the elements one by one in a list with enumerate function using for loop.

        Parameters:
            self: 
                    First Parameter  - self is first parameter for this instance method
                    second parameter - self.listvalue(instance variable) second parameter for this instance method
                                      
        Returns:
            list: Iterate element one by one in a list or sequence.
        """
        self.listvalue = listvalue
        
        print(f"listvalue: {self.listvalue}")
        for indx, value in enumerate(self.listvalue):
            if indx==2:
                break
            print("Accessing element if indx == 2", indx, value)
     
    def test_for_loop_using_conditional_statement3(self, listvalue):
        """
        This method is to iterate the elements one by one in a list with enumerate function using for loop.

        Parameters:
            self: 
                    First Parameter  - self is first parameter for this instance method
                    second parameter - self.listvalue(instance variable) second parameter for this instance method
                                      
        Returns:
            list: Iterate element one by one in a list or sequence.
        """
        self.listvalue = listvalue
        
        print(f"listvalue: {self.listvalue}")
        for indx, value in enumerate(self.listvalue):    
            if indx > 3:
                continue
            print("Accessing element if indx is less than 3:", indx, value)
    
    def test_iterate_element_with_positive_slicing_using_for_loop(self, listvalue):
        self.listvalue = listvalue
        
        print(f"listvalue: {self.listvalue}")
        # Iterate the elements using positive slicing in a sequence or list
        for item in range(0, len(self.listvalue), 2):
            print(f"Positive slicing - Accessing each item: {item} {self.listvalue[item]}")
        
        
        
        
# Creating objects using the constructor
# obj = Test_ListMethods([1,2,3], [4,5,6]) # Object instantatiation
#print(Test_ListMethods.test_class_msg)
# obj.test_createlist() # Accessing instance methods using object
# obj.test_append(value=40)
# obj.test_extend(value=[1,2,3])
# obj.test_index(value=2)
# obj.test_count(value=1)
# obj.test_insert(index=0, value=100)
# obj.test_remove(value=40)
# obj.test_reverse()
# obj.test_sort()
# obj.test_copy()
# obj.test_clear()
#if __name__ == '__main__':
    #unittest.main()
