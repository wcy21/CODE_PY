current_users = ['tiramisu', 'blue_dog', 'admin', 'admins', 'none']
new_users = ['Blue_Dog', 'tiRamiSU', 'blue_Dog_2022', 'Admin123']

for user in new_users:
    if user.lower() in current_users:
        print("'" + user + "' is already in use.")
    else:
        print("You can use name '" + user + "'.")
