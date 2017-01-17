from survey import AnonymousSurvey

# 定义一个问题，并创建一个表示调查的AnonymousSurvey对象
question = 'What is the language did you first learn to spean?'
my_survey = AnonymousSurvey(question)

# 显示问题
my_survey.show_questions()

# 存储答案
print('Enter "q" at any time to quit.\n')
while True:
    response = input("Language: ")
    if response == 'q':
        break
    my_survey.store_response(response)

my_survey.show_results()