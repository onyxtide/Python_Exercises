#Learning about built-in list methods in Python

#Exercise: Suppose we want to add 'Pachinko' to the list. Can you use a list method to do so?
# Let's say we finished reading 'The Fault in Our Stars' and '1984'. Can you use the .remove() method to remove one and the .pop() method to remove the other?

books = ['Harry Potter', '1984', 'The Fault in Our Stars', 'The Mom Test', 'Life in Code']

books.append('Pachinko')
books.remove('The Fault in Our Stars')
books.pop(1)

print(books)
