import unittest
from employee import Employee


class EmployeeTest(unittest.TestCase):

    def setUp(self):
        self.masha = Employee('Masha', 'Petrova', 25000)

    def test_give_default_raise(self):
        a = 30000
        b = self.masha.give_raise()
        self.assertEqual(b, a)

    def test_give_custom_raise(self,):
        c = 28000
        s = self.masha.give_raise(3000)
        self.assertEqual(c, s)


if __name__ == '__main__':
    unittest.main()
