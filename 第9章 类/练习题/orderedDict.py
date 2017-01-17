from collections import OrderedDict

persons = OrderedDict()
persons['李懿哲'] = '26岁'
persons['张三丰'] = '100岁'

for name, age in persons.items():
    print(name + ' ' + age)
