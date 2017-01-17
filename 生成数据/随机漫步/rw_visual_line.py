import matplotlib.pyplot as plt

from random_walk import RandomWalk

# 绘制线

rw = RandomWalk(num_points=500)
rw.fill_walk()

plt.plot(rw.x_values, rw.y_values,  linewidth=1)
plt.scatter(0, 0, c='green', s=100)
plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', s=100)
plt.show()