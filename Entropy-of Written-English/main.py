import numpy as np
import matplotlib.pyplot as plt
import re

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

print('CLEANED UP TEXT (FIRST 100 CHARACTERS): ', book_1[:100])

words = book_1.split()
print('NUMBER OF WORDS: ', len(words))
print('FIRST 50 WORDS:', words[:50])

word_lengths = np.zeros(len(words))

for word_pos in range (len(words)):
  word_lengths[word_pos] = len(words[word_pos])

plt.hist(word_lengths, bins=30)
plt.xlabel('Word lengths')
plt.ylabel('Word count')
plt.show()





















