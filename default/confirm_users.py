unconfirmed_users = ['张飞', '刘备', '关羽']
confirmed_users = []
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    confirmed_users.append(current_user)
print(unconfirmed_users)
print(confirmed_users)