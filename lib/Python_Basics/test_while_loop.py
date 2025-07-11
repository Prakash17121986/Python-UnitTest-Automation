

import unittest

class test_while_loop():
    #With the while loop we can execute a set of statements as long as a condition is true
    def test_while_loop_break(self, i):
        self.i = i
        print(f"while loop with break statement: i, {i}")
        while self.i < 6:
            print("Candy")
            if self.i == 3:
                break #With the break statement we can stop the loop even if the while condition is true
                
            self.i+=1
        print("Bye")

    def test_while_loop_continue(self, i):
        self.i = i
        print(f"while loop with continue statement: i, {i}")
        while self.i < 6:
            self.i+=1
            if self.i == 3:
                continue #With the continue statement we can stop the current iteration, and continue with the next
            print(i)

    def test_while_loop_else(self, i):
        self.i = i
        print(f"while loop with else condition: i, {i}")
        while i < 6:
            print(i)
            i += 1
        else: #With the else statement we can run a block of code once when the condition no longer is true:
            print("i is no longer less than 6")
                        

if __name__ == '__main__':
    obj = test_while_loop()
    obj.test_while_loop_break(1)
    obj.test_while_loop_continue(1)
    obj.test_while_loop_else(1)
    unittest.main()

    # PS C:\Users\Anamika\Python_codes> & C:/Users/Anamika/AppData/Local/Programs/Python/Python310/python.exe c:/Users/Anamika/Python_codes/Project/tests/all_tests/Python_Basics/test_while_loop.py
    # while loop with break statement: i, 1
    # Candy
    # Candy
    # Candy
    # Bye
    # while loop with continue statement: i, 1
    # 1
    # 1
    # 1
    # 1
    # while loop with else condition: i, 1
    # 1
    # 2
    # 3
    # 4
    # 5
    # i is no longer less than 6

    # ----------------------------------------------------------------------
    # Ran 0 tests in 0.000s

    # OK
    # PS C:\Users\Anamika\Python_codes> 