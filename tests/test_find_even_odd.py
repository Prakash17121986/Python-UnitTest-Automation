
import unittest

#Even or Odd Program
def test_even_odd(num):
    for i in range(num):
        if i%2==0:
            print(f"Even Number: {i}")
        else:
            print(f"Odd Number: {i}")

def test_list_comhrension_method(num):
    even_numbers = [i for i in range(num) if i%2==0]
    odd_numbers  = [i for i in range(num) if i%2!=0]

    return even_numbers, odd_numbers
    

def test_list_comhrension_method1(num):
    obj = ["Even" if i%2==0 else "odd" for i in range(num)]

    for key,value in enumerate(obj):
        print ("{} is {} number".format(key,value))

    obj1 = [(i, "Even") if i%2==0 else (i, "odd") for i in range(num)] 
    print(f'list_comhrension_method using tuple Method: {obj1}')

    obj2 = {i:"even" if i%2==0 else "odd" for i in range(num)}
    print(f'list_comhrension_method using dictionary Method: {obj2}')

    obj3 = [(i,"even" if i%2==0 else "odd") for i in range(num)]
    print(f'list_comhrension_method using string Method: {obj3}')

    obj4 = [f"{i} is Even" if i%2==0 else f"{i} is odd" for i  in range(num)]
    print('list_comhrension_method using fstring Method:', ''.join(obj4), end='\n')


def test_list_comprehension_filter(num):
    evens = list(filter(lambda n: n % 2 == 0, [1,2,3,4,5,6,7,8]))
    odds = list(filter(lambda n: n % 2 != 0, [1,2,3,4,5,6,7,8]))
    return evens, odds

def test_for_loop_even_odd(num):
    evens, odds = [], []

    for n in num:
        evens.append(n) if n % 2 == 0 else odds.append(n)
    
    print(f'even number using for loop: {evens}')
    print(f'odd number using for loop: {odds}')

def test_while_loop_even_odd(num):
    evens, odds, i = [], [], 0

    while i < len(num):
        evens.append(num[i]) if num[i] % 2 == 0 else odds.append(num[i])
        i += 1

    print(f'even number using while loop: {evens}')
    print(f'odd number using while loop: {odds}')


def test_list_counter_method(num):
    # Creating a list of numbers
    num = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    # Initializing counters for even and odd numbers
    even = 0
    odd = 0

    for num in num:
    
        # Checking if the number is even
        if num % 2 == 0:  
            even += 1
        else:  
            odd += 1

    # Printing the results
    print(f'even number using by count method: {even}')
    print(f'odd number using by count method: {odd}')

def test_list_collections_counter_method(num):

    from collections import Counter

    num = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    # Counting even and odd numbers using Counter
    counts = Counter(['even' if num % 2 == 0 else 'odd' for num in num])

    # Printing the results
    print("Count the Even numbers using counter method:", counts['even'])
    print("Count the Odd numbers using counter method:", counts['odd'])


def test_list_filter_lambda_method(num):
    num = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    # Counting even numbers using filter and lambda
    even_count = len(list(filter(lambda num: num % 2 == 0, num)))

    # Counting odd numbers using filter and lambda
    odd_count = len(list(filter(lambda num: num % 2 != 0, num)))

    # Printing the results
    print("Count the Even numbers using filter and lambda method:", even_count)
    print("Count the Odd numbers using filter and lambda method:", odd_count)

