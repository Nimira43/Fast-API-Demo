# import requests
# book1 = requests.get('https://www.gutenberg.org/cache/epub/35/pg35.txt')
# print(book1)

import re

with open('./books/the-time-machine.txt', 'r', encoding='utf-8') as file:
  book_1 = file.read()

print('CHARACTERS: ', len(book_1))
print('FIRST 2000 CHARACTERS: ', book_1[:2000])

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
  
print('--------------------------------------')
print('MODIFIED CHARACTERS (FIRST 2000): ', book_1[:2000])