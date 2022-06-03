import json


def read_number():
    """输入用户喜欢的数字"""
    number = input("Please enter your favorite number: ")
    number = int(number)
    filename = 'json/favorite_number.json'
    with open(filename, 'w') as f_obj:
        json.dump(number, f_obj)
    print("I remember this number!")


def load_number():
    """读取存储的数字并输出"""
    filename = 'json/favorite_number.json'
    try:
        with open(filename) as f_obj:
            number = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return number


def favorite_number():
    number = load_number()
    if number:
        print("I know your favorite number! It's " + str(number) + "!")
    else:
        read_number()


favorite_number()
