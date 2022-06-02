class User():
    """模拟用户"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def describe_user(self):
        """打印用户信息摘要"""
        print("\nSimple User Information:")

        print("- username: " + self.first_name + ' ' + self.last_name)
        print("- age: " + str(self.age))

    def greet_user(self):
        """向用户问候"""
        print("\nHello, " + self.first_name + ' ' + self.last_name + ".")
        print("Welcome to this system.")


class Privileges():
    """权限类"""

    def __init__(self):
        self.privileges = ['can add post', 'can delete post', 'can ban user']

    def show_privileges(self):
        print("\nAdmin have the following privileges:")
        for privilege in self.privileges:
            print("- " + privilege)


class Admin(User):
    """模拟管理员"""

    def __init__(self, first_name, last_name, age):
        super().__init__(first_name, last_name, age)
        self.privileges = Privileges()

# admin = Admin('blue', 'dog', 20)
# admin.greet_user()
# admin.privileges.show_privileges()
