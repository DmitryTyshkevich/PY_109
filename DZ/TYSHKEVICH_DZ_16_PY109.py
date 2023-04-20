def debug(func):
    def wrapper(*args, **kwargs):
        '''Функция добовляет справочную информацию к передаваемой функции'''
        print(f'Имя функции: {func.__name__}', '\nАргументы: ', *args,
              f'\nРезультат работы функции: {func(*args, **kwargs)}')
        return func(*args, **kwargs)

    wrapper.__name__ = func.__name__
    wrapper.__doc__ = func.__doc__
    return wrapper


@debug
def mult(a, b):
    '''Функция умножает параметр а на b'''
    return a * b


print(mult.__doc__)
mult(3, 4)


# ======================================================================================================================


def decorator(func):
    '''декоратор возвращает количество значений, не кратных 3 из первоначального списка'''

    def wrapper(*args, **kwargs):
        count = [n for item in args[0] for n in item if n % 3 != 0]
        print(f'Список значений кратных 3: {func(*args, **kwargs)}')
        return f'Количество значений не кратных 3: {len(count)}'

    return wrapper


@decorator
def func(lst):
    '''Функция возвращает список со значениями кратных 3'''
    new_list = [num for item in lst for num in item if num % 3 == 0]
    return new_list


list_numbers = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(func(list_numbers))
