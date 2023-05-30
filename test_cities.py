import unittest
from city_functions import city_function


class CityTest(unittest.TestCase):

    def test_city_country(self):
        formatted_city = city_function('britain', 'london')
        self.assertEqual(formatted_city, 'Britain, London')

    def test_city_country_population(self):
        formatted_city = city_function('santiago', 'chile', population=300000)
        self.assertEqual(formatted_city, 'Santiago, Chile - population 300000')


if __name__ == '__main__':
    unittest.main()
