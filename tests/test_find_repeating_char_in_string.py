import unittest

def find_repeating_char_in_string(str1=" ", freq_dict = {}, repeating_char =""):

        repeating_char = ""
        str1 = input("Please enter a string:")
        freq_dict = {}
        for char in str1:
            if char in freq_dict:
                freq_dict[char]+=1
            else:
                freq_dict[char] =1

        repeating_char =""

        for char in str1:
            if freq_dict[char]!=1:
                repeating_char +=char
        print("Repeating character:", repeating_char)
        print(freq_dict)

if __name__ == '__main__':
    find_repeating_char_in_string(str1=" ", freq_dict = {},repeating_char ="")
    unittest.main()