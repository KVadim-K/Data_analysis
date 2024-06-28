import pandas as pd
import numpy as np

df = pd.read_csv('World-happiness-report-2024.csv')
# print(df.head())  # Вывод первых 5 строк
# print(df.tail())  # Вывод последних 5 строк
# print(df.info())  # Информация о датафрейме
# Здесь выводится информация о том, сколько всего данных содержится в датасете, названия всех столбцов
# и какое количество столбцов содержит в себе информ
# print(df.describe())  # Вывод описательной статистики
# функция позволяет получить статистические данные:найти минимальные, максимальные и средние значения, количество и т.д.
# print(df['Country name']) # выводить конкретную информацию, например, сведения из определённого столбца
# print(df[['Country name', 'Regional indicator']])# выводить конкретную информацию, например, сведения из опр. столбцов
# print(df.loc[56])  # всю информацию, которая есть в строке 56 по всем колонкам.
# print(df.loc[56, 'Healthy life expectancy'])  # В результате мы получаем только один показатель по конкретной строке
print(df[df['Healthy life expectancy'] > 0.7])
