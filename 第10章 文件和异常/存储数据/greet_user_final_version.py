import json

def get_old_user():
    filename = 'username.json2'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_user():
    filename = 'username.json2'
    username = input('请输入你的名字：')
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
        return username

def greet_user():
    username = get_old_user()
    if username:
        message = input(username + '是你吗？如果不是，请输入n重新登记')
        if message.lower() == 'n':
            print('感谢您的登记，' + get_new_user())
        else:
            print("欢迎回来，冒险进行的如何？" + username + ".")


    else:
        print('感谢您的登记，' + get_new_user())

"""调用问候用户的方法"""
greet_user()
