import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    """针对AnonymousSurvey类的测试"""

    def setUp(self):
        """
        创建一个调查对象，供测试方法使用
        """

        question = '你学会的第一门语言是什么？'
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['汉语', '文言文', '英语']

    def test_store_single_response(self):
        """测试单个答案会被妥善存储"""


        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.responses)

    def test_store_three_response(self):
        """测试三个答案会被妥善存储"""

        for response in self.responses:
            self.my_survey.store_response(response)

        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)