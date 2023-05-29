class Restaurant():
    """ Restaurant description."""

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(self.restaurant_name)
        print(self.cuisine_type)

    def open_restaurant(self):
        print('The restaurant is open')

    def set_number_served(self, number):
        self.number_served = number

    def increment_number_served(self, number):
        self.number_served += number


restaurant = Restaurant('Cloud', 'Russain')
restaurant.number_served = 23
restaurant.set_number_served(483)
restaurant.increment_number_served(2000)
# print(restaurant.number_served)


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


anatoly = User("Anatoly", "Ivanov", "23",
               country="Russia", marital_status="married")
anatoly.increment_login_attempts()
anatoly.increment_login_attempts()
anatoly.increment_login_attempts()
print(anatoly.login_attempts)
anatoly.reset_login_attempts()
print(anatoly.login_attempts)
