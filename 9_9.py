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
    def set_number_served(self,number):
            self.number_served = number
    def increment_number_served(self, number):
         self.number_served +=number

class IceCreamStand(Restaurant):
     def __init__(self, restaurant_name, cuisine_type,flavours):
          super().__init__(restaurant_name, cuisine_type)
          self.flavours = flavours
     def show_flavours(self):
          return self.flavours
     
vanillaa = IceCreamStand('Ice','Russian', 'vanilla')
# print(vanillaa.show_flavours())

class User():
    """ User description"""
    def __init__(self,first_name, last_name,age,country,marital_status):
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

class Privileges():
     def __init__(self,privileges = []):
          self.privileges = privileges
     def show_privileges(self):
          return self.privileges

class Admin(User):
     def __init__(self,first_name, last_name,age,country,marital_status, privileges):
        super().__init__(first_name, last_name,age,country,marital_status)
        self.privileges = Privileges(privileges)
    
     
tanya = Admin("Tanya","Ivanova",30, "Russia","single","Can ban users")

sasha = Admin("Sasha","Ivanova",30, "Russia","single", ['Can delete users','Can ban users'])
# print(sasha.privileges.show_privileges())
class Car():
    """Простая модель автомобиля."""
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    def get_descriptive_name(self):
        long_name = f"{self.year} {self.manufacturer} {self.model}"
        return long_name.title()
    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")
    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    def increment_odometer(self, miles):
        self.odometer_reading += miles

class Battery():
    """Простая модель аккумулятора электромобиля."""
    def __init__(self, battery_size=75):
        """Инициализирует атрибуты аккумулятора."""
        self.battery_size = battery_size
    def describe_battery(self):
        """Выводит информацию о мощности аккумулятора."""
        print(f"This car has a {self.battery_size}-kWh battery.")
    def get_range(self):
        """Выводит приблизительный запас хода для аккумулятора."""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
        print(f"This car can go about {range} miles on a full charge.")
    def upgrade_battery(self):
        if self.battery_size < 100:
            self.battery_size = 100



class ElectricCar(Car):
    """Представляет аспекты машины, специфические для электромобилей."""
    def __init__(self, make, model, year):
        """инициализирует атрибуты класса-родителя."""
        super().__init__(make, model, year)
        self.battery = Battery()
    def fill_gas_tank(self):
        """У электромобилей нет бензобака."""
        print("This car doesn't need a gas tank!")

tesla = ElectricCar('tesla','s3','2020')
print(tesla.battery.describe_battery())
tesla.battery.upgrade_battery()
print(tesla.battery.describe_battery())


     

     

     
