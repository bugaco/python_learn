name_message = '请输入您的名号：'
question_message = '您为什么喜欢编程呀？'

file_name = 'name_reason.txt'

while True:
    name = input(name_message)
    if name != 'q':
        reason = input(question_message)
        if reason != 'q':
            with open(file_name, 'a') as file_object:
                file_object.write(name + ':' + reason + '\n')
        else:
            print('您选择了😊退出')
            break
    else:
        print('您选择了退出')
        break