# if __name__ == '__main__':
#     test_even_odd(30)
#     even, odd = test_list_comhrension_method(30)
#     print(f'even numbers using list comphrension method: {even}')
#     print(f'odd numbers using list comphrension method: {odd}')
#     test_list_comhrension_method1(20)
#     even_num, odd_num = test_list_comprehension_filter([1,2,3,4,5,6,7,8])
#     print(f'even numbers using list comphrension method: {even_num}')
#     print(f'odd numbers using list comphrension method: {odd_num}')
#     test_for_loop_even_odd([1,2,3,4,5,6,7,8])
#     test_while_loop_even_odd([1,2,3,4,5,6,7,8])
#     test_list_counter_method([1,2,3,4,5,6,7,8])
#     test_list_collections_counter_method([1,2,3,4,5,6,7,8])
#     test_list_filter_lambda_method(30)
#     unittest.main()
# 
#     # ====================Program Output=================================
    # PS C:\Users\Anamika\Python_codes> & C:/Users/Anamika/AppData/Local/Programs/Python/Python310/python.exe c:/Users/Anamika/Python_codes/Project/tests/all_tests/DSA/test_find_even_odd.py
    # Even Number: 0
    # Odd Number: 1
    # Even Number: 2
    # Odd Number: 3
    # Even Number: 4
    # Odd Number: 5
    # Even Number: 6
    # Odd Number: 7
    # Even Number: 8
    # Odd Number: 9
    # Even Number: 10
    # Odd Number: 11
    # Even Number: 12
    # Odd Number: 13
    # Even Number: 14
    # Odd Number: 15
    # Even Number: 16
    # Odd Number: 17
    # Even Number: 18
    # Odd Number: 19
    # Even Number: 20
    # Odd Number: 21
    # Even Number: 22
    # Odd Number: 23
    # Even Number: 24
    # Odd Number: 25
    # Even Number: 26
    # Odd Number: 27
    # Even Number: 28
    # Odd Number: 29
    # even numbers using list comphrension method: [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28]
    # odd numbers using list comphrension method: [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29]
    # 0 is Even number
    # 1 is odd number
    # 2 is Even number
    # 3 is odd number
    # 4 is Even number
    # 5 is odd number
    # 6 is Even number
    # 7 is odd number
    # 8 is Even number
    # 9 is odd number
    # 10 is Even number
    # 11 is odd number
    # 12 is Even number
    # 13 is odd number
    # 14 is Even number
    # 15 is odd number
    # 16 is Even number
    # 17 is odd number
    # 18 is Even number
    # 19 is odd number
    # list_comhrension_method using tuple Method: [(0, 'Even'), (1, 'odd'), (2, 'Even'), (3, 'odd'), (4, 'Even'), (5, 'odd'), (6, 'Even'), (7, 'odd'), (8, 'Even'), (9, 'odd'), (10, 'Even'), (11, 'odd'), (12, 'Even'), (13, 'odd'), (14, 'Even'), (15, 'odd'), (16, 'Even'), (17, 'odd'), (18, 'Even'), (19, 'odd')]
    # list_comhrension_method using dictionary Method: {0: 'even', 1: 'odd', 2: 'even', 3: 'odd', 4: 'even', 5: 'odd', 6: 'even', 7: 'odd', 8: 'even', 9: 'odd', 10: 'even', 11: 'odd', 12: 'even', 13: 'odd', 14: 'even', 15: 'odd', 16: 'even', 17: 'odd', 18: 'even', 19: 'odd'}
    # list_comhrension_method using string Method: [(0, 'even'), (1, 'odd'), (2, 'even'), (3, 'odd'), (4, 'even'), (5, 'odd'), (6, 'even'), (7, 'odd'), (8, 'even'), (9, 'odd'), (10, 'even'), (11, 'odd'), (12, 'even'), (13, 'odd'), (14, 'even'), (15, 'odd'), (16, 'even'), (17, 'odd'), (18, 'even'), (19, 'odd')]
    # list_comhrension_method using fstring Method: 0 is Even1 is odd2 is Even3 is odd4 is Even5 is odd6 is Even7 is odd8 is Even9 is odd10 is Even11 is odd12 is Even13 is odd14 is Even15 is odd16 is Even17 is odd18 is Even19 is odd
    # even numbers using list comphrension method: [2, 4, 6, 8]
    # odd numbers using list comphrension method: [1, 3, 5, 7]
    # even number using for loop: [2, 4, 6, 8]
    # odd number using for loop: [1, 3, 5, 7]
    # even number using while loop: [2, 4, 6, 8]
    # odd number using while loop: [1, 3, 5, 7]
    # even number using by count method: 4
    # odd number using by count method: 5
    # Count the Even numbers using counter method: 4
    # Count the Odd numbers using counter method: 5
    # Count the Even numbers using filter and lambda method: 4
    # Count the Odd numbers using filter and lambda method: 5

    # ----------------------------------------------------------------------
    # Ran 0 tests in 0.000s

    # OK
    # PS C:\Users\Anamika\Python_codes> 