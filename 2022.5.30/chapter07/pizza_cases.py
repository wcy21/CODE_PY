prompt = "\nPlease add toppings to your pizza:"
prompt += "\n(Enter 'quit' to end the program) "

active = True
while active:
    topping = input(prompt)

    if topping == 'quit':
        active = False
    else:
        print("\nWe'll add " + topping + " to your pizza!")

print("\nOK, your pizza will be ready in a few moments.")
