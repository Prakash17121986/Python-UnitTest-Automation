
import unittest
import re

def test_file_read_write(string_input="", words =[]):
    string_input = "Hello Dude how are you! are you in bangalore" 
    
    #filepath = r"C:\Users\Anamika\Python_codes\simpletext.txt"                                                                                                   
    with open(r"C:\Users\Anamika\Python_codes\simpletext.txt", "w") as f:
        f.write(string_input)
        f.writelines("Where are you")
    
    #print(re.findall('\w+', open(r'C:\Users\Anamika\Python_codes\simpletext.txt').read()))
    #word = re.findall('\w+', open(r'C:\Users\Anamika\Python_codes\simpletext.txt').read())
    #print(word, len(word))
    
    with open(r"C:\Users\Anamika\Python_codes\simpletext.txt", "r") as h:
        for word in h.read().lower().split(" "):
            words.append({word,len(re.findall(h.read().lower(), word))} )
    
    print(words)
    
if __name__ == '__main__':
    test_file_read_write(string_input="Hello Dude how are you! are you in bangalore", words =[])
    unittest.main()