class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def get_summary(self):
        return f"'{self.title}' by {self.author}, published in {self.year}"

class Library(Book):
    def __init__(self, title, author, year, library_name):
        super().__init__(title, author, year)
        self.library_name = library_name

    def get_library_info(self):
        return f"{self.get_summary()} - Available at {self.library_name} Library"    
    
my_book = Library("1984", "George Orwell", 1949, "City Central")
print(my_book.get_library_info())
