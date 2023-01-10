#create a list of three fruits
fruit = ["banana", "strawberry", "apple"]

#output all the fruits in the list
print(fruit)

#output the second fruit in the list
print(fruit[1])

#create a set of three fruits
fruit_one = {"orange", "strawberry", "apple"}
fruit_two = {"banana", "pineapple", "kiwi"}
fruit_three = {"melon", "plum", "grapes"}

# create a list of the three sets
fruits = [fruit_one, fruit_two, fruit_three]

#add a new fruit to the set
fruit_one.add("dates")

# print the updated list of sets
print(fruits)

# add the same fruit again to the set
fruit_one.add("dates")

# print the updated list of sets
print(fruits)

#Creates a dictionary of three fruits with a corresponding price
fruits = {
    "apple": 0.5,
    "banana": 0.25,
    "orange": 0.75
}

# Output all the fruits in the dictionary
print(fruits.keys())

# Output the price of the second fruit in the dictionary
print(list(fruits.values())[1])

# For a given fruit, output its price if it is in the dictionary or a message if it is not in the list
fruit = "apple"
if fruit in fruits:
    print(fruits[fruit])
else:
    print(f"{fruit} is not in the list.")