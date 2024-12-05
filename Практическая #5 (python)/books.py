class Book:
    def __init__(self, title: str, author: str, year: int, genre: str):
        self.title = title
        self.author = author
        self.year = year
        self.genre = genre

    def __str__(self) -> str:
        return f"Название - {self.title}\nАвтор - {self.author}\nГод - {self.year}\nЖанр - {self.genre}"

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Book):
            return (self.title == other.title and
                    self.author == other.author and
                    self.year == other.year and
                    self.genre == other.genre
            )
        return False
    

