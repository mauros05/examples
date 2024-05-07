human = {
         "name": "Mauricio",
         "age": 25,
         "weight": 93,
         "height": 1.81,
         "glasses": True
         }

print(human.keys())
print(human.values())
print(human.items())

print(human.get("married", "The key married was not found"))