friends = (
    {"name": "Rolf Smith", "age": 24},
    {"name": "Adam Wool", "age": 30},
    {"name": "Anne Pun", "age": 27}
)
print(friends[0]["name"]) # her ændre du tallet til den person du vil have og
# eller ændre navn til age hvis du hellere vil have alderen


friends = [("Rolf", 24), ("Adam", 30), ("Anne", 27)]
frineds_ages = dict(friends)
print(frineds_ages)