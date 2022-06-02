from user import User


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
