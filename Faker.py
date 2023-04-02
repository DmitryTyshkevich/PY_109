from faker import Faker
# Создаем генератор фальшивых русских данных
fake = Faker("ru_RU")

# Гненрируем по отдельности мужское имя и фамилию
print("Данные пользователя №1:")
print(fake.first_name_male(), fake.last_name_male())
# Гненрируем адрес
print(fake.street_address())
print()

# Гненрируем по отдельности женское имя и фамилию
print("Данные пользователя №2:")
print(fake.first_name_female(), fake.last_name_female())
print(fake.street_address())
print()

# Гненрируем имя и фамилию
print("Данные пользователя №3:")
print(fake.name())
print(fake.street_address())