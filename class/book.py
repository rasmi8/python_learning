
class laptop: 
    def __init__(self, brand, ram, price): 
        self.brand = brand 
        self.ram = ram 
        self.price = price 
    def show_specs(self): 
        print(self.brand, self.ram, self.price) 
l1= laptop('HP', 512, 2500) 
l1.show_specs()