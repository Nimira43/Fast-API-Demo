import numpy as np
import matplotlib.pyplot as plt
import re
import string

with open('./books/the-time-machine.txt', 'r', encoding='utf-8') as file:
  book_1 = file.read()

print('CHARACTERS: ', len(book_1))

strings_to_replace = [
  '\r\n\r\nâ\x80\x9c', 
  'â\x80\x9c',         
  'â\x80\x9d',         
  '\r\n',              
  'â\x80\x94',         
  'â\x80\x99',         
  'â\x80\x98',         
  '_',                
]

for strings_to_match in strings_to_replace :
  regular_expression = re.compile(r'%s' %strings_to_match)
  book_1 = regular_expression.sub(' ', book_1)

book_1 = re.sub(r'\s+', ' ', book_1)
book_1 = book_1.strip()

words = book_1.split()
print('NUMBER OF WORDS: ', len(words))
print('FIRST 50 WORDS: ', words[:50])

letters = string.ascii_lowercase
print('NUMBER OF LETTER A IN BOOK: ', book_1.count('a'))
print('NUMBER OF LETTER M IN BOOK: ', book_1.count('m'))
print('NUMBER OF LETTER X IN BOOK: ', book_1.count('x'))
print('NUMBER OF LETTER Z IN BOOK: ', book_1.count('z'))


























