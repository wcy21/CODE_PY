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


class IceCreamStand(Restaurant):
    """模拟冰淇淋类"""

    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['vanilla', 'blueberry', 'watermelon']

    def show_flavors(self):
        print("The flavors of ice-cream are as follows:")
        for flavor in self.flavors:
            print("- " + flavor + " flavored")


ice_cream_stand1 = IceCreamStand("blue dog ice-cream", "ice land")
ice_cream_stand1.show_flavors()
