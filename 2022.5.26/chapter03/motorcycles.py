motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

motorcycles.append('honda')
print(motorcycles)

motorcycles.insert(0, 'kaier')
print(motorcycles)

del motorcycles[0]
print(motorcycles)

popped_motorcycle = motorcycles.pop(2)
print(motorcycles)
print(popped_motorcycle)

last_owned = motorcycles.pop()
print("The last motorcycle I owned was a " + last_owned.title() + ".")

too_expensive = 'yamaha'
motorcycles.remove(too_expensive)
print(motorcycles)
print("A " + too_expensive.title() + " is too expensive for me.")
