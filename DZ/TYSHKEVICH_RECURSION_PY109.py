def list_alignment(list_):
    if list_ == []:
        return list_
    if isinstance(list_[0], list):
        return list_alignment(list_[0]) + list_alignment(list_[1:])
    return (list_[:1] + list_alignment(list_[1:]))


my_list = [
    [1, 2, 3, 4, [6, 7, 8, 9, [10, 11, 12], 13], 14], [15, [16, 17, 18], 19, [20]]
]

print(list_alignment(my_list))


# **********************************************************************************************************************

def GetFibonacciList(n, L):
    # Проверить, корректна ли длина списка
    count = len(L)

    if len(L) < 2:
        return []

    # Получить последние числа в списке L
    num1 = L[count - 2]
    num2 = L[count - 1]

    # Формула расчета следующего числа
    if (num1 + num2) < n:
        L = L + [num1 + num2]
        return GetFibonacciList(n, L)  # вызвать рекурсивно функцию
    else:
        return L  # если достигнут конец, то обычный выход


# Вызвать функцию GetFibonacciList()
fib = GetFibonacciList(8, [0, 1])
print(fib)