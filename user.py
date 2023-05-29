class User():
    """ User description"""

    def __init__(self, first_name, last_name, age, country, marital_status):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.country = country
        self.marital_status = marital_status
        self.login_attempts = 0

    def describe_user(self):
        print(
            f'Name is {self.first_name} {self.last_name}\nAge is {self.age} \nCountry is {self.country}\n' +
            f'Marital status is {self.marital_status}'
        )

    def greet_user(self):
        print(f'Hello, {self.first_name} {self.last_name}!')

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0
