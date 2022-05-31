def make_car(car_producer, car_type, **car_info):
    car = {'producer': car_producer, 'type': car_type}
    for key, value in car_info.items():
        car[key] = value
    return car
