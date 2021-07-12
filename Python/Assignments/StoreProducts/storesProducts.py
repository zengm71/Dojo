class Product:
    def __init__(self, name, price, category) -> None:
        self.name = name
        self.price = price
        self.category = category

    def update_price(self, percent_change, is_increased):
        if is_increased:
            self.price *= 1 + percent_change
        else:
            self.price *= 1 - percent_change
        return self

    def print_info(self):
        print(f"The product {self.name} in category {self.category} is at price {self.price}")

class Store:
    def __init__(self, name) -> None:
        self.name = name
        self.products = []

    def add_product(self, new_product):
        self.products.append(new_product)

    def sell_product(self, id):
        product_sold = self.products.pop(id)
        product_sold.print_info()

    def inflation(self, percent_increase):
        for product in self.products:
            product.update_price(percent_increase, True)

    def set_clearance(self, category, percent_discount):
        for product in self.products:
            if product.category == category:
                product.update_price(percent_discount, False)

store0 = Store(name = 'Store0')
product0 = Product(name = "product0", price = 100, category="category0")
product1 = Product(name = "product1", price = 5000, category="category0")
product2 = Product(name = "product2", price = 200, category="category1")
store0.add_product(new_product = product0)
store0.sell_product(id = 0)
store0.add_product(new_product = product0)
store0.add_product(new_product = product1)
store0.add_product(new_product = product2)

store0.inflation(percent_increase=.05)
store0.products[0].print_info()
store0.products[1].print_info()
store0.products[2].print_info()

store0.set_clearance(category='category0', percent_discount=.5)
store0.products[0].print_info()
store0.products[1].print_info()
store0.products[2].print_info()

product0.update_price(percent_change=.5, is_increased=True)
product0.print_info()
store0.products[0].print_info()
