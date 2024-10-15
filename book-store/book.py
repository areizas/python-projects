class Book:
  def __init__(self, title, author, isbn):
    self.title = title
    self.author = author
    self.isbn = isbn
    self.is_available = True

  def borrow(self):
    if(self.is_available):
      self.is_available = False
      print(f"The book {self.title} has been borrowed.")
      return True
    else:
      print(f"The book {self.title} is not available.")
      return False

  def return_book(self):
    if(not self.is_available):
      self.is_available = True
      print(f"The book {self.title} has been returned.")
      return True
    else:
      print(f"The book {self.title} was already available.")
      return False

if __name__ == "__main__":
  book = Book(title="title",author="author",isbn="1234abc")

  book.borrow()
  book.borrow()
  book.return_book()
  book.return_book()
