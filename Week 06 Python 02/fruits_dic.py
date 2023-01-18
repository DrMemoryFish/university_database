#Creates a dictionary of three fruits with a corresponding price
def check_fruit_price(fruit):
    fruits = {
        "apple": 0.5,
        "banana": 0.25,
        "orange": 0.75
    }
    # Output all the fruits in the dictionary
    print(check_fruit_price.keys())

# Output the price of the second fruit in the dictionary
print(list(check_fruit_price.values())[1])

# For a given fruit, output its price if it is in the dictionary or a message if it is not in the list
#case where the fruit is in the dictionary
fruit = "apple"
if fruit in check_fruit_price:
    print(check_fruit_price[fruit])
else:
    print(f"{fruit} is not in the list.")

# For a given fruit, output its price if it is in the dictionary or a message if it is not in the list
#case where the fruit is not in the dictionary
fruit = "pear"
if fruit in check_fruit_price:
    print(check_fruit_price[fruit])
else:
    print(f"{fruit} is not in the list.")