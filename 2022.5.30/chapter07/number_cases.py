number = input("Enter a number, and I'll tell you if it's divisible by 10: ")
number = int(number)

if number % 10 == 0:
    print("\nThe number " + str(number) + " is divisible by 10.")
else:
    print("\nThe number " + str(number) + " is not divisible by 10.")
