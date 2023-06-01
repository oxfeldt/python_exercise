inventory = ["Axe", "Food", "Helmet"]
food = inventory[1]
inventory[1] = "fruit"

inventory[0:2]
first_two = inventory[0:2]

inventory.append("Water")
inventory.remove("Axe")
inventory.insert(1,"Globe")
print(inventory)
