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