"""表示汽车的类"""


class Car():
    """模拟汽车"""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """返回整洁的描述信息"""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        """打印汽车里程"""
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        """
        指定里程表读数
        禁止读数回调
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """里程表增加指定量"""
        if miles >= 0:
            self.odometer_reading += miles
        else:
            print("You can't roll back an odometer!")

# my_new_car = Car('audi', 'a4', '2016')
# print(my_new_car.get_descriptive_name())
#
# my_new_car.update_odometer(23500)
# my_new_car.read_odometer()
#
# my_new_car.increment_odometer(100)
# my_new_car.read_odometer()
