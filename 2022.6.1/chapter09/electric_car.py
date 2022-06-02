"""表示电动车的类"""

from car import Car


class Battery():
    """模拟电动汽车电瓶"""

    def __init__(self, battery_size=70):
        self.battery_size = battery_size

    def describe_battery(self):
        """打印电池容量的描述"""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

    def get_range(self):
        """打印出电瓶的续航里程"""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270

        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)

    def upgrade_battery(self):
        if self.battery_size != 85:
            self.battery_size = 85


class ElectricCar(Car):
    """电动车类"""

    def __init__(self, make, model, year):
        """
        初始化父类属性
        在初始化电动车特有属性
        """
        super().__init__(make, model, year)
        self.battery = Battery()

# my_tesla = ElectricCar('tesla', 'model s', 2016)
# print(my_tesla.get_descriptive_name())
# my_tesla.battery.describe_battery()
# my_tesla.battery.get_range()

# my_bugatti = ElectricCar('Bugatti', 'EB16.4', 2010)
#
# print("before update:")
# my_bugatti.battery.get_range()
#
# print("after update:")
# my_bugatti.battery.upgrade_battery()
# my_bugatti.battery.get_range()
