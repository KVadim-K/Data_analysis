# 2. Построй диаграмму рассеяния для двух наборов случайных данных,
#    сгенерированных с помощью функции `numpy.random.rand`.

import numpy as np
import matplotlib.pyplot as plt

# Сгенерируем случайные числа
random_array = np.random.rand(5)  # массив из 5 случайных чисел
print(random_array)

# Генерируем случайные цвета
colors = np.random.rand(5)

# Построим диаграмму рассеяния
plt.scatter(random_array, random_array, c=colors, alpha=0.6, edgecolors='w', s=100, cmap='viridis')  # Диаграмма
# рассеяния (прозрачность точек alpha, белые края точек edgecolors, размер точек s). Цветовая карта `viridis`
plt.colorbar(label='Цветовая шкала')  # Добавить цветовую шкалу
plt.title('Диаграмма рассеяния случайных данных')  # Заголовок диаграммы
plt.xlabel('Данные X')  # Подпись оси X
plt.ylabel('Данные Y')  # Подпись оси Y
plt.grid(True)  # Включение сетки
plt.show()  # Отображение диаграммы
