class Library:
    def __init__(self, books, borrowers):
        self.books = books
        self.borrowers = borrowers

    def add_books(self, add_books):
        if add_books > 0:
            self.books += add_books
        return self.books

    def lend_books(self, borrowed_books):
        book = self.books
        if borrowed_books > 0:
            book -= borrowed_books

    def display_information(self):
        print(self.books)
        print(self.borrowers)


book_1 = Library(4000, 31)
print(book_1.add_books(300))
print(book_1.lend_books(30))

book_1.display_information()
