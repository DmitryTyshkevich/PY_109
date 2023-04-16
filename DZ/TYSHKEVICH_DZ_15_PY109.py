import string


class Human:
    default_name = 'No name'
    default_age = 0

    def __init__(self, name=default_name, age=default_age):
        self.name = name
        self.age = age
        self.__money = 0
        self.__house = None

    def info(self):
        '''Справочный метод для вывода динамических атрибутов экземпляра'''
        print(f'Имя: {self.name}\nВозраст: {self.age}\nДеньги: {self.__money}\nДом: {self.__house}')

    @staticmethod
    def default_info():
        '''Справочный статический метод для вывода статических атрибутов'''
        print(Human.default_name, Human.default_age)

    def earn_money(self, x):
        '''Метод для увеличения денег объекта'''
        self.__money += x
        return self.__money

    def __make_deal(self, obj, price):
        '''Метод, отвечающий за техническую реализацию покупки дома'''
        self.__money -= price
        self.__house = obj

    def buy_house(self, obj, discount):
        '''Метод проверяет, достаточно ли денег для покупки дома и совершает сделку'''
        fin_price = obj.final_price(discount)
        if self.__money >= fin_price:
            self.__make_deal(obj, fin_price)
        else:
            print('Не хватает денег!')


class House:
    def __init__(self, area, price):
        self._area = area
        self._price = price

    def final_price(self, discount):
        '''Метод влзвращает цену с учетом скидки'''
        if isinstance(discount, int):
            self._price -= self._price * (discount / 100)
            return self._price


class SmallHouse(House):
    square = 40

    def __init__(self, price):
        super().__init__(SmallHouse.square, price)


Human.default_info()
print()
dmitry = Human('Dmitry', 30)
dmitry.info()
dmitry.earn_money(1_000)
print()
dmitry.info()

small_house = SmallHouse(56_000)
dmitry.buy_house(small_house, 25)
dmitry.info()
print()
dmitry.earn_money(1_000_000)
dmitry.buy_house(small_house, 25)
dmitry.info()
print(small_house._area)


# =======================================================================================================================

class Alphabet:
    def __init__(self, lang, letters):
        self.lang = lang
        self.letters = list(letters)

    def print(self):
        '''Метод выводит в консоль буквы алфавита'''
        print(f'Буквы алфавита({self.lang}): ', *self.letters, sep='')

    def letters_num(self):
        '''Метод возвращает количество букв в алфавите'''
        return len(self.letters)


class EngAlphabet(Alphabet):
    __letters_num = 26

    def __init__(self, lang, letters):
        super().__init__(lang, letters)

    def is_en_letter(self, letter):
        '''Метод определяет относится ли буква к алфавиту'''
        if letter.lower() not in self.letters:
            return f'Буквы "{letter}" нет в английском алфавите'
        return f'Буква "{letter}" есть в английском алфавите'

    def letters_num(self):
        '''Метод возвращает значение статического свойства'''
        return EngAlphabet.__letters_num

    @staticmethod
    def example():
        '''Статический метод, который возвращает пример текста на англ. языке'''
        return "Hello world!"


eng = EngAlphabet('EN', string.ascii_lowercase)
eng.print()
print(f'Количество букв в алфавите - {eng.letters_num()}')
print(eng.is_en_letter('F'))
print(eng.is_en_letter('Щ'))
print(eng.example())


# =======================================================================================================================
class Tomato:
    '''Класс: Томат'''

    states = {
        1: 'Фаза прорастания',
        2: 'Фаза роста',
        3: 'Фаза цветения',
        4: 'Фаза созревания и плодоношения'
    }

    def __init__(self, index=1):
        self._index = index
        self._state = self.states[self._index]

    def grow(self):
        '''Метод перевода томата на след. стадию созревания'''
        self._index += 1
        self._state = self.states[self._index]

    def is_ripe(self):
        '''Метод проверяет достиг ли томат последней стадии созревания'''
        return self._state == self.states[4]


class TomatoBush:
    '''Класс: Томатный куст'''

    def __init__(self, number_of_tomatoes):
        self.tomatoes = [Tomato() for _ in range(number_of_tomatoes)]

    def grow_all(self):
        '''Метод переводит все объекты из списка томатов на след. этап созревания'''
        for obj in self.tomatoes:
            obj.grow()

    def all_are_ripe(self):
        '''Метод проверяет все ли томаты из списка стали спелыми'''
        return all([obj.is_ripe() for obj in self.tomatoes])

    def give_away_all(self):
        '''Метод очищвет список томатов после сбора урожая'''
        self.tomatoes.clear()


class Gardener:
    '''Класс: Садовник'''

    def __init__(self, name, plant):
        self.name = name
        self._plant = plant

    def work(self):
        '''Метод заставляет садовника работать, что позволяет растению
        становиться более зрелым'''
        self._plant.grow_all()

    def harvest(self):
        '''Метод проверяет все ли плоды созрели.
        если все- собираем урожай, если нет- выводит предупреждение'''
        if self._plant.all_are_ripe():
            print('Плоды готовы к сбору урожая!\nCобираем урожай!')
            self._plant.give_away_all()
        else:
            print(f'Плоды еще не созрели!')

    @staticmethod
    def knowledge_base(gardener):
        '''Метод выводит справку по садоводству'''
        print("\nСправочная информация по садоводству:")
        print(f'Садовником является: {gardener.name}\n'
              f'Количество плодов на кусте томата: {len(gardener._plant.tomatoes)} шт.')
        print('Чтобы собрать урожай нужно пройти 4 стадии созревания:')
        for number, state in Tomato.states.items():
            print(f'{number}-ая стадия: {state}')

        try:
            print(f'Стадия зосревания на данный момент: {gardener._plant.tomatoes[0]._state}\n')
        except IndexError:
            print('Урожай собран, так как достигнута фаза созревания и плодоношения!')


bush = TomatoBush(5)
gardener = Gardener('Miha', bush)
gardener.knowledge_base(gardener)
gardener.work()
gardener.harvest()
gardener.work()
gardener.harvest()
gardener.work()
gardener.harvest()
gardener.knowledge_base(gardener)
