# 3. Необходимо спарсить цены на диваны с сайта divan.ru в csv файл, обработать данные, найти среднюю цену и вывести ее,
# а также сделать гистограмму цен на диваны.

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import csv
import matplotlib.pyplot as plt

driver = webdriver.Chrome()  # Используем Google Chrome

url = 'https://www.divan.ru/rostov-na-donu/category/rasprodazha-divanov'  # URL страницы

driver.get(url)  # Открытие страницы

time.sleep(5)  # Ждем некоторое время, чтобы страница полностью загрузилась

# Парсинг цен
# prices = driver.find_elements(By.XPATH, "//span[@data-mark='MainPrice']/span")
prices = driver.find_elements(By.XPATH, "//span[@data-testid='price']")


# Открытие CSV файла для записи
with open('pricesDivan.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Price'])  # Записываем заголовок столбца

    # Записываем цены в CSV файл
    for price in prices:
        price_text = price.text.replace('руб.', '').replace(' ', '')  # Убираем "руб." и пробелы
        try:
            price_value = int(price_text)  # Преобразуем в число
            writer.writerow([price_value])
        except ValueError:
            print(f"Ошибка преобразования значения: {price_text}")

# Закрытие драйвера
driver.quit()
# Чтение данных из CSV файла
prices_list = []
with open('pricesDivan.csv', mode='r', newline='', encoding='utf-8') as file:
    reader = csv.reader(file)
    next(reader)  # Пропускаем заголовок
    for row in reader:
        prices_list.append(int(row[0]))

# Построение гистограммы
plt.figure(figsize=(10, 6))
plt.hist(prices_list, bins=20, edgecolor='black')
plt.title('Гистограмма цен на диваны')
plt.xlabel('Цена')
plt.ylabel('Количество')
plt.grid(True)
plt.show()
