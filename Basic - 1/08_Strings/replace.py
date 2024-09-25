dc = "batman"
print(dc.replace("bat","super"))

print(dc)


pokemon = "pikachu, balbasaur, squirtle, charizad"
print(pokemon.split())  #['pikachu,', 'balbasaur,', 'squirtle,', 'charizad']

print(pokemon.split(", "))  #['pikachu', 'balbasaur', 'squirtle', 'charizad']


# Find

sentence = "The quick brown fox jumps over the lazy dog: A popular pangram that's often used for touch-typing practice, testing keyboards, and displaying fonts. It's been used since at least the late 19th century."

print(sentence.find("fox"))

print(sentence.count("s"))