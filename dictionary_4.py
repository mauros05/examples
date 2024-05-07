# Clear, Copy and Update

# CLEAR

example = {1: "England", 2: "France", 3: "Mexico"}
print(example)

example.clear()
print(example)

# COPY

example2 = {1: "England", 2: "France", 3: "Mexico"}
print(example2)
countrys = example2
countrys[3] = "Spain"
print(countrys)

# UPDATE
example3 = {1: "England", 2: "France", 3: "Mexico"}
city = {4: "USA"}
example3.update(city)

print(example3)
