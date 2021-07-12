class Product:
    def __init__(self, name, price, category, unique_id) -> None:
        self.name = name
        self.price = price
        self.category = category
        self.unique_id = unique_id

    def update_price(self, percent_change, is_increased):
        if is_increased:
            self.price *= 1 + percent_change
        else:
            self.price *= 1 - percent_change
        return self

    def print_info(self):
        print(f"The product {self.name} in category {self.category} is at price {self.price}")

if __name__ == "__main__":
    print("the file is being executed directly")
else:
    print("The file is being executed because it is imported by another file. The file is called: ", __name__)