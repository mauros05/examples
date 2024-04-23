called_mixed_case = "A song of Ice and Fire"

print(called_mixed_case.isupper())

print(called_mixed_case.islower())

print(called_mixed_case.upper())

print(called_mixed_case.lower())

print(called_mixed_case.istitle())

title = called_mixed_case.title()
print(title)

print(called_mixed_case.startswith("A"))  
print(called_mixed_case.endswith("e"))  
words = called_mixed_case.split()
print(words)  
print("".join(words).isalpha())  