from restaurant import Restaurant

restaurant1 = Restaurant("QUANJUDE Peking Roast Duck", "Chinese food")
restaurant1.describe()
restaurant1.open_restaurant()
restaurant1.set_number_served(15)
print(restaurant1.restaurant_name + " served " + str(restaurant1.number_served) + " people.")

restaurant2 = Restaurant("Matsukawa", "Janpanese food")
restaurant2.describe()
restaurant2.open_restaurant()
restaurant2.increment_number_served(30)
print(restaurant2.restaurant_name + " served " + str(restaurant2.number_served) + " people.")

restaurant3 = Restaurant("A l'endroit", "French food")
restaurant3.describe()
restaurant3.open_restaurant()
