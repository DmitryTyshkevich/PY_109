import csv

'''
Дополнительная задача:
1. Создать класс "Сотрудник"
2. Определить атрибуты класса: имя, фамилия, должность, зарплата
3. Определить конструктор класса для инициализации атрибутов
4. Реализовать методы для изменения и получения значений каждого атрибута
5. Реализовать метод для вывода информации о сотруднике на экран
6. Создать несколько объектов класса "Сотрудник"
7. Продемонстрировать работу методов на созданных объектах
Расширение задачи:
8. Добавить в класс "Сотрудник" метод для изменения зарплаты на заданное значение
9. Добавить в класс "Сотрудник" метод для увеличения зарплаты на заданное процентное значение
10. Добавить в класс "Сотрудник" метод для сравнения зарплаты текущего объекта с зарплатой другого объекта 
класса "Сотрудник"
11. Продемонстрировать работу новых методов на созданных объектах.

**** реализовать метод, который будет записывать в CSV-файл изменение зарплаты по сотруднику
(в момент изменения зарплаты - создается запись в CSV)
'''


class Employee:

    def __init__(self, first_name, last_name, position, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.position = position
        self.salary = salary

    def name_change(self):
        '''Метод для изменения имени'''
        self.first_name = input(f'Введите новое имя для {self.first_name} {self.last_name}: ').capitalize()
        return self.first_name

    def surname_change(self):
        '''Метод для изменения фамилии'''
        self.last_name = input(f'Введите новую фамилию для {self.first_name} {self.last_name}: ').capitalize()
        return self.last_name

    def position_change(self):
        '''Метод для изменения должности'''
        self.position = input(f'Введите новую должность для {self.first_name} {self.last_name}: ').capitalize()
        return self.position

    def salary_change(self):
        '''Метод для изменения заработной платы'''
        self.salary = int(input(f'Введите новый уровень заработной платы для {self.first_name} {self.last_name}: '))
        return self.salary

    def employee_information(self):
        '''Метод для вывода информации о сотруднике'''
        print(f'\nИмя: {self.first_name}\nФамилия: {self.last_name}\nДолжность: {self.position}\n'
              f'Заработная плата: {self.salary}$\n')

    def salary_increase(self):
        '''Метод для увеличения зарплаты на заданное процентное значение'''
        percent = int(input(f'На сколько процентов увеличиваем зп для {self.first_name} {self.last_name}?: '))
        result = self.salary * (percent / 100)
        self.salary += result

    def salary_comparison(self, obj):
        '''Метод для сравнения зарплат'''
        print(f'ЗП текущего объекта - {self.first_name} {self.last_name} ({self.position}): {self.salary}$'
              f'\nЗП другого объекта - {obj.first_name} {obj.last_name} ({obj.position}): {obj.salary}$')

    def salary_change_with_entry(self):
        '''Метод для изменения заработной платы с записью в csv-файл'''
        new_salary = int(input(f'\nВведите новый уровень заработной платы для {self.first_name} {self.last_name}: '))
        with open('../file/Salary_employee.csv', 'w', encoding='utf-8') as w_file:
            file_writer = csv.writer(w_file, delimiter=',', lineterminator='\r')
            file_writer.writerow(['Имя', 'Фамилия', 'Должность', 'ЗП до изменения', 'ЗП после изменения'])
            file_writer.writerow([self.first_name, self.last_name, self.position, self.salary, new_salary])

        self.salary = new_salary
        return self.salary


'''Часть 1'''

employee_1 = Employee('Михаил', 'Зубенко', 'Вор в законе', 1_000_000)
employee_1.employee_information()
employee_2 = Employee('Франко', 'Коломбо', 'Бодибилдер', 25_000_000)
employee_2.position_change()
employee_2.salary_change()
employee_2.employee_information()

'''Часть 2'''

employee_2.salary_increase()
employee_2.salary_comparison(employee_1)
employee_1.salary_change_with_entry()
