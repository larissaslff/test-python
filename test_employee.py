import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    def setUp(self):
        """
        Inicia um Employee
        """
        self.employee = Employee('Ana', 'Moura', 5000)
        
    def test_give_default_raise(self):
        self.employee.give_raise()
        self.assertEqual(self.employee.salario_anual, 10000)


    def test_give_custom_raise(self):
        self.employee.give_raise(10000)
        self.assertEqual(self.employee.salario_anual, 15000)


unittest.main()