import matplotlib.pyplot as plt

from random_walk import RandomWalk


rw = RandomWalk(num_points=500)
rw.fill_walk()

#设置绘图窗口的分辨率
plt.figure(figsize=(10, 6))

point_numbers = list(range(rw.num_points))
plt.scatter(rw.x_values,rw.y_values, c=point_numbers,cmap=plt.cm.Blues,edgecolors='none',  s=10)

#突出起点和终点
plt.scatter(0, 0, c='green', edgecolors='none', s=100)
plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)

#隐藏坐标轴
plt.axes().get_xaxis().set_visible(False)
plt.axes().get_yaxis().set_visible(False)

#设置绘图窗口的尺寸
plt.show()

