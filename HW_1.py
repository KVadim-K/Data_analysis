import pandas as pd

df = pd.read_csv('Dataset salary 2024.csv')  # Загрузка датафрейма

print(df.head())  # Вывод первых 5 строк

print(df.info())  # Информация о датафрейме

print(df.describe())  # Вывод описательной статистики