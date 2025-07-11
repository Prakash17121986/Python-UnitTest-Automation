
import re
# Only numbers and words
string = "I was born on June 24"
print(string)
regex = "([a-zA-z]+) (\d+)"
a = re.search(regex, string)
print(a)
print(a.group(0))   
print(a.group(1))

#----------------------------------------------------------
# Only numbers and not words
regex = r"[a-zA-z]*\d+"
a = re.search(regex, string)
print(a)
print(a.group(0))  

#----------------------------------------------------------
# Only word and not numbers
regex = r"\w+"
a = re.findall(regex, string)
print(a)
b = ''.join(a)
print(b)

#----------------------------------------------------------
# Only word and not numbers
Nameage = '''Janice is 22 and Theon is 33 Gabriel is 44 and Joey is 21'''
print(Nameage)
regex = r"\w+"
a = re.findall(regex, Nameage)
print(a)

#----------------------------------------------------------
Nameage = '''Janice is 22 and Theon is 33 Gabriel is 44 and Joey is 21'''
regex = r"[A-Z][a-z]*"
print(Nameage)
a = re.findall(regex, Nameage)
print(a)
#----------------------------------------------------------
#Reapeating charcater
a = "abcabcdef"
print(a)
b = re.findall('abc+', a)
print(a)
print("repeating character",b)

#----------------------------------------------------------
# Non repeating character
a = "abcabcdef"
print(a)
c = re.search(r'[^abc]\w+', a)
print(c)
print("Non repeating character",c.group(0))


#----------------------------------------------------------
#search method
a = "Here is Edureka"  
print(a)       
b = re.search("Edureka",a)                    
print(a)
print(b.group(0))


#----------------------------------------------------------
a = "12345"
print(a)
b = re.match("\d+", a)                     
print(a)
print(b.group(0)) 


#----------------------------------------------------------
# \s - single whitespace
# S - Not whitespace
# \ escape character
# . Any character
# \d - digit
# \D - Non digit
# \w - word character
# \W - Non word character
# \b - word boundary
# \B - Not word boundary
# ^ - Begining of string
# $ - end of the string
# b = re.match('^[\s]*(.*?)[\s*]*$', a)
# ^ - start of the string
# \s - single white space
# [^abc] - Characters not in brackets are matched.
# () - capture the group
# . - any character
# * 0 or more
# ? 0 or 1
# + -  1 or more
# [] = single space match
# {min,max} - min char or max range of char

#----------------------------------------------------------
#^[\s]*(.*?)[\s]*$ matches the text by avoiding the extra spaces
a = "Hi I miss you so much"
print(a)
patt = r'(\w+\s*\w+\s*\w+\s*\w+\s*\w+\s*\w+$)'
b = re.match(patt, a)
print(b)
print(b.group(0))

#----------------------------------------------------------
#^[a-zA-Z0-9 ]*$ matches any alphanumeric with spaces.
a = "hello123"
print(a)
patt = r'[a-z0-9]*$'
b = re.match(patt, a)
print(b)
print(b.group(0))


#----------------------------------------------------------

#^(\d*)[.,](\d+)$ matches numbers like 12,3 or 12.3
a = "12,312.3"
patt = r'(\d+\,\d+\.\d+$)'
print(a)
b = re.match(patt, a)
print(b)
print(b.group(0))

#----------------------------------------------------------
# findall - match all the occurances of keyword and stored in list
a = 'abcabcdef'
print(a)
print(re.findall(r'\w\w\w',a))

a = 'abcdfeg'
print(a)
print(re.findall(r'\w\w|\w\w\w\w',a))

print(re.findall(r'\w\w',a))

#----------------------------------------------------------
#re.search(pattern, string, Flags)
# match at any place unlike re.match
# match at any place not just begining
import re
str1 = "I am IP guy"
print(re.search("am", str1))
print(re.search("am", str1).group())

#----------------------------------------------------------

# PS C:\Users\Anamika\Python_codes> & C:/Users/Anamika/AppData/Local/Programs/Python/Python310/python.exe c:/Users/Anamika/Python_codes/Project/tests/all_tests/Advanced_Python/test_re.py
# I was born on June 24
# <re.Match object; span=(14, 21), match='June 24'>
# June 24
# June
# <re.Match object; span=(19, 21), match='24'>
# 24
# ['I', 'was', 'born', 'on', 'June', '24']
# IwasbornonJune24
# Janice is 22 and Theon is 33 Gabriel is 44 and Joey is 21
# ['Janice', 'is', '22', 'and', 'Theon', 'is', '33', 'Gabriel', 'is', '44', 'and', 'Joey', 'is', '21']
# Janice is 22 and Theon is 33 Gabriel is 44 and Joey is 21
# ['Janice', 'Theon', 'Gabriel', 'Joey']
# abcabcdef
# abcabcdef
# repeating character ['abc', 'abc']
# abcabcdef
# <re.Match object; span=(6, 9), match='def'>
# Non repeating character def
# Here is Edureka
# Here is Edureka
# Edureka
# 12345
# 12345
# 12345
# Hi I miss you so much
# <re.Match object; span=(0, 21), match='Hi I miss you so much'>
# Hi I miss you so much
# hello123
# <re.Match object; span=(0, 8), match='hello123'>
# hello123
# 12,312.3
# <re.Match object; span=(0, 8), match='12,312.3'>
# 12,312.3
# abcabcdef
# ['abc', 'abc', 'def']
# abcdfeg
# ['ab', 'cd', 'fe']
# ['ab', 'cd', 'fe']
# <re.Match object; span=(2, 4), match='am'>
# am
# PS C:\Users\Anamika\Python_codes> 