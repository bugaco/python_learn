import json

filename= 'username.json1'

try:
    with open(filename) as f_obj:
        username = json.load(f_obj)
except FileNotFoundError:
        print('这是你第一次登录')
else:
        print('欢迎回来，' + username)