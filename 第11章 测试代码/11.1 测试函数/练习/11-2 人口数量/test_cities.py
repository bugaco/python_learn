import unittest
from city_functions import get_formatted_city

class CityTestCase(unittest.TestCase):
    """测试city_functions.py"""

    def test_city_country_populationfunc(self):
        """测试三个参数"""
        city_country_populationfunc = get_formatted_city('beijing', 'china', 20000000)
        self.assertEqual(city_country_populationfunc, 'Beijing,China - population 20000000')

    def test_city_country(self):
        city_country = get_formatted_city('beijing', 'china')
        self.assertEqual(city_country, 'Beijing,China')

if __name__ == '__main__':
    unittest.main()