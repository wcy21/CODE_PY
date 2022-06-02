from user import User
from admin import Admin, Privileges

user1 = User('happy', 'dog', 20)
user1.describe_user()
user1.greet_user()

admin = Admin('blue', 'dog', 20)
admin.greet_user()
admin.privileges.show_privileges()
