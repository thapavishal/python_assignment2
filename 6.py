# Search for the name ‘John’ using a for a loop

name = ["cena", "orton", "rock", "john", "hobbs", "cold", ]

for item in name:
    if item == "john":
        print("Hi john")
        break
else:
    print("Not found")
