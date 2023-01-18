def fruit_price(fruit):
    fruits = {
        "apple": 0.5,
        "banana": 0.25,
        "orange": 0.75
    }

    if fruit in fruits:
        return fruits[fruit]
    else:
        return f"{fruit} is not in the list."

# Usage examples
print(fruit_price("apple"))
print(fruit_price("banana"))
print(fruit_price("orange"))
print(fruit_price("pear"))