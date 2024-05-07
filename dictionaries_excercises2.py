bands = {
         "Queen": "Bohemian Rhapsody", 
         "Bee Gees": "Stayin' Alive", 
         "U2": "One", 
         "Michael Jackson": "Billie Jean", 
         "The Beatles": "Hey Jude", 
         "Bob Dylan": "Like A Rolling Stone"
         }

print(len(bands))

for key in bands.keys():
    print(key)

print(bands.values())

for key, values in bands.items():
    print(key,values)

print(bands.get("Promise of the Real", "That is not a key that appears in the dictionary."))