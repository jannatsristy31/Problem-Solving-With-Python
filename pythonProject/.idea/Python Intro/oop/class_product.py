class Product:
    def __init__(self, name):
        self.name = name
        self.price = 0
        self.quantity = 0

    def add_stock(self, new_stock):
        self.quantity += new_stock

    def sell_products(self, items_sold):
        self.quantity -= items_sold

    def add_price(self, price_add):
        self.price = price_add

    def display_information(self):
        # print(self.name)
        # print(self.price)
        # print(self.quantity)
        print(f"Name : {self.name}, Price : {self.price}, Quantity : {self.quantity}")


product = Product("Earring")
# product.add_price(200)
# product.add_stock(300)
product.sell_products(5)
product.sell_products(3)
product.add_stock(8)

product.display_information()
