word = input("introduce a word: ")

print("The word is: ", word)
print("The number of caracters is: ", len(word))

count = 0  # This variable will be used to hold the number of characters in the string.
# This for loop adds 1 to count for each character in user_str.
for char in word:
    count += 1
 
print(word)  
print(count)