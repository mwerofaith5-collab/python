
inventory = {
    "Laptop": 65,
    "Smartphone":78,
    "Headphones":5,
    "Monitor": 35,
    "Keyboard": 17
}
inventory["Mouse"] = 29
inventory["Monitor"] = 10 
def low_stock_items(inv):
    return [product for product, qty in inv.items() if qty < 10]
del inventory["Smartphone"]
for product, qty in inventory.items():
    print(f"{product}: {qty}")
print("Low stock products:", low_stock_items(inventory))
print("Updated inventory:", inventory)