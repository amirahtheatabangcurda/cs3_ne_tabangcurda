def calculate_checkout (cart_total, shipping_speed):
    if shipping_speed == "express":
        shipping_cost = 20
    elif shipping_speed == "overnight":
        shipping_cost = 35
    elif shipping_speed == "standard" and cart_total >= 100:
        shipping_cost = 0
    elif shipping_speed == "standard" and cart_total < 100:
        shipping_cost = 10
    else:
        print("Error. Please enter a valid shipping speed.")
        shipping_cost = 0
    return cart_total + shipping_cost

print(calculate_checkout(120, "overnight"))