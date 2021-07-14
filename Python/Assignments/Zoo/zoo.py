class animal:
    def __init__(self, type, name):
        self.type = type
        self.name = name
    def display_info(self):
        print(f"This is a {self.type}, its name is {self.name}")        


class Zoo:
    def __init__(self, zoo_name):
        self.animals = []
        self.name = zoo_name
    def add_animal(self, type, name):
        self.animals.append(animal(type = type, name = name))
    def print_all_info(self):
        print("-"*30, self.name, "-"*30)
        for animal in self.animals:
            animal.display_info()
zoo1 = Zoo("John's Zoo")
zoo1.add_animal('lion', 'lol')
zoo1.add_animal('lion', 'olo')
zoo1.add_animal('tiger', "Rajah")
zoo1.add_animal('tiger', "Shere Khan")
zoo1.print_all_info()
