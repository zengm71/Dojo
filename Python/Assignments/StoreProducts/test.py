from product import Product
from store import Store

store0 = Store(name = 'Store0')
product0 = Product(name = "product0", price = 100, category="category0", unique_id = 0)
product1 = Product(name = "product1", price = 5000, category="category0", unique_id = 1)
product2 = Product(name = "product2", price = 200, category="category1", unique_id = 2)

store0.add_product(new_product = product0)
store0.sell_product(unique_id = 0)
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
