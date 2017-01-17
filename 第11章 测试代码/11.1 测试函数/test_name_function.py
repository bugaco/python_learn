import unittest
from name_function import get_formatted_name

class NameTestCase(unittest.TestCase):
    """测试name_function.py"""

    def test_first_last_name(self):
        """能够正确处理像Li Yizhe这样的姓名吗？"""
        formatted_name = get_formatted_name('li', 'yizhe')
        self.assertEqual(formatted_name, 'Li Yizhe')

    def test_first_last_middle_name(self):
        """能够正确处理像 Li Yi Zhe这样的姓名吗？"""
        formatted_name = get_formatted_name('li', 'zhe', 'yi')
        self.assertEqual(formatted_name, 'Li Yi Zhe')

if __name__ == '__main__':
    unittest.main(verbosity=0)