class Employee():
    def __init__(self, first_name, last_name, salary):
        self.first_nmae = first_name
        self.last_name = last_name
        self.salary = salary

    def give_raise(self, add=None):
        if add:
            self.salary += add
            return self.salary
        else:
            self.salary += 5000
            return self.salary


chel = Employee('Sasha', 'Petrov', 3000)

print(chel)
masha = Employee("masha", 'Petrova', 20000)
print(masha)
