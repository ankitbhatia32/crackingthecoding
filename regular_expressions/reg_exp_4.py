# Python program to remove initial extra zeros in regular expressions 

import re

def match_wrd(string):
  match = re.sub(r'\.[0]*','.', string)
  return match

print match_wrd("000.0112.0000231.0123")
# print match_ wrd("Python Exercises")
