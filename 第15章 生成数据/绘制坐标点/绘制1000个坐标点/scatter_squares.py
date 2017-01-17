import matplotlib.pyplot as plt

#传递多组坐标
x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]

#指定三原色
# plt.scatter(x_values, y_values, c=(1, 1, 0.8), edgecolors='none', s=40)

#指定颜色名称
# plt.scatter(x_values, y_values, c='red', edgecolors='none', s=40)

#使用颜色映射
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, edgecolors='none', s=40)

# 设置图标标题，并给坐标轴加上标签
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

#设置每个坐标轴的取值范围
plt.axis([0, 1100, 0, 1100000])

plt.show()

#保存文件
# plt.savefig('/Users/mapbar/Desktop/squares_plot.png')