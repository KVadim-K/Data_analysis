import pandas as pd
import matplotlib.pyplot as plt


# # Линейный график
# x = [2, 6, 8, 14, 20]
# y = [6, 4, 10, 12, 16]
#
# plt.title('График')
# plt.xlabel('X ось')
# plt.ylabel('Y ось')
# plt.plot(x, y)
# plt.show()


# # Гистограмма
# data = [1, 2, 2, 3, 4, 4, 4, 5, 6, 6, 6, 6, 6]
#
# plt.hist(data, bins=6)
# plt.xlabel("x ось")
# plt.ylabel("y ось")
# plt.title("Тестовая гистограма")
# plt.show()


# # Диаграмма рассеяния точечная
x = [1, 4, 6, 7, 8, 9]
y = [3, 5, 8, 10, 11, 13]

plt.scatter(x, y)  # Создаём диаграмму
plt.xlabel("ось Х")
plt.ylabel("ось Y")
plt.title("Тестовая диаграмма рассеяния")
plt.show()
