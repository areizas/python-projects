from book import Book

class Patron:
  def __init__(self,name,patron_id):
    self.name = name
    self.patron_id = patron_id
    self.borrowed_books = []

  def borrow_book(self, book):
    if(book.borrow()):
      self.borrowed_books.append(book)
      print(f"Patron {self.name} borrowed \"{book.title}\"")
    else:
      print(f"Patron {self.name} was not able to borrow \"{book.title}\"")
  
  def return_book(self, book):
    if book in self.borrowed_books:
      if(book.return_book()):
        self.borrowed_books.remove(book)
        print(f"Patron {self.name} returned \"{book.title}\"")
    else:
      print(f"Patron {self.name} has not borrowed the book \"{book.title}\"")
    
if __name__ == '__main__':
  b1 = Book(title="b1",author="a1",isbn="ba11")
  b2 = Book(title="b2",author="a1",isbn="ba21")
  b3 = Book(title="b3",author="a2",isbn="ba32")

  p = Patron(name="p1",patron_id="1")

  p.borrow_book(b1)
  p.borrow_book(b1)
  p.borrow_book(b2)
  p.return_book(b1)
  p.return_book(b3)
  p.return_book(b1)
  p.return_book(b3)