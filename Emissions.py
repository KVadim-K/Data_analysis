import pandas as pd
import matplotlib.pyplot as plt


data = {'value':[1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 6, 7, 8, 9, 10, 55]}
df = pd.DataFrame(data)
# print(df.describe())

# # Создадим график, который поможет визуализировать данные из датафрейма.
# # Для этого мы будем использовать библиотеку Matplotlib:
# df['value'].hist()  # используем функцию hist() для построения диаграммы
# plt.show()  # показывает график, который мы создали.

# Для построения гистограммы можно использовать другой вариант визуализации этих данных:
df.boxplot(column='value')
plt.show()

# Oпределим первый(Q1) и третий(Q3) квартили, используя функцию quantile():
Q1 = df['value'].quantile(0.25)
Q3 = df['value'].quantile(0.75)
IQR = Q3 - Q1  # Определим межквартильный размах(IQR):

# Определим  нижнюю и верхнюю границы для определения выбросов. Пропишем переменные для границ
downside = Q1 - 1.5 * IQR
upside = Q3 + 1.5 * IQR

# Теперь удалим все выбросы, которые не входят в очерченный диапазон
df = df[(df['value'] >= downside) & (df['value'] <= upside)]

df_new = df.boxplot(column='value')  # Построим гистограмму с удаленными выбросами
plt.show()

