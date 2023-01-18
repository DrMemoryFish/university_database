# Creating a dictionary of three fruits with a corresponding price
fruits_dict = {
    "apple": 0.5, 
    "banana": 0.25, 
    "orange": 0.75
    }

# Outputting all the fruits in the dictionary
print(fruits_dict)

# Outputting the price of the second fruit in the dictionary
print(list(fruits_dict.items())[1][1])

# For a given fruit output its price if it is the dictionary or a message if it is not in the list
def fruit_price(fruit):
    # Check if the input is a string, if not raise a TypeError
    if not isinstance(fruit, str):
        raise TypeError("Input must be a string")
    # check if the input string is not empty
    elif not fruit:
        raise ValueError("Input string must not be empty")
    # check if the fruit is in the dictionary
    elif fruit in fruits_dict:
        return fruits_dict[fruit]
    else:
        return f"{fruit} is not in the list."

# Usage examples
print(fruit_price("apple")) # 0.5
print(fruit_price("banana")) # 0.25
print(fruit_price("orange")) # 0.75
print(fruit_price("mango")) # not in the list
