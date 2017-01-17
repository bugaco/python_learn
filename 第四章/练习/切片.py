cubes = [value for value in range(1, 11)]
print(cubes[-22:])#最后的22
print(cubes[0:3])#前三名队员
print(cubes)

digitals = ['92', '5', '32','7' ]

print(digitals)

# 列表复制
digitals2 = digitals
print(digitals2)

digitals.append(100)
digitals2.append(1000)
print(digitals)
print(digitals2)

for value in digitals:
	print(value)
