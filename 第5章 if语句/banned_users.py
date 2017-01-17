banned_users = ['andrew', 'carolina', 'david']
print(banned_users)

user = 'marie'
if user not in banned_users:
	print(user.title() + ", you can post a response if you wish.")