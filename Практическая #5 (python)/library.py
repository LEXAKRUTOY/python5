class Library:
    def __init__(self, libraryname: str):
        self.libraryname = libraryname
        self.readerlist = []
        self.bookslist = []

    def add_book(self, book):
        self.bookslist.append(book)

    def remove_book(self, book):
        if book in self.bookslist:
            self.bookslist.remove(book)
        else:
            print("Книга отсутствует")

    def register_reader(self, reader):
        self.readerlist.append(reader)

    def lend_book(self, book, reader):
        if reader in self.readerlist:
            if book in self.bookslist:
                reader.borrow_book(book)
                self.bookslist.remove(book)
            else:
                print("Книга отсутствует в библиотеке")
        else:
            print("Читатель не существует")

    def return_book(self, book, reader):
        if book in reader.bookslist:
            reader.return_book(book)
            self.bookslist.append(book)
        else:
            print("У читателя отсутствует данная книга")

    def find_book(self, title=None, author=None):
        return [book for book in self.bookslist if
                (title and title.lower() in book.title.lower()) or
                (author and author.lower() in book.author.lower())]
                

    def get_reader_books(self, reader):
        if reader in self.readerlist:
            return [str(book) for book in reader.bookslist]
        else:
            print("Читатель не зарегистрирован")
            return []

    def __str__(self):
        return f"Library '{self.libraryname}' with {len(self.bookslist)} books and {len(self.readerlist)} readers."
