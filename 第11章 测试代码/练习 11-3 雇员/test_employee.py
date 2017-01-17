import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    """定义测试employee.py的类"""

    def setUp(self):
        """在setUp中，定义一个雇员，以便测试方法直接使用"""
        self.employee_a = Employee('懿哲', '李', 9000)

    def test_give_default_raise(self):
        """测试默认的加薪方法"""
        self.employee_a.give_raise()
        self.assertEqual(14000, self.employee_a.salary)

    def test_give_custom_raise(self):
        """测试自定义加薪方法"""
        self.employee_a.give_raise(6000)
        self.assertEqual(15000, self.employee_a.salary)