import pandas as pd

data = {
    'name': ['Alice','Bob', 'Charlie', 'David', 'Eve'],
    'gender': ['female', 'male', 'male', 'male', 'female'],
    'department': ['HR', 'Engineering', 'Marketing', 'Engineering', 'HR']
}
df = pd.DataFrame(data)

# Преобразуем столбцы в категориальные данные. Мы можем сделать категории для столбцов "gender" и "department":
# astype преобразует гендер и департамент в категориальный тип, что позволяет работать с данными как с категориями.
df['gender'] = df['gender'].astype('category')
df['department'] = df['department'].astype('category')
df['department'] = df['department'].cat.add_categories(['Finance'])  # Добавляем категорию "Finance"

# print(df['gender'].cat.categories)
print(df['department'].cat.categories)  # Вывод категорий

df['department'] = df['department'].cat.remove_categories(['HR'])  # Удаляем категорию "HR"
print(df['department'].cat.categories)  # Вывод категорий
print(df)
