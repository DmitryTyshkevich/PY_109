from random import randrange, randint

'''Задание №1'''


def hypotenuse(a, b):
    '''Функция вычисляет гипотенузу треугольника'''
    return (a ** 2 + b ** 2) ** 0.5


print('По двум введенным катетам вычислить длину гипотенузы')
cathet_1 = int(input('Введите значение первого катета: '))
cathet_2 = int(input('Введите значение второго катета: '))
print(hypotenuse(cathet_1, cathet_2))

# **********************************************************************************************************************


'''Задание №2'''


def average_num(a, b, c):
    '''Функция находит среднее из трех чисел'''
    if b <= a <= c or c <= a <= b:
        return f'Средним является число {a}'
    elif a <= b <= c or c <= b <= a:
        return f'Средним является число {b}'

    return f'Средним является число {c}'


print('\nВводятся три разных числа. Найти, какое из них является средним')
num_1 = int(input('Введите первое число: '))
num_2 = int(input('Введите второе число: '))
num_3 = int(input('Введите третье число: '))
print(average_num(num_1, num_2, num_3))

# **********************************************************************************************************************


'''Задание №3'''


def odd_num(a, b):
    '''Функция определяет нечетное число'''
    if a % 2 != 0:
        return f'Нечетное - {a}'
    elif b % 2 != 0:
        return f'Нечетное - {b}'
    else:
        return f'Введены четные числа'


print('\nИз двух случайных чисел, одно из которых четное, а другое нечетное, \
определить и вывести на экран нечетное число.')
num_1 = randrange(0, 100, 2)
num_2 = randrange(1, 100, 2)
print(f'Первое число: {num_1}\nВторое число: {num_2}')
print(odd_num(num_1, num_2))

# **********************************************************************************************************************


'''Задание №4'''


def inverse_num(n):
    '''Функция выводит число в обратном порядке'''
    if n.isdigit():
        return n[::-1]
    return f'Введено не число'


print('\nСформировать из введенного числа обратное по порядку \
\nвходящих в него цифр и вывести на экран.')
num = input('Введите число: ')
print(inverse_num(num))

# **********************************************************************************************************************


'''Задание №5'''


def rectangle(a, b):
    '''Функция считает площадь прямоугольника'''
    return f'Площадь прямоугольника = {a * b}'


def area_triangle(d, h):
    '''Функция считает площадь треугольника'''
    return f'Площадь треугольника = {1 / 2 * d * h}'


def area_circle(r):
    '''Функция считает площадь круга'''
    return f'Площадь круга = {3.14 * r ** 2}'


print('\nНайти площади прямоугольника, треугольника или круга.\
Введите соответствующий номер:')
geom_sh = input('1 - Прямоугольник\n2 - Треугольник\n3 - Круг\n>>> ')

if geom_sh == '1':
    side1 = int(input('Введите значение стороны а: '))
    side2 = int(input('Введите значение стороны b: '))
    print(rectangle(side1, side2))
elif geom_sh == '2':
    cathet = int(input('Введите значение катета: '))
    height = int(input('Введите значение высоты: '))
    print(area_triangle(cathet, height))
elif geom_sh == '3':
    radius = int(input('Введите значение радиуса: '))
    print(area_circle(radius))
else:
    print('Некорректный ввод')

# **********************************************************************************************************************


'''Задание №6'''


def existence_triangle(a, b, c):
    '''Функция определяет существование треугольника'''
    if a < b + c and b < a + c and c < b + a:
        return 'Треугольник существует'
    return 'Треугольник не существует'


print('\nОпределить существование треугольнка по трем сторонам')
side1 = int(input('Введите значение первой стороны треугольника: '))
side2 = int(input('Введите значение второй стороны треугольника: '))
side3 = int(input('Введите значение третьей стороны треугольника: '))
print(existence_triangle(side1, side2, side3))

# **********************************************************************************************************************


'''Задание №7'''


def existence_circle(x, y, r):
    '''Функция определяет принадлежность точки окружности'''
    if ((x ** 2 + y ** 2) ** 0.5) <= r:
        return 'Точка принадлежит окружности'
    return 'Точка не принадлежит окружности'


print('\nОпределить принадлежность точки кругу')
coordinate_x = int(input('Введите координату х: '))
coordinate_y = int(input('Введите координату у: '))
radius = int(input('Введите радиус окружности: '))
print(existence_circle(coordinate_x, coordinate_y, radius))

# **********************************************************************************************************************


'''Задание №8'''


def counting_words(str_):
    '''Функция определяет количество слов в строке'''
    # Создаем список из строки и возвращаем его длину
    return f'Слов в строке - {len(str_.split())}'


print('\nВводится строка, состоящая из слов, разделенных пробелами \
\nтребуется посчитать количество слов в ней')
string = input('Введите строку, состоящую из слов: ')
print(counting_words(string))

# **********************************************************************************************************************


'''Задание №9'''


def removes_capital_letters(str_):
    '''Функция удаляет заглавные буквы из строки'''
    result = ''
    for c in str_:  # Перебираем строку посимвольно
        if not c.isupper():
            result += c
    return result


string = input('\nВведите строку, состоящую из букв разного регистра:\n>>> ')
print(removes_capital_letters(string))

# **********************************************************************************************************************


'''Задание №10'''

print('\nПрограмма выводит числа от 0 до 100, пропуская числа кратные 7')

for i in range(0, 101):
    if i % 7 != 0:
        print(i)

# **********************************************************************************************************************


'''Задание №11'''

print('\nНайти сумму ряда чисел от 1 до 100')
numbers = [i for i in range(1, 101)]  # Создаем список числами от 1 до 100
print(f'Сумма = {sum(numbers)}')

# **********************************************************************************************************************


'''Задание №12'''


def factorial(n):
    '''Функция вычисляет факториал натурального числа'''
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


print('По данному натуральному числу вычислите значение n!')
num = int(input('Введите натуральное число:\n>>> '))
print(f'{num}! = {factorial(num)}')

# **********************************************************************************************************************


'''Задание №13'''


def tree(n):
    '''Функция выводит последовательность чисел
    от 1 до n елочкой'''
    total = 0  # Счетчик для вывода последовательности
    for i in range(1, n + 1):  # Внешний цикл для построчного вывода последовательности
        if total < n:  # Условие для остановки вывода последовательности
            for j in range(i):  # Внутренний цикл для вывода чисел в одной строке i-раз
                total += 1  # Обновляем счетчик вывода после каждой итерации
                print(total, end=' ')
                if total == n:
                    break
        else:
            break
        print()


print('Пользователь передает целое положительное число N,\
вывести на экран последовательность от 1 до N "елочкой"')

num = int(input('Введите положительное натуральное число:\n>>> '))
tree(num)

# **********************************************************************************************************************


'''Задание №14'''


def intersection_list(list1, list2):
    '''Функция находит пересечение в двух списках и записывает в третий'''
    # Добавляем элементы из первого списка в третий, если они есть во втором списке
    list3 = [elem for elem in list1 if elem in list2]
    return f'{list3=}'


print('\nНайти пересечение в 2 списках и записать в 3 список эти пересечения')
# Создаем два списка, заполненные рандомными числами длиной 10 элементов
my_list1 = [randint(1, 20) for _ in range(10)]
my_list2 = [randint(1, 20) for _ in range(10)]

print(f'Исходные данные: \n{my_list1=} \n{my_list2=}')
print(intersection_list(my_list1, my_list2))
