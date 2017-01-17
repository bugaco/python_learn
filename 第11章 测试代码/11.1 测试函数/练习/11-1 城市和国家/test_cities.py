import unittest
from city_functions import get_formatted_city

class CityTestCase(unittest.TestCase):
    """测试city_functions.py"""

    def test_city_func(self):
        city_country = get_formatted_city('beijing', 'china')
        self.assertEqual(city_country, 'Beijing,China')