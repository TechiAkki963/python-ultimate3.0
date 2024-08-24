import random
fruits = ['apple','mango','orange','rasberry']
print(random.choice(fruits))
# 'rasberry'
print(random.choice(fruits))
# 'apple'
print(random.choice(fruits))
# 'apple'
print(random.choice(fruits))
# 'mango'
print(random.choice(fruits))
# 'mango'

print(random.shuffle(fruits))
print(random.shuffle(fruits))
print(fruits)
# ['mango', 'rasberry', 'orange', 'apple']

print(random.shuffle(fruits))
print(fruits)
# ['orange', 'rasberry', 'mango', 'apple']