class Reader:
    def __init__(self, name: str, ID: int):
        self.name = name
        self.ID = ID
        self.bookslist = []

    def __str__(self):
        books = "\n".join(str(book) for book in self.bookslist) if self.bookslist else "Пусто."
        return f"Имя - {self.name}\nID читателя - {self.ID}\nСписок взятых книг:\n{books}"
    
    def borrow_book(self, book):
        self.bookslist.append(book)
        print(f"Книга \"{book.title}\" выдана читателю \"{self.name}\"")

    def return_book(self, book):
        if book in self.bookslist:
            self.bookslist.remove(book)
            print(f"Книга \"{book.title}\" возвращена читателем \"{self.name}\"")
        else:
            print(f"Книга \"{book.title}\" не числится за читателем \"{self.name}\"")