import unittest

# Function to produce infinite Fibonacci numbers
def fibonacci():
  # Generate first number
  a = 1
  yield a

  # Generate second number
  b = 1
  yield b

  # Infinite loop
  while True:
    # Return sum of a + b
    c = a + b
    yield c
    # Function resumes loop here on next call
    a = b
    b = c

# if __name__ == '__main__':
#     # Iterate through the Fibonacci sequence until a limit is reached
#     for num in fibonacci():
#         if num > 50:
#             break
#         print(num)
# 
#     # PS C:\Users\Anamika\Python_codes> & C:/Users/Anamika/AppData/Local/Programs/Python/Python310/python.exe c:/Users/Anamika/Python_codes/Project/tests/all_tests/DSA/test_generator_method.py
    # 1
    # 1
    # 2
    # 3
    # 5
    # 8
    # 13
    # 21
    # 34