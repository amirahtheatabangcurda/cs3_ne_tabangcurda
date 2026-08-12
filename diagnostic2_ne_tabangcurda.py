def calculate_fuel(cargo_weight):
    total_weight = cargo_weight + 50000
    fuel_needed = total_weight * 3
    return fuel_needed 

while True:
    try:
        cargo = (input("Enter cargo you want to load: "))
        if cargo == "satellite" or cargo == "rover" or cargo == "supplies":
            print("Cargo loaded.")
            continue
        if total_cargo_weight > 10000:
            print ("ALERT! MAX WEIGHT REACHED!")
        break
    except cargo == "Launch":
        print("Launching cargo.")

        if cargo == "satellite":
            print ("Satellite loaded.") 
            total_cargo_weight = 50000 + 1000
        elif cargo == "rover":
            print ("Rover loaded")
            total_cargo_weight = 50000 + 2500
        elif cargo == "supplies": 
            print ("Supplies loaded.") 
            total_cargo_weight = 50000 + 500
        else:
            print ("Error! Item is not approved for the mission. Please enter valid item.")

        