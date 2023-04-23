import json

with open('data.json', encoding='utf-8') as file:
    file_content = json.load(file)

for key, value in file_content.items():
    print(
        f"{key}\t\t{value['Цена(BYN)']} BYN\t{value['Цена(USD)']} USD\tТип двигателя: {value['Тип двигателя']}"
        f"\t\tОбъем: {value['Объем']}л.\t\tПробег: {value['Пробег']} км.\t\tГод выпуска: {value['Год выпуска']}г.")
