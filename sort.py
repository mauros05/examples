beatles_names = ["George", "Ringo", "John", "Paul"]
beatles_names.sort(reverse=True)
print(beatles_names)


beatles_names.sort(key=str.lower)
print(beatles_names)

# Excercise for lists

arctic_animals = ["penguin", "elephant", "polar bear", "walrus", "tiger", "reindeer"]
del arctic_animals[4]
arctic_animals.remove("elephant")
arctic_animals.append("arctic fox")
arctic_animals.insert(2, "snowy owl")  
arctic_animals.sort()  
print(arctic_animals)
print(arctic_animals.index("reindeer"))
print(arctic_animals.pop())