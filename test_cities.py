import unittest
from city_functions import city_country

class NamesTestCase(unittest.TestCase):

    def test_city_country(self):
        nome_formatado = city_country('santiago', 'chile')
        self.assertEquals(nome_formatado, 'santiago, chile')
    
    
    def test_city_country_population(self):
        nome_formatado = city_country('santiago', 'chile', population=5000)
        self.assertEquals(nome_formatado, 'santiago, chile - população 5000')


if __name__ == '__main__':
    unittest.main()