import pandas as pd
import numpy as np

data = {
    'Name': ['Alice', 'Bob', 'Roma', 'Anna'],
    'Age': [23, 45, 17, 24],
    'City': ['New York', 'LA', 'Chicago', 'Moscow']
}
df = pd.DataFrame(data)  # Функция DataFrame преобразует созданный словарь в датафрейм
print(df)

# data = [1, 2, 3, 4, 5]
# series = pd.Series(data) # Функция Series преобразует созданный числовой список в массив с индексом
# print(series)

df.to_csv('data.csv', index=False)  # index=False`, pandas запишет индексы строк в первой колонке CSV файла.
# Это может быть полезно в некоторых случаях, но если вам не нужны индексы строк в CSV файле
# или вы хотите сохранить только данные, вы можете указать `index=False`.

