class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def display_info(self):
        print(self.title, self.author, self.price)
        # print(self.author)
        # print(self.price)

    @staticmethod
    def price_calculator(books):
        total_price = 0
        for x in books:
            total_price += x.price
        return total_price


book_1 = Book("A Thousand Splendid Suns", "Khaled Hosseini", 250)
del book_1
book_2 = Book("ABC Thousand Splendid Suns", " Hosseini", 350)
book_3 = Book("wABC Thousand Splendid Suns", " Hosseini", 400)
book_4 = Book("xABC Thousand Splendid Suns", " Hosseini", 100)

book_collection = [book_2, book_3, book_4]
value = Book.price_calculator(book_collection)

print(value)
for book in book_collection:
    book.display_info()


# book_1 = Book("A Thousand Splendid Suns", "Khaled Hosseini", 250)
#
# title = "ML Architecture!"
# author = "S.M DOUMOUND"
# price = 23.90
# book_1.display_info(author, price)
# # book_2 = Book("Kite Runner", "Khaled Hosseini", 200)
# # book_3 = Book("Harry Potter and the Goblet of Fire", "JK Rowling", 275)
# # book_4 = Book("Game of Thrones", "G George", 280)
# # book_5 = Book("Harry Potter and the Philosopher's Stone", "JK Rowling", 250)
# # book_6 = Book("Six of Crows", "Martin Browning", 340)

