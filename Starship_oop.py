class Cargo:
    def __init__(self):
        self.cargo_count = 0 

    def add_cargo(self):
        self.cargo_count += 1  
class Starship:
    def __init__(self, base_weight):
        self.base_weight = base_weight
        self.load = Cargo()  
        self.fuel_needed = 0  

    def calculate_fuel(self):
        total_weight = self.base_weight + (self.load.cargo_count * 1000)
        self.fuel_needed = total_weight * 3
        print("Total weight: ", total_weight)
        print("Fuel needed: ", self.fuel_needed)

    def display_info(self, name, model):
        print("Starship name: ", name)
        print("Starship model: ", model)
        print("Starship weight: ", self.base_weight)
        print("Cargo load: ", self.load.cargo_count)

starship = Starship(50000)
starship.load.add_cargo()
starship.load.add_cargo()
starship.load.add_cargo()
starship.calculate_fuel()



