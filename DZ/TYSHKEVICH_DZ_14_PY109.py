'''Homework (OOP)'''

'''Два метода в классе, один принимает в себя либо строку, либо чмсло.
Если передаем строку, то смотрим:
- если произведение гласных и согласных букв меньше или равно длине слова:
выводить все гласные, иначе согласные;
- если число: то произведение суммы четных цифр на длину числа.
Длину строки и числа искать во втором методе'''


class Example:
    def __init__(self):
        self.obj = input('Введите слово или число: ').lower()

    def string_or_number(self, length):
        if self.obj.isalpha():
            vowels = ('а', 'я', 'у', 'ю', 'о', 'е', 'ё', 'э', 'и', 'ы',
                      'a', 'e', 'i', 'o', 'u', 'y')

            consonants = ('б', 'в', 'г', 'д', 'ж', 'з', 'й', 'к', 'л', 'м',
                          'н', 'п', 'р', 'с', 'т', 'ф', 'х', 'ц', 'ч', 'ш',
                          'щ', 'p', 'b', 'k', 'f', 'v', 'm', 'z', 'h', 't',
                          'd', 'l', 'n', 's')

            all_vowels = [letter for letter in self.obj if letter in vowels]
            all_consonants = [letter for letter in self.obj if letter in consonants]
            if len(all_vowels) * len(all_consonants) <= length:
                print('Произведение гласных и согласных букв не больше длины слова! \
                \nВыводим гласные:', *all_vowels)
            else:
                print('Произведение гласных и согласных букв больше длины слова! \
                \nВыводим согласные:', *all_consonants)

        elif self.obj.isdigit():
            sum_even_numbers = sum(map(int, filter(lambda x: int(x) % 2 == 0, self.obj)))
            print('Произведение суммы четных чисел на длину числа:', sum_even_numbers * length)
        else:
            print('Некорректный ввод!')

    def len_obj(self):
        return len(self.obj)


while True:
    f = Example()
    f.string_or_number(f.len_obj())
    close = input('Продолжить? "д / н": ').lower()
    if close == 'н' or close == 'y':
        break



