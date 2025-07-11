
import unittest

def test_find_nonrepeating_char_in_string(count=None, str1="", dict1={}):
        #find_nonrepeating_char("abcabcdef")
        # for loop method
        count = 0

        for i in str1:
            count = 0
            dict1 = {}
            for j in str1:
                if i ==j:
                    count+=1
                if count>1:
                    break
            if count ==1:
                print(f"Non repeating character: {i}, count: {count}")
                dict1.update({i:count})
                
                print("Non repeating character:",dict1)

def test_no_of_occurances_in_string(count=None, str1="", dict1={}):

    count = 0
    #dictionary method
    str1 = input("Please enter a string:")
    freq_dict = {}

    for char in str1:
        if char in freq_dict:
            freq_dict[char]+=1
        else:
            freq_dict[char] =1

    non_repeating_char =""
    for char in str1:
        if freq_dict[char]==1:
            non_repeating_char +=char

    print("No of occurance of each character:", non_repeating_char)
    print(freq_dict)


if __name__ == '__main__':
    test_find_nonrepeating_char_in_string(count=None, str1="", dict1={})
    test_no_of_occurances_in_string(count=None, str1="", dict1={})
    unittest.main()