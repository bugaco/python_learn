vehicles = ["subway", "bus"]
message = 'I would like to own a '
print(message + vehicles[0] + ".")
print(message + vehicles[-1] + ".")

#改变列表中一个元素的内容
print(vehicles)
vehicles[0] = "bicycle"
print(vehicles)

#往里诶保重追加元素
vehicles.append("moto")
print(vehicles)

#初始化一个摩托车品牌数组
motorcicle = []
motorcicle.append('Dayang')
motorcicle.append('Yamaha')
motorcicle.append('Yadi')
print(motorcicle)

#插入一个元素
motorcicle.insert(1, 'heihei')
print("insert :\n" + str(motorcicle))

#删除一个元素
del motorcicle[1]
print("\nafter delete: " + str(motorcicle))

bike = motorcicle.pop(1)
print(motorcicle)
print(bike)

too_expensive = "Dayang"
motorcicle.remove(too_expensive)
print(motorcicle)

