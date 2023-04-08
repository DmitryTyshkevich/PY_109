import pandas as pd

''' Pandas - это высокоуровневая библиотека для обработки и  анализа табличных данных. Высокоуровневая - потому что 
построена она поверх более низкоуровневой библиотеки NumPy (написана на Си), что является большим плюсом 
в производительности. В экосистеме Python, pandas является наиболее продвинутой и быстроразвивающейся библиотекой для 
обработки и анализа данных.

    Pandas используют для того, чтобы:

●	Группировать данные по определённым признакам.
●	Создавать сводные таблицы из нескольких.
●	Очищать данные от дубликатов и невалидных строк или столбцов.
●	Выводить определённые значения по фильтрам или уникальности.
●	Использовать агрегирующие функции, например подсчёт значений, сумму элементов, среднее значение.
●	Визуализировать собранные данные.

●  Чтобы эффективно работать с pandas, необходимо освоить самые главные структуры данных библиотеки: 
Series и DataFrame.

                                                 <<< Series >>>

    Series представляет из себя объект, похожий на одномерный массив (список), но отличительной его 
чертой является наличие ассоциированных меток (индексов) вдоль каждого элемента из списка. 
Такая особенность превращает его в ассоциативный массив или словарь.
'''
'''Создать объект класса Series можно следующим образом: s = pd.Series(data, index=index)'''

my_series = pd.Series([1.0, 6, 7, 8, 9, 10])
print(my_series)

''' Доступ к элементам объекта Series возможны по их индексу: '''

print(f'\n>>>Доступ к элементу Series по индексу:\n{my_series[4]}')

''' Индексы можно задавать явно: '''

my_series2 = pd.Series([5, 6, 7, 8, 9, 10], index=['a', 'b', 'c', 'd', 'e', 'f'])
print(f'\n>>>Объект Series с явно заданными индексами:\n{my_series2}')

''' У объекта Series есть атрибуты через которые можно получить список элементов и индексы, это values и index.'''

print(f'\n>>>Индексы объекта Series:\n{my_series2.index}')

print(f'\n>>>Список элементов объекта Series:\n{my_series2.values}')

''' Выборка по нескольким индексам и групповое присваивание: '''

print('\n>>>Выборка по нескольким индексам:')
print(my_series2[['e', 'b', 'f']])

print('\n>>>Групповое присваивание:')
my_series2[['a', 'b', 'f']] = 0
print(my_series2)

''' Series можно фильтровать, а также применять математические операции и многое другое: '''

print('\n>>>Вывод элементов > 0:')
print(my_series2[my_series2 > 0])

print('\n>>>Умножение элеиентов > 0 на 2:')
print(my_series2[my_series2 > 0])
2
''' Если Series напоминает нам словарь, где ключом является индекс, а значением сам элемент, то в конструктор можно
передать сам словарь: '''

my_series3 = pd.Series({'a': 5, 'b': 6, 'c': 7, 'd': 8})
print("\n>>>Словарь {'a': 5, 'b': 6, 'c': 7, 'd': 8} как объект Series:")
print(my_series3)

''' У объекта Series и его индекса есть атрибут name, задающий имя объекту и индексу: '''

my_series3.name = 'numbers'
my_series3.index.name = 'letters'
print('\n>>>Задаем имя объекту и индексу:')
print(my_series3)

''' Индекс можно поменять "на лету", присвоив список атрибуту index объекта Series: '''
my_series3.index = ['A', 'B', 'C', 'D']
print('\n>>>Изменение индексов:')
print(my_series3)

'''Методы Index:

    Есть методы для получения информации об индексах из структуры данных. Например, idxmin() и idxmax() — структуры, 
возвращающие индексы с самым маленьким и большим значениями '''

print(f"\nИндекс с самым маленьким значением:\n{my_series3.idxmin()}")

series4 = pd.Series(range(6), index=['white', 'white', 'blue', 'green', 'green', 'yellow'])

''' В случае с маленькими структурами легко определять любые повторяющиеся индексы, но если структура большая, то растет 
и сложность этой операции. Для этого в pandas у объектов Index есть атрибут is_unique. Он сообщает, есть ли индексы с 
повторяющимися метками в структуре (Series или Dataframe).'''

print(f'\n{series4}')
print(f"\nЕсть ли повторяющиеся индексы:\n{series4.is_unique}")
