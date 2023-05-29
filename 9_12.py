import restaurant
import user
import admin
my_resto = restaurant.Restaurant('Alica', 'russian')
print(my_resto.describe_restaurant())

# der_user = user.Admin("Sasha", "Ivanova", 30, "Russia", "single", [
#     'Can delete users', 'Can ban users'])
# print(der_user.privileges.show_privileges())
adminchek = admin.Admin("Sasha", "Ivanova", 30, "Russia", "single", [
    'Can delete users', 'Can ban users'])
print(adminchek.privileges.show_privileges())
