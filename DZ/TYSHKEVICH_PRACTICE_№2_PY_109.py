'''1'''


def body_mass_index(height, weight):
    return weight / (height / 100) ** 2


height = int(input('Введите рост: '))
weight = int(input('Введите вес: '))

if 25 <= body_mass_index(height, weight) >= 30:
    print('Вы имеете избыточный вес')
else:
    print('Можно кушать спокойно')

'''2'''


def shape_type(arg):
    if arg == 3:
        return 'Треугольник'
    elif arg == 4:
        return 'Квадрат'
    elif arg == 5:
        return 'Пятиугольник'
    elif arg == 6:
        return 'Шестиугольник'
    elif arg == 7:
        return 'Семиугольник'
    elif arg == 8:
        return 'Восьмиугольник'
    elif arg == 9:
        return 'Девятиугольник'
    elif arg == 10:
        return 'Десятиугольник'
    return 'За границей диапазона'


'''4'''


def get_shipping_cost(quantity):
    return 10.95 + 2.95 * (quantity - 1)


n = int(input('Введите кол-во товара: '))
print(get_shipping_cost(n))

'''6'''


def list_output(list_):
    print(list_[::-1])
    print(sorted(list_, reverse=True, key=int))
    print(sorted(list_, key=int))
    print(list_[2:8])
    del list_[4]
    print(list_)
    print(set(list_))


my_list = [1, 1, 5, 6, '34', '56', 34, 6, '8', 36, '21']
list_output(my_list)

'''7'''


def countRange(list_, min_, max_):
    result = [num for num in list_ if min_ <= num < max_]
    return len(result)


print(countRange([1, 3, 4, 6.5, 5, 3], 1, 7))
print(countRange([1, 3.5, 44, 6.5, 5, 3], 1.8, 6))

'''8'''


def number_of_sublists(list_):
    count = 0
    for elem in list_:
        if isinstance(elem, list):
            count += 1 + number_of_sublists(elem)
        else:
            count += 1
    return count


'''9'''


def anagram(s1, s2):
    d1 = {c: s1.count(c) for c in s1}
    d2 = {c: s2.count(c) for c in s2}
    return d1 == d2


word1 = input('Введите первое слово: ')
word2 = input('Введите второе слово: ')

print(anagram(word1, word2))

'''10'''

s = input().upper()
result = ''
keyboard = {
    "1": ".,?!:",
    "2": "ABC",
    "3": "DEF",
    "4": "GHI",
    "5": "JKL",
    "6": "MNO",
    "7": "PQRS",
    "8": "TUV",
    "9": "WXYZ",
    "0": " "
}
for c in s:
    for key, value in keyboard.items():
        if c in value:
            result += key * (value.index(c) + 1)

print(result)

'''11'''


def list_alignment(list_):
    if list_ == []:
        return list_
    if isinstance(list_[0], list):
        return list_alignment(list_[0]) + list_alignment(list_[1:])
    return (list_[:1] + list_alignment(list_[1:]))


my_list = [1, [2, 3], [4, [5, [6, 7]]], [[[8], 9], [10]]]

print(list_alignment(my_list))
