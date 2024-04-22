numbers = range(1, 51)

for num in numbers:
    if num % 3 == 0 and num % 5 == 0:
        print("Fizz Buzz - " + str(num))
    elif num % 3 == 0:
        print("Fizz - " + str(num))
    elif num % 5 == 0:
        print("Buzz - " + str(num))
    else:
        print(num)
    