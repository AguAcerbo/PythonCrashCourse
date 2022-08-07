import unittest
from city_functions import get_city_country

class CityCountryTestCase(unittest.TestCase):
    """Test for city_functions.py"""
    
    def test_city_country(self):
        """Do cities like Rosario, Argentina works?"""
        city_country = get_city_country('Rosario', 'Argentina')
        self.assertEqual(city_country, 'Rosario, Argentina')
        
    def test_city_country_pop(self):
        """Do cities like Rosario, Argentina - pop works?"""
        city_country = get_city_country('Rosario', 'Argentina', 1500000)
        self.assertEqual(city_country, 'Rosario, Argentina - Population 1500000')        
        

if __name__=='__main__':
    unittest.main()