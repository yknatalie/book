def city_function(country, city, population=''):
    if population:
        return f'{country.title()}, {city.title()} - population {population}'
    else:
        return f'{country.title()}, {city.title()}'


a = city_function('britain', 'london', 30000000)
print(a)
