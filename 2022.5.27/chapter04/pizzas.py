pizzas = ['菠萝披萨', '鸡肉披萨', '鲜虾披萨']
for pizza in pizzas:
    print("I like " + pizza)

print("I like pizza")

friend_pizzas = pizzas[:]

pizzas.append('火腿披萨')
friend_pizzas.append('培根披萨')

print("My favorite pizzas are:")
for pizza in pizzas:
    print(pizza)

print("My friend's favorite pizzas are:")
for friend_pizza in friend_pizzas:
    print(friend_pizza)
