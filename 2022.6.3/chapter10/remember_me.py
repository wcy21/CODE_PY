import json


def get_stored_username():
    """若存储了用户名，加载"""
    filename = 'json/username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username


def get_new_username():
    """提示输入用户名"""
    username = input("What is your name? ")
    filename = 'json/username.json'
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
    return username


def greet_user():
    """问候用户"""
    username = get_stored_username()
    if username:
        repeat = input("Is " + username + " your username? (yes/ no) ")
        if repeat == 'yes':
            print("Welcome back, " + username + "!")
        else:
            username = get_new_username()
            print("We'll remember you when you come back, " + username + "!")
    else:
        username = get_new_username()
        print("We'll remember you when you come back, " + username + "!")


greet_user()
