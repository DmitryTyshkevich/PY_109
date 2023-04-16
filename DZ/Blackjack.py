'''Blackjack'''
from random import randint

# Раздача карт дилеру
dealer_card_1 = randint(2, 11)
dealer_card_2 = randint(2, 11)

# Раздача карт игроку
player_card_1 = randint(2, 11)
player_card_2 = randint(2, 11)

# Подсчитываем карты у дилера и игрока
combination_dealer = dealer_card_1 + dealer_card_2
combination_player = player_card_1 + player_card_2

# Выводим комбинации участников игры на экран
print('У дилера выпало -', combination_dealer)
print('У игрока выпало -', combination_player)






