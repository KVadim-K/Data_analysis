# Определите среднюю зарплату (Salary) по городу (City) - используйте файл приложенный к дз - dz.csv
# В поле сдачи домашнего задания приложите ссылку на репозиторий с кодом.


import pandas as pd  # Импорт библиотеки pandas

df = pd.read_csv('dz.csv')  # Загрузка датафрейма

print(df)

group = df.groupby('City')['Salary'].mean()  # Группировка по столбцу City с расчетом средней зарплаты

print(group)
