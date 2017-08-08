## Write a Python program that matches a word containing 'z'

import re

def match_wrd(string):
  match = re.findall(r'[z]', string)
  return bool(match)

print match_wrd("The quick brown fox jumps over the lazy dog.")
print match_wrd("Python Exercises.")