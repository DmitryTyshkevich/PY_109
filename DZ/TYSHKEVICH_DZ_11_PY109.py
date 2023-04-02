'''Homework №11'''

'''Задание №2'''


def sorted_file(file):
    '''функция считывает строки из файла и возвращает отосортированный список'''
    file1 = file.read().split()
    print(f'Содержание файла {file1}')
    file2 = file1.copy()
    list_num = sorted(int(num) for num in file1 if num.isdigit())
    list_str = sorted(line for line in file2 if line.isalpha())
    result = list_num + list_str
    return result


with open('../file/newexample.txt', encoding='utf-8') as file:
    print(sorted_file(file))

'''Задание №3'''


def data_recording(file):
    '''функция записывает данные в файл'''
    text = input('Введите данные для записи в файл:\n'
                 'Для окончания нажмите Enter:\n>>> ')
    while text:
        file.write(text + '\n')
        text = input('Введите данные для записи в файл:\n'
                     'Для окончания нажмите Enter:\n>>> ')


with open('../file/output_file.txt', 'w') as f:
    data_recording(f)

'''Задание №4'''


def counting_strings_characters(file):
    '''функция подсчитывает кол-во строк в файле,
    а также для каждой строки кол-во символов'''
    list_str = [string.rstrip() for string in f]
    print(f'Количество строк в файле: {len(list_str)}')
    for str in list_str:
        print(f'В строке {str} - {len(str)} символов')


with open('../file/output_file.txt') as f:
    counting_strings_characters(f)

'''Домашняя задача'''


def file_recording(list_, file):
    '''Функция записывает в файл из массива сначала слова в порядке
    их длины, а после слов цифры в порядке возрастания'''
    list_words = sorted([word for word in list_ if isinstance(word, str)], key=lambda x: len(x))
    list_numbers = sorted(num for num in list_ if isinstance(num, int))
    for word in list_words:
        file.write(word + '\n')

    for num in list_numbers:
        file.write(str(num) + '\n')


list_ = [123, 'watermelon', 'banana', 43, 'cat', 'dog', 3, 0]

with open('../file/f1.txt', 'w') as f:
    file_recording(list_, f)
