'''Домашнее задание'''


def sum_even_number(x):
    '''Функция считает сумму четного числа'''
    summ = 0
    n = x  # присваиваем переменной число данного элемента
    while n:  # при помощи цикла находим сумму цифр
        summ += n % 10  # к счетчику прибавляем последнюю цифру числа
        n //= 10  # отсекаем последнюю цифру
    print(f'Элемент {x} является четным числом, его сумма цифр: {summ}')


def counts_vowels_and_consonants(s):
    '''Функция считает кол-во гласных и согласных букв в строке'''
    vowels = 0  # счетчки гласных букв
    consonants = 0  # счетчик согласных букв
    for c in list_[i]:  # проходим циклом по каждому букве строки
        if c in 'aeiou':
            vowels += 1  # если буква гласная, то обновляем счетчик гласных букв
        else:
            consonants += 1  # если согласная, то обновляем счетчик согласных букв
    print(f'Элемент {list_[i]} является строкой, гласных букв: {vowels}, согласных букв: {consonants}')


list_ = [15, 48, 'hello', 6, 19, 'world']

for i in range(len(list_)):  # циклом проходим по каждому элементу списка
    if isinstance(list_[i], int):  # проверка элемента на число
        if list_[i] % 2 == 0:  # если число четное, находим сумму его цифр
            sum_even_number(list_[i])
        else:
            print(f'Элемент {list_[i]} является нечетным числом - меняем его на 1 ')
            list_[i] = 1  # если число нечетное, то меняем его на 1
    elif isinstance(list_[i], str):  # проверка элемента на строку
        counts_vowels_and_consonants(list_[i])

print(f'Итоговый список {list_ = }')  # выводим измененный список
