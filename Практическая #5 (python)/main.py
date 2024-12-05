from library import Library
from books import Book
from reader import Reader

library = Library("Городская библиотека")
book1 = Book("1984", "George Orwell", 1949, "Dystopian")
book2 = Book("To Kill a Mockingbird", "Harper Lee", 1960, "Fiction")

library.add_book(book1)
library.add_book(book2)

reader = Reader("Лёха", 1)
library.register_reader(reader)
library.lend_book(book1, reader)


found_books = library.find_book(title="To Kill a Mockingbird")
print("Найденные книги:", [str(book) for book in found_books])

library.lend_book(book2, reader)
print("Книги, взятые читателем:", library.get_reader_books(reader))

library.return_book(book1, reader)
print("Книги, взятые читателем после возврата:", library.get_reader_books(reader))
