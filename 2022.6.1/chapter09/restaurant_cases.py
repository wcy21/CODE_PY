class Restaurant():
    """模拟餐馆"""

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe(self):
        """描述餐馆"""
        print("\nRestaurant Description:")
        print("- The name of the restaurant is " + self.restaurant_name + ".")
        print("- The restaurant's cuisine is " + self.cuisine_type + ".")

    def open_restaurant(self):
        """餐馆开门"""
        print("" + self.restaurant_name + " is open!")

    def set_number_served(self, number):
        """设置就餐人数"""
        self.number_served = number

    def increment_number_served(self, number):
        """增加就餐人数"""
        self.number_served += number


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
