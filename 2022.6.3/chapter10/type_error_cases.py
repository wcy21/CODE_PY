print("Enter two numbers to get their sum:")

while True:
    first_number = input("\nFirst Number: ")
    second_number = input("Second Number: ")

    try:
        result = int(first_number) + int(second_number)
    except ValueError:
        print("Input Error! Please enter again!")
    else:
        print("Sum = " + str(result))
        break
