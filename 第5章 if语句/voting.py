age = 19
if age >= 18:
	print("You are old enough to vote!")
else:
	print("You are too young")

# elif
age = 28
if age <= 10:
	print('<= 10')
elif age <= 20:
	print('11~20')
elif age <= 50:
	if age == 25:
		print(age)
	else:
		print('21~50,but not 25')
else:
	print('50+')