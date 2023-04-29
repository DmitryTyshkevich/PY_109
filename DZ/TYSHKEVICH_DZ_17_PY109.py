'''Homework: iterators and generators'''

from random import randint, shuffle

'''1. Напишите генератор, который на вход получает список чисел и возвращает только те числа, 
которые делятся на 3 без остатка.'''

'''Вариант 1:'''

for i in (elem for elem in list(range(1, 100)) if elem % 3 == 0):
    print(i)

'''Вариант 2:'''


def generator(lst):
    '''Функция-генератор, которая принимает список целых чисел и возвращает числа,
    которые делятся на 3 без остатка'''
    for elem in lst:
        if elem % 3 == 0:
            yield elem


# =======================================================================================================================
'''2. Напишите итератор, который на вход получает строку и возвращает каждый второй символ этой строки.'''


class StringIterator:
    '''Класс - итератор, возвращающий каждый n-ый символ строки'''

    def __init__(self, str_, n=1):
        self.str_ = str_
        self.n = n

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index < len(self.str_):
            symbol = self.str_[self.index]
            self.index += self.n
            return symbol
        else:
            raise StopIteration


s = 'Сейчас лучше, чем никогда.'
example = StringIterator(s, 2)
for c in example:
    print(c)

# ======================================================================================================================
'''3. Напишите генератор, который на вход получает два списка чисел и возвращает только те числа, 
которые есть в обоих списках.'''


def return_common_numbers(array1, array2):
    '''Функция-генератор получает два списка чисел и возвращает только те числа,
    которые есть в обоих спискаx'''
    set_ = set(array1)
    for elem in set_.intersection(array2):
        yield elem


my_list_1 = [randint(1, 10) for _ in range(20)]
my_list_2 = [randint(1, 10) for _ in range(20)]

example2 = return_common_numbers(my_list_1, my_list_2)
for elem in example2:
    print(elem)

# =======================================================================================================================
'''4. Напишите генератор, который на вход получает список строк и возвращает только те строки, 
которые содержат букву "a".'''


def lines_with_a(array):
    '''Функция-генератор получает список строк и возвращает только те строки,
    которые содержат букву "a"'''
    return (
        line
        for line in array
        if 'а' in line
    )


list_str = ["медведь", "список", "словарь", "часы", "лампочка"]
for line in lines_with_a(list_str):
    print(line)

# =======================================================================================================================
'''5. Напишите итератор, который на вход получает список чисел и возвращает каждый третий элемент этого списка.'''


class ListIterator:
    def __init__(self, array):
        self.array = array

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n < len(self.array):
            elem = self.array[self.n]
            self.n += 3
            return elem
        else:
            raise StopIteration


rand_num_list = [randint(1, 100) for _ in range(20)]
print(*rand_num_list)
for elem in ListIterator(rand_num_list):
    print(elem)

#=======================================================================================================================
'''Реализуйте итератор колоды карт (52 штуки) CardDec. Каждая карта представлена в виде строки типа "2 Пик".
При вызове функции next() будет представлена следующая карта. По окончании перебора всех элементов возникнет 
ошибка StopIteration'''


class CardDec:
    pack_cards = [
        "2 Треф", "2 Бубен", "2 Черви", "2 Пик",
        "3 Треф", "3 Бубен", "3 Черви", "3 Пик",
        "4 Треф", "4 Бубен", "4 Черви", "4 Пик",
        "5 Треф", "5 Бубен", "5 Черви", "5 Пик",
        "6 Треф", "6 Бубен", "6 Черви", "6 Пик",
        "7 Треф", "7 Бубен", "7 Черви", "7 Пик",
        "8 Треф", "8 Бубен", "8 Черви", "8 Пик",
        "9 Треф", "9 Бубен", "9 Черви", "9 Пик",
        "10 Треф", "10 Бубен", "10 Черви", "10 Пик",
        "Валет Треф", "Валет Бубен", "Валет Черви", "Валет Пик",
        "Дама Треф", "Дама Бубен", "Дама Черви", "Дама Пик",
        "Король Треф", "Король Бубен", "Король Черви", "Король Пик",
        "Туз Треф", "Туз Бубен", "Туз Черви", "Туз Пик"
    ]

    def __init__(self):
        shuffle(self.pack_cards)
        self.cards = self.pack_cards

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index < len(self.cards):
            card = self.cards[self.index]
            self.index += 1
            return card
        else:
            raise StopIteration


s = iter(CardDec())
print(next(s))
