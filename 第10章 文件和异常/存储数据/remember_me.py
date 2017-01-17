import json

filename = 'username.json'

username = input('你叫什么名字？')

with open(filename, 'w') as f_obj:
    json.dump(username, f_obj)
    print('你下次登录时，我们将会记住你！' + username)