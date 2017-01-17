#打印1~一百万
digitals = list(range(1, 1000001))
print(max(digitals))
print(min(digitals))

#1~一百万相加
sum = 0
for digital in digitals:
	sum += digital
print("sum : + ", sum)

#1～20的奇数
uneven_numbers = list(range(1, 21, 2))
print(uneven_numbers)

# 3～30之间 3的倍数
mutipule_3_numbers = list(range(3, 31, 3))
print(mutipule_3_numbers)

# 1~10的立方
cubes  = []
for value in range(1, 11):
	cubes.append(value ** 3)
print(cubes)

# 立方解析
cubes = [value ** 3 for value in range(1, 11)]
print(cubes)

