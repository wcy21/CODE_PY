numbers = [number for number in range(3, 31, 3)]

for number in numbers:
    print(number)

print("The first three items in the list are:")
print(numbers[:3])

print("Four items from the middle of the list are:")
print(numbers[3:7])

print("The last three items in the list are:")
print(numbers[-3:])
