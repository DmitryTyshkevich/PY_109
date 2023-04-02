def product_basket(key, value, dict_):
    '''Функция добавляет товар в корзину'''
    if key not in dict_:
        dict_[key] = [round(dict_products[key][0] * value, 2), value]
    else:
        dict_[key] = [round(dict_[key][0] + (dict_products[key][0] * value), 2), dict_[key][1] + value]
    return dict_


def price_list(products):
    '''Функция выводит прайс товара'''
    for key, value in products.items():
        print(f'{key} - {value[0]} р. - {value[1]} шт.')


def basket_output(products):
    '''Функция выводит корзину с товаром'''
    print('\nВаш заказ:')
    for key, value in products.items():
        print(f'{key} - {value[0]} р. - {value[1]} шт.')


def calculating_cost(products):
    '''Функция подсчитывает итоговую сумму '''
    sum_ = 0
    for i in products.values():
        sum_ += i[0]
    return sum_


dict_products = {'Ручка': [3.45, 123], 'Карандаш': [1.5, 342],
                 'Ластик': [2.1, 200], 'Линейка': [5.3, 87],
                 'Циркуль': [15, 45], 'Транспортир': [10, 95],
                 'Стержень': [1.2, 322], 'Корректор': [7.3, 76]}
purchases = {}  # словарь для покупок
balance = 500

while True:
    print(f'\nБаланс: {round(balance, 2)}р.')
    print('\nПрайс-лист магазина канцтоваров:')
    price_list(dict_products)
    print('\nДля выхода введите "n"')
    product = input('Для покупки товара введите его название:\n>>>').title()
    if product == 'N' or product == 'Т':  # условие для выхода
        print('Вы вышли из магазина')
        break
    elif product not in dict_products:  # проверка наличия товара
        print('Такого товара нет либо ввод некорректен!')
    else:
        quantity = int(input('Количество: '))
        if quantity <= dict_products[product][1]:  # проверка необходимого кол-ва товара
            if balance < dict_products[product][0] * quantity:  # проверка баланса
                print('У вас недостаточно средств')
            else:
                product_basket(product, quantity, purchases)  # добавляем товар в карзину
                dict_products[product][1] -= quantity  # отнимаем из прайса выбранное кол-во товара
                balance -= dict_products[product][0] * quantity  # минусуем баланс
                print('Товар добавлен в корзину')
        else:
            print('Такого количества нет!')

basket_output(purchases)
print(f'\nК оплате: {calculating_cost(purchases)} р.')
