# Mutable and Immutable in Python

### Let's Talk About Changeable and Unchangeable Things in Python.

Imagine you have a box of crayons. You can add more crayons to the box, take some out, or even change the order of the crayons. This box of crayons is like a changeable thing in Python, called a mutable object.

Now, imagine you have a chocolate bar. Once you break off a piece, you can't put it back. The chocolate bar is like an unchangeable thing in Python, called an immutable object.

## Mutable Objects
- Can be changed after they're created.
Examples: lists, dictionaries

```python

my_crayons = ["red", "blue", "green"]  # A list of crayons
my_crayons.append("yellow")  # Adding a new crayon
print(my_crayons)  # Output: ['red', 'blue', 'green', 'yellow']

```

## Immutable Objects
- Cannot be changed after they're created.
- Examples: strings, numbers, tuples

```python


chocolate_bar = "milk chocolate"
chocolate_bar = chocolate_bar + " with almonds"  # Creating a new string
print(chocolate_bar)  # Output: milk chocolate with almonds

```

Important: When you change a mutable object, you're actually changing the original object. But when you change an immutable object, you're creating a new object.

### Why does it matter?

- Understanding mutable and immutable objects is important because it helps you write correct and efficient Python code. For example, if you need to keep track of a list of items that can change, you'll use a mutable object (like a list). But if you need a value that will never change, you'll use an immutable object (like a string).