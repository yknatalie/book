import user


class Privileges():
    def __init__(self, privileges=[]):
        self.privileges = privileges

    def show_privileges(self):
        return self.privileges


class Admin(user.User):
    def __init__(self, first_name, last_name, age, country, marital_status, privileges):
        super().__init__(first_name, last_name, age, country, marital_status)
        self.privileges = Privileges(privileges)
