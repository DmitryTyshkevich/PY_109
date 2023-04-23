from bs4 import BeautifulSoup
import requests
import lxml
import json
import csv

'''Напишите парсер, который делает выборку по всем страницам с моделями BMW E60. (или любой модели на Ваш выбор).
1. Необходимо спарсить:
    1). Ссылку на объявление
    2). Цену в BYN / USD
    3). Тип двигателя / объем / пробег / год выпуска
2. Полученную информацию отсортируйте по цене в USD
3. Запишите полученную информацию в форматах JSON и CSV
4. В отдельном Python-файле пропишите код, который будет
считывать спаршеную информацию из CSV/JSON'''


def get_html(url):
    # передаваемые заголовки
    headers = {
        'Accept': 'text/html, application/xhtml+xml, application/xml;q=0.9,image/webp, */*;q=0.8',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko)'
                      ' Chrome/112.0.0.0 Safari/537.36'
    }
    # в переменную req получим результат вызова requests.get с параметрами url, а ткаже headers
    req = requests.get(url, headers=headers)

    return req


links_list = []
list_price_by = []
list_price_usd = []
list_params = []

for count in range(1, 9):
    url = f'https://cars.av.by/filter?brands[0][brand]=6&brands[0][model]=5812&page={count}'
    soup = BeautifulSoup(get_html(url).text, 'html.parser')

    # Формирование списка ссылок
    list_model_a8 = soup.find_all('h3', 'listing-item__title')
    for item in list_model_a8:
        links_list.append('https://cars.av.by' + item.a.attrs.get('href'))

    # Формирование списка цен в byn
    price_by = soup.find_all('div', 'listing-item__price')
    for price in price_by:
        # Кодируем в ASCII
        price_encode = price.text.encode('ascii', errors='ignore')
        # Декодируем  в utf-8
        price_decode = price_encode.decode('utf-8').strip('.')
        list_price_by.append(int(price_decode))

    # Формирование списка цен в USD
    price_usd = soup.find_all('div', 'listing-item__priceusd')
    for price in price_usd:
        # Кодируем в ASCII
        price_encode = price.text.encode('ascii', errors='ignore')
        # Декодируем  в utf-8
        price_decode = price_encode.decode('utf-8').strip('$')
        list_price_usd.append(int(price_decode))

    # Формирование списка характеристик
    params = soup.find_all('div', 'listing-item__params')
    for item in params:
        years_encode = item.find('div').text.encode('ascii', errors='ignore')
        years_decode = int(years_encode.decode('utf-8').strip('.'))

        mileage_encode = item.find('span').text.encode('ascii', errors='ignore')
        mileage_decode = int(mileage_encode.decode('utf-8'))

        par = item.get_text().split(',')
        engine_type = par[2].strip(' ')

        volume_encode = par[1].encode('ascii', errors='ignore')
        volume_decode = float(volume_encode.decode('utf-8'))
        list_params.append([engine_type, volume_decode, mileage_decode, years_decode])

collected_data = {}  # Формирование данных в словарь
for a, i, j, k in zip(links_list, list_price_by, list_price_usd, list_params):
    collected_data[a] = {'Цена(BYN)': i, 'Цена(USD)': j, 'Тип двигателя': k[0],
                         'Объем': k[1], 'Пробег': k[2], 'Год выпуска': k[3]}

list_tuples = list(collected_data.items())
result_sort = dict(sorted(list_tuples, key=lambda x: x[1]['Цена(USD)']))  # Сортировка по цене в USD

# Запись данных в json-файл
with open('data.json', 'w', encoding='utf-8') as file:
    json.dump(result_sort, file, indent=4, ensure_ascii=False)

# Запись данных в csv-файл
with open('file.csv', 'w', encoding='utf-8') as file:
    file_writer = csv.writer(file, delimiter=',', lineterminator='\r')
    file_writer.writerow(['Ссылка', 'Цена(BYN)', 'Цена(USD)', 'Тип двигателя', 'Объем', 'Пробег', 'Год выпуска'])
    for key, value in result_sort.items():
        file_writer.writerow([key, value['Цена(BYN)'], value['Цена(USD)'], value['Тип двигателя'], value['Объем'],
                              value['Пробег'], value['Год выпуска']])
