# Creating sets using curly braces
fruits = {"apple", "banana", "orange"}
numbers = {1, 2, 3, 4}

# Creating sets using the set() constructor
colors = set(["red", "green", "blue"])
mixed_set = set([1, "hello", 3.14])


# Accesing Elements in Sets
if "apple" in fruits:
    print("Apple is in the set.")
else:
    print("Apple is not in the set.")

# Modifying Sets
fruits.add("grapes")    
print(fruits)

# Removing Sets
fruits.remove("banana")
print(fruits)

# Updating in Sets
berries = {"rasberry","blueberry","strawberry"}
fruits.update(berries)
print(fruits)

# Clearing Sets
fruits.clear()
print(fruits)