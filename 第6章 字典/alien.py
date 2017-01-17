alien_0 = {'color': 'green', 'point': '5'}
print(alien_0['color'])
print(alien_0['point'])

alien_0['x_position'] = 5
alien_0['y_position'] = 25

alien_0['speed'] = 'fast'

speed = alien_0['speed']

if speed == 'slow':
	x_increment = 1
elif speed == 'medium':
	x_increment = 2
else:
	x_increment = 3

alien_0['x_position'] = alien_0['x_position'] + x_increment

#删除
del alien_0['color']

print(alien_0)

#print 分行写法
print("---------")
print("My name is " + 
	"Hanmeme" + 
	"."
	)
#个人信息
print('--------')
Liyizhe = {'name':'Li Yizhe', 'city': 'Beijing'}

for key, value in Liyizhe.items():
	print(key + " " + value)
#返回所有键
for key in Liyizhe.keys():
	print(key )
	#或者
for key in Liyizhe:
	print(key )

#返回所有值
for value in Liyizhe.values():
	print(value )

#.key()可以省略，默认返回keys
print('-----')
for key in Liyizhe:
	print(key)