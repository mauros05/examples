import copy

numbers = [1, 2, 3, 4, 5]
other_numbers = copy.deepcopy(numbers)

other_numbers[0] = 6

print(numbers)
print(other_numbers)