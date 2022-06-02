from car import Car
from electric_car import ElectricCar

my_bettle = Car('volkswagen', 'beetle', 2016)
print(my_bettle.get_descriptive_name())

my_tesla = ElectricCar('tesla', 'roadster', 2016)
print(my_tesla.get_descriptive_name())
