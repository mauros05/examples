number = int(input("Please give me a number: "))

def factorial_number(input):
    number_range = range(input, 1, -1)
    returned = 1

    for num in number_range:
        returned *= num

    return returned

print(factorial_number(number))