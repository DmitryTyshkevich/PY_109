'''Homework'''
import json

''' Задача №1
Пользователь будет вводить название и стоимость каждой своей покупки за день, до тех пор пока он не напишет
“стоп”. Задача записать это в json файл в формате:{"название" : "яблоко", "стоимость": "200"}
'''

purchase_data = []
while True:
    purchase_name = input('Введите название покупки (для завершения введите "стоп"):\n>>> ').lower()
    if purchase_name == 'стоп' or purchase_name == 'cnjg':
        break
    purchase_price = input('Введите стоимость пукупки:\n>>> ')
    if not purchase_price.isdigit():
        print('Цена введена некорректно!')
    else:
        purchase_data.append({'название': purchase_name, 'стоимость': purchase_price})

with open('../file/price.json', 'w', encoding='utf-8') as recordable_file:
    json.dump(purchase_data, recordable_file, ensure_ascii=False)

'''Задача №2
Прочитать файл из предыдущего задания и вывести стоимость всех покупок за день'''

with open('../file/price.json', encoding='utf-8') as output_file:
    data = json.load(output_file)

result = 0
for cost in data:
    result += int(cost['стоимость'])
print(f'Стоимсоть всех покупок: {result} денежных единиц')
