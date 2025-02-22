# import requests
# book1 = requests.get('https://www.gutenberg.org/cache/epub/35/pg35.txt')
# print(book1)

with open('./books/the-time-machine.txt', 'r', encoding='utf-8') as file:
  book1 = file.read()

print('CHARACTERS: ', len(book1))
print('FIRST 2000 CHARACTERS', book1[:2000])