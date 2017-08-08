# Regular Expressions in Python

import re # This is the regular expression library we are importing


# Note: Python REGULAR EXPRESSIONS are case sensitive
# This is the split function in RE.
# Now this is the simple but we can perform many thing with
print re.split(r'\s*', 'Hello from the other sides')

print re.split(r'(\s*)', 'No hi from this side')

# Here we are split out string with character 'h' in the the string
print re.split(r'(h*)', 'Hey there how are you')

# Here we are separating or break up out a range of characters.
# This example suggests that split characters 'a' through 'f'
print re.split(r'[a-f]', 'afknsd;cuen;akdnfsadkjdscemo;erfjnAFTWKLKDN!', flags=re.I|re.M)

# We can add the flags after the string input
# Here we have added flag 're.I', this ignore the case sensitivity
# and re.M suggests to carry operation on multiple lines
print re.split(r'[a-f][a-f]', 'afknsd;cuen;akdnfsadkjdscemo;erfjnAFTWKLKDN!', flags=re.I|re.M)

# we can use findall function to find the pattern

print re.findall(r'\d', 'asdfi;2415csdjn;jidjf') # '\d' finds all the digits

print re.findall(r'\d{1,3}', 'asdfi;2415csdjn; jidjf') # we can define the range of digits i.e. '\d{1,5}'



# Here we want to get digits plus a space plus full name.
# '\s' represents space, '\w' represents aplhanumberic characters. '+' signs represents the full aplha numeric word i.e. main here
print re.findall(r'\d{1,4}\s\w+', 'asdfi;2415 main st.')

# Now this will only find till main but what if need to have further i.e. another space
print re.findall(r'\d{1,4}\s\w+\s\w+\.', 'asdfi;2415 main st.iwoeir13')



print re.findall(r'\D', 'asdfi;2415csdjn; jidjf') # '\D' finds all the non-digits, including special characters & spaces

print re.findall(r'\S', 'asdfi;2415csdjn; jidjf') # '\S' finds all the non-spaces