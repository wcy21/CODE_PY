prompt = "\nEnter your age, and I'll tell you the price of your movie tickets:"
prompt += "\n(Enter 'quit' to end the program.) "

while True:
    age = input(prompt)

    if age == 'quit':
        break

    age = int(age)
    if age < 3:
        print("> You can buy tickets for free.")
    elif age <= 12:
        print("> You need to pay $10 for the movie ticket.")
    else:
        print("> You need to pay $15 for the movie ticket.")
