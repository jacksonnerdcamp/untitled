from matplotlib import pyplot as plt

dev_x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
dev_y = [2, 4, 6, 8, 10, 12, 14, 16, 18]
plt.plot(dev_x,dev_y)
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.title('title')
plt.legend()
plt.xlim(0, 10)
plt.ylim(0, 20)
plt.tight_layout()


plt.show()
