lans = {'Jax': 'Yurenyu', 'Yi': "WujiLan", 'Ashe':'BingshuangLan', 'Manwang': "BingshuangLan"}
print(lans)
for lan in lans.values():
	print(lan)

#用set去重
print('\n')
for lan in set(lans.values()):
	print(lan)