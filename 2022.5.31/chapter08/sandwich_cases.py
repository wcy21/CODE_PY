def make_sandwich(*toppings):
    print("\nMaking a sandwich with the following toppings.")
    for topping in toppings:
        print("- " + topping)


make_sandwich('sandwich')
make_sandwich('toast', 'cheese', 'ham')
make_sandwich('egg', 'bread', 'tomato', 'carrot')
