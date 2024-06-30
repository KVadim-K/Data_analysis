import pandas as pd

df = pd.read_csv('animal.csv')
print(df)

# df.fillna(0, inplace=True)  # Заменить пропуски на 0 в датафрейме
# print(df)

# df.dropna(inplace=True)  # Удаление строк с пропусками
# print(df)

group = df.groupby('Пища')['Средняя продолжительность жизни'].mean()  # Группировка по столбцу Пища с расчетом средней продолжительности жизни
print(group)
