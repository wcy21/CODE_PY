favorite_numbers = {
    'blue_dog': [1, 6, 2],
    'friendA': [0, 9],
    'friendB': [5, 16, 29],
    'friendC': [1, 66, 799],
    'friendD': [7, 8, 12, 18, 25, 67]
}

for name, numbers in favorite_numbers.items():
    print("\n" + name + "'s favorite numbers:")

    for number in numbers:
        print("\t" + str(number))